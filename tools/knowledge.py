"""Validate and index Markdown knowledge. No engine execution or condition inference."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker


class KnowledgeError(ValueError):
    pass


class StrictLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys rather than silently replacing knowledge."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            if key in result:
                raise KnowledgeError(f"Duplicate YAML key: {key}")
            result[key] = loader.construct_object(value_node, deep=deep)
        except TypeError as exc:
            raise KnowledgeError("YAML mapping keys must be scalar") from exc
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_yaml(text):
    try:
        return yaml.load(text, Loader=StrictLoader)
    except yaml.YAMLError as exc:
        raise KnowledgeError(f"Invalid YAML: {exc}") from exc


def read_text(path):
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (UnicodeError, OSError) as exc:
        raise KnowledgeError(f"Cannot read UTF-8 file {path}: {exc}") from exc
    if "\ufffd" in text:
        raise KnowledgeError(f"Replacement character found in {path}")
    return text


def schema_validator(root, name):
    schema = json.loads(read_text(root / "schemas" / name))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_schema(validator, data, label):
    errors = sorted(validator.iter_errors(data), key=lambda e: str(list(e.path)))
    if errors:
        raise KnowledgeError("\n".join(
            f"{label}: {'/'.join(map(str, e.path)) or '<metadata>'}: {e.message}"
            for e in errors
        ))


@dataclass
class Node:
    path: Path
    metadata: dict
    body: str
    digest: str


def parse_node(root, path, validator):
    text = read_text(path)
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise KnowledgeError(f"{path}: Missing YAML Front Matter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise KnowledgeError(f"{path}: Unclosed YAML Front Matter") from exc
    metadata = load_yaml("\n".join(lines[1:end]))
    validate_schema(validator, metadata, str(path.relative_to(root)))
    body = "\n".join(lines[end + 1:]).strip()
    prose = re.sub(r"(?m)^\s*#+[^\n]*$", "", body).strip()
    if not prose:
        raise KnowledgeError(f"{path}: Empty knowledge body")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*\.md", path.name):
        raise KnowledgeError(f"{path}: Use an English kebab-case filename")
    return Node(path, metadata, body, hashlib.sha256(text.encode("utf-8")).hexdigest())


def find_cycle(graph):
    """Iterative DFS supports growing repositories without recursion limits."""
    done = set()
    for start in sorted(graph):
        if start in done:
            continue
        active = [start]
        positions = {start: 0}
        stack = [iter(sorted(graph.get(start, [])))]
        while stack:
            target = next(stack[-1], None)
            if target is None:
                completed = active.pop()
                done.add(completed)
                positions.pop(completed)
                stack.pop()
            elif target in positions:
                return active[positions[target]:] + [target]
            elif target not in done:
                positions[target] = len(active)
                active.append(target)
                stack.append(iter(sorted(graph.get(target, []))))
    return None


def is_dependency(relation, config):
    rule = config["relations"][relation["type"]]["dependency"]
    return rule is True or (rule == "required" and relation.get("requirement") == "required")


def markdown_links(text):
    """Basic inline, reference and image paths, excluding code examples."""
    visible = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is None:
            visible.append(line)
    text = re.sub(r"(`+).*?\1", "", "\n".join(visible))
    references = {}
    for match in re.finditer(r"(?m)^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)", text):
        references[match[1].casefold().strip()] = match[2].strip("<>")
    links = [match[1].strip("<>") for match in re.finditer(
        r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\s*\)", text
    )]
    for match in re.finditer(r"!?\[([^\]\n]+)\](?:\[([^\]\n]*)\])?(?![(:])", text):
        label = (match[2] or match[1]).casefold().strip()
        if label in references:
            links.append(references[label])
    return links


def validate_links(root, nodes, documents):
    by_path = {node.path.resolve(): node for node in nodes.values()}
    for path in documents:
        if not path.resolve().is_relative_to(root):
            raise KnowledgeError(f"Document leaves repository: {path}")
        source = by_path.get(path.resolve())
        text = source.body if source else read_text(path)
        declared = set()
        if source:
            data = source.metadata
            declared.update(r["target"] for r in data["relations"])
            declared.update(data["evidence"])
            declared.update(data.get("superseded_by", []))
            declared.update(c["target"] for c in data.get("evidence_details", {}).get("claims", []))
        for link in markdown_links(text):
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(root):
                raise KnowledgeError(f"{path.relative_to(root)}: Link leaves repository: {link}")
            if not target.exists():
                raise KnowledgeError(f"{path.relative_to(root)}: Missing local link: {link}")
            if source and target in by_path and by_path[target].metadata["id"] not in declared:
                raise KnowledgeError(f"{path.relative_to(root)}: Node link is not declared in metadata: {link}")


def validate_evidence(nodes, node_id, data):
    def records(ids):
        return [nodes[item].metadata for item in ids]

    for evidence_id in data["evidence"] + [item for r in data["relations"] for item in r.get("evidence", [])]:
        if nodes[evidence_id].metadata["kind"] != "evidence":
            raise KnowledgeError(f"{node_id}: Not an Evidence node: {evidence_id}")
    details = data.get("evidence_details")
    if details:
        for claim in details["claims"]:
            if claim["target"] not in nodes:
                raise KnowledgeError(f"{node_id}: Missing claim target: {claim['target']}")
        if details["source_kind"] == "official-documentation" and not details["sources"]:
            raise KnowledgeError(f"{node_id}: Official documentation needs source URLs")
    if data["status"] != "validated" and data.get("compatibility", {}).get("verification") != "engine-tested":
        return
    evidence = [item for item in records(data["evidence"])
                if item["status"] in {"reviewed", "validated"}
                and item["evidence_details"]["source_kind"] != "hypothesis"
                and any(c["target"] == node_id for c in item["evidence_details"]["claims"])
                and item["evidence_details"]["checked_at"] is not None]
    if not evidence:
        raise KnowledgeError(f"{node_id}: Validated/engine-tested requires reviewed, scoped Evidence")
    if data["kind"] in {"recipe", "adapter"} or data.get("compatibility", {}).get("verification") == "engine-tested":
        executed = [item for item in evidence if item["evidence_details"]["source_kind"] in
                    {"reproduced-test", "first-party-experiment", "production-observation"}
                    and item["evidence_details"].get("execution")]
        if not executed:
            raise KnowledgeError(f"{node_id}: Recipe/Adapter needs engine execution Evidence")
        if data["scope"] == "engine-specific":
            compatibility = data["compatibility"]
            if compatibility["verification"] != "engine-tested" or not compatibility["engine_version"] or not compatibility["renderer"] or not compatibility["platforms"]:
                raise KnowledgeError(f"{node_id}: Engine-tested compatibility must name tested conditions")
            if not any(item["evidence_details"]["execution"]["engine"] == data["engine"]
                       and item["evidence_details"]["execution"]["engine_version"] == compatibility["engine_version"]
                       and item["evidence_details"]["execution"]["renderer"] == compatibility["renderer"]
                       for item in executed):
                raise KnowledgeError(f"{node_id}: Execution Evidence does not match compatibility")


def load_repository(root):
    root = root.resolve()
    config = json.loads(read_text(root / "schemas" / "graph-config.json"))
    validator = schema_validator(root, "node.schema.json")
    nodes, paths = {}, set()
    for folder in config["node_roots"]:
        directory = (root / folder).resolve()
        if not directory.is_relative_to(root):
            raise KnowledgeError(f"Node root leaves repository: {folder}")
        for path in sorted(directory.rglob("*.md")):
            if not path.resolve().is_relative_to(root):
                raise KnowledgeError(f"Node leaves repository: {path}")
            relative = path.relative_to(root).as_posix().casefold()
            if relative in paths:
                raise KnowledgeError(f"Case-insensitive duplicate path: {relative}")
            paths.add(relative)
            node = parse_node(root, path, validator)
            node_id, data = node.metadata["id"], node.metadata
            if node_id in nodes:
                raise KnowledgeError(f"Duplicate ID: {node_id}")
            if node_id.split("/", 1)[0] != data["kind"]:
                raise KnowledgeError(f"{node_id}: ID namespace does not match kind")
            if set(data["tags"]) - set(config["tags"]):
                raise KnowledgeError(f"{node_id}: Unknown tags: {sorted(set(data['tags']) - set(config['tags']))}")
            nodes[node_id] = node
    if not nodes:
        raise KnowledgeError("No knowledge nodes found")
    dependencies, replacements = {}, {}
    for node_id, node in nodes.items():
        data = node.metadata
        references = data["evidence"] + data.get("superseded_by", [])
        references += [r["target"] for r in data["relations"]]
        references += [item for r in data["relations"] for item in r.get("evidence", [])]
        for target in references:
            if target not in nodes:
                raise KnowledgeError(f"{node_id}: Missing reference: {target}")
        for relation in data["relations"]:
            rule = config["relations"][relation["type"]]
            if rule.get("target_kinds") and nodes[relation["target"]].metadata["kind"] not in rule["target_kinds"]:
                raise KnowledgeError(f"{node_id}: Invalid target kind for {relation['type']}")
        dependencies[node_id] = [r["target"] for r in data["relations"] if is_dependency(r, config)]
        replacements[node_id] = data.get("superseded_by", [])
        if replacements[node_id] and data["status"] != "deprecated":
            raise KnowledgeError(f"{node_id}: superseded_by is only allowed for deprecated nodes")
        validate_evidence(nodes, node_id, data)
    for name, graph in [("Mandatory dependency", dependencies), ("Replacement", replacements)]:
        cycle = find_cycle(graph)
        if cycle:
            raise KnowledgeError(f"{name} cycle: {' -> '.join(cycle)}")
    documents = set(root.glob("*.md")) | {node.path for node in nodes.values()}
    for folder in config["document_roots"]:
        directory = (root / folder).resolve()
        if not directory.is_relative_to(root):
            raise KnowledgeError(f"Document root leaves repository: {folder}")
        documents.update(directory.rglob("*.md"))
    validate_links(root, nodes, sorted(documents))
    return nodes, config


def generate_index(root, nodes, config):
    entries, backlinks, symmetric = [], {node_id: [] for node_id in nodes}, {node_id: [] for node_id in nodes}
    for node_id, node in sorted(nodes.items()):
        entries.append({**node.metadata, "path": node.path.relative_to(root).as_posix(), "sha256": node.digest})
        for position, relation in enumerate(node.metadata["relations"]):
            entry = {"source": node_id, "relation_index": position, **relation}
            backlinks[relation["target"]].append(entry)
            if config["relations"][relation["type"]]["symmetric"]:
                symmetric[relation["target"]].append({**entry, "target": node_id, "derived": True})
        for evidence_id in node.metadata["evidence"]:
            backlinks[evidence_id].append({"source": node_id, "type": "evidence"})
        for relation_index, relation in enumerate(node.metadata["relations"]):
            for evidence_id in relation.get("evidence", []):
                backlinks[evidence_id].append({"source": node_id, "type": "relation-evidence", "relation_index": relation_index})
        for target in node.metadata.get("superseded_by", []):
            backlinks[target].append({"source": node_id, "type": "superseded_by"})
        for claim in node.metadata.get("evidence_details", {}).get("claims", []):
            backlinks[claim["target"]].append({"source": node_id, "type": "claim", "statement": claim["statement"]})
    result = {"schema_version": "0.1.0", "generated": True, "nodes": entries,
              "backlinks": dict(sorted(backlinks.items())), "symmetric_relations": dict(sorted(symmetric.items()))}
    payload = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    rows = ["# 知識索引（自動生成）", "", "`python tools/knowledge.py index` で再生成する。直接編集しない。", "", "| ID | 名前 | 状態 |", "| --- | --- | --- |"]
    for entry in entries:
        title = entry["title"].replace("|", "\\|").replace("\n", " ")
        rows.append(f"| `{entry['id']}` | [{title}](../{entry['path']}) | {entry['status']} |")
    return {"nodes.json": payload, "README.md": "\n".join(rows) + "\n"}


def resolve_dependencies(nodes, config, selection):
    decisions = {}
    for decision in selection["conditional_decisions"]:
        source, position = decision["source"], decision["relation_index"]
        if source not in nodes or nodes[source].metadata["revision"] != decision["source_revision"]:
            raise KnowledgeError(f"Unknown source or outdated decision revision: {source}")
        relations = nodes[source].metadata["relations"]
        if position >= len(relations) or not is_dependency(relations[position], config) or "when" not in relations[position]:
            raise KnowledgeError(f"Decision must identify a conditional mandatory relation: {source}#{position}")
        if (source, position) in decisions:
            raise KnowledgeError(f"Duplicate condition decision: {source}#{position}")
        decisions[source, position] = decision
    included, excluded, unresolved = set(), [], []
    pending = list(selection["selected_nodes"])
    while pending:
        node_id = pending.pop()
        if node_id in included:
            continue
        if node_id not in nodes:
            raise KnowledgeError(f"Unknown selected node: {node_id}")
        data = nodes[node_id].metadata
        if data["scope"] == "engine-specific" and data["engine"] != selection["engine"]:
            raise KnowledgeError(f"{node_id}: Engine differs from the explicitly selected engine")
        included.add(node_id)
        for position, relation in enumerate(data["relations"]):
            if not is_dependency(relation, config):
                continue
            edge = {"source": node_id, "relation_index": position, **relation}
            if "when" in relation:
                decision = decisions.get((node_id, position))
                if decision is None:
                    unresolved.append(edge)
                    continue
                edge["decision_reason"] = decision["reason"]
                if not decision["applies"]:
                    excluded.append(edge)
                    continue
            pending.append(relation["target"])
    unused = [f"{source}#{position}" for source, position in decisions if source not in included]
    if unused:
        raise KnowledgeError(f"Condition decisions outside adopted dependency graph: {', '.join(unused)}")
    return {"selected_nodes": selection["selected_nodes"], "engine": selection["engine"],
            "required_nodes": sorted(included), "excluded_conditional_dependencies": excluded,
            "unresolved_conditions": unresolved, "conditions_evaluated_automatically": False,
            "engine_compatibility_verified": False,
            "conditional_decisions": selection["conditional_decisions"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate", help="Validate structure, never engine quality")
    validate.add_argument("--check-index", action="store_true")
    commands.add_parser("index", help="Regenerate deterministic derived indexes")
    search = commands.add_parser("search", help="Search metadata; results are candidates")
    search.add_argument("query")
    search.add_argument("--kind")
    search.add_argument("--engine")
    search.add_argument("--status")
    related = commands.add_parser("related", help="Browse outgoing links and backlinks without adoption")
    related.add_argument("id")
    dependencies = commands.add_parser("dependencies", help="Resolve mandatory dependencies after explicit selection")
    dependencies.add_argument("selection", type=Path)
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        nodes, config = load_repository(root)
        if args.command in {"index", "validate"}:
            generated = generate_index(root, nodes, config)
            for name, content in generated.items():
                path = root / "index" / name
                if args.command == "index":
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with path.open("w", encoding="utf-8", newline="\n") as output:
                        output.write(content)
                elif args.check_index and (not path.exists() or path.read_bytes() != content.encode("utf-8")):
                    raise KnowledgeError(f"Stale generated index: {path.relative_to(root)}; run index")
            print(f"{args.command}: {len(nodes)} nodes; structure only; engine execution not verified")
        elif args.command == "search":
            results = []
            for node_id, node in sorted(nodes.items()):
                data = node.metadata
                if any(getattr(args, key) and data.get(key) != getattr(args, key) for key in ("kind", "engine", "status")):
                    continue
                haystack = " ".join([node_id, data["title"], data["summary"], *data["aliases"], *data["tags"]]).casefold()
                if args.query.casefold() in haystack:
                    results.append({key: data[key] for key in ("id", "title", "summary", "kind", "status", "revision")})
            print(json.dumps(results, ensure_ascii=False, indent=2))
        elif args.command == "related":
            if args.id not in nodes:
                raise KnowledgeError(f"Unknown node: {args.id}")
            generated = json.loads(generate_index(root, nodes, config)["nodes.json"])
            print(json.dumps({"id": args.id, "outgoing": nodes[args.id].metadata["relations"],
                              "incoming": generated["backlinks"][args.id],
                              "symmetric_derived": generated["symmetric_relations"][args.id],
                              "adopts_nodes": False}, ensure_ascii=False, indent=2))
        else:
            selection = load_yaml(read_text(args.selection))
            validate_schema(schema_validator(root, "selection.schema.json"), selection, str(args.selection))
            result = resolve_dependencies(nodes, config, selection)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            if result["unresolved_conditions"]:
                return 2
    except (KnowledgeError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    raise SystemExit(main())
