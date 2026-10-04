"""Structure-only fixtures; no VFX execution or production evidence is implied."""

from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

from tools import knowledge


REPOSITORY = Path(__file__).resolve().parents[1]


class FoundationTests(unittest.TestCase):
    def setUp(self):
        self.work_base = REPOSITORY / ".test-work"
        self.work_base.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="knowledge-", dir=self.work_base)
        self.root = Path(self.temp.name).resolve()
        self.assertTrue(self.root.is_relative_to(self.work_base.resolve()))
        shutil.copytree(REPOSITORY / "schemas", self.root / "schemas")
        # Keep the original eight-node fixture independent of catalog growth.
        for relative in (
            "semantics/fireball.md", "semantics/magic-orb.md",
            "compositions/projectile.md",
            "recipes/fireball-readable-core.md", "recipes/magic-orb-readable-core.md",
            "techniques/mesh-core.md", "techniques/billboard.md",
            "evaluation/projectile-readability.md",
        ):
            destination = self.root / "knowledge" / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / "knowledge" / relative, destination)

    def tearDown(self):
        # Verify the final deletion target before TemporaryDirectory cleans recursively.
        if not self.root.is_relative_to(self.work_base.resolve()) or self.root == self.work_base.resolve():
            raise RuntimeError("Refusing to clean outside the test workspace")
        self.temp.cleanup()

    def load(self):
        return knowledge.load_repository(self.root)

    def data(self, node_id):
        nodes, _ = self.load()
        node = nodes[node_id]
        return node.path, deepcopy(node.metadata), node.body

    def write(self, path, data, body="これはテスト用の構造データであり、実際の制作・成功・実測を示す記録ではない。"):
        path.parent.mkdir(parents=True, exist_ok=True)
        content = "---\n" + yaml.safe_dump(data, allow_unicode=True, sort_keys=False) + "---\n\n" + body + "\n"
        with path.open("w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)

    def node(self, node_id, **changes):
        kind = node_id.split("/")[0]
        return {
            "schema_version": "0.1.0", "id": node_id, "kind": kind,
            "title": "構造確認用データ", "summary": "実機検証を表さないテストデータ。",
            "status": "draft", "revision": 1, "updated_at": "2026-10-04",
            "aliases": [], "tags": [], "scope": "engine-neutral",
            "relations": [], "evidence": [], "superseded_by": [], **changes,
        }

    def relation(self, target, relation_type="requires", **changes):
        return {"target": target, "type": relation_type, "reason": "構造テスト用の関係。", **changes}

    def selection(self, selected, engine=None, decisions=None):
        return {"selected_nodes": selected, "engine": engine, "conditional_decisions": decisions or []}

    def cli(self, *args):
        output, error = io.StringIO(), io.StringIO()
        with redirect_stdout(output), redirect_stderr(error):
            code = knowledge.main(["--root", str(self.root), *args])
        return code, output.getvalue(), error.getvalue()

    def test_real_nodes_are_draft_and_design_examples_are_not_registered(self):
        nodes, _ = self.load()
        self.assertEqual(len(nodes), 8)
        self.assertEqual({node.metadata["status"] for node in nodes.values()}, {"draft"})
        self.assertNotIn("technique/history-ribbon", nodes)
        self.assertFalse(any(node.metadata["kind"] == "adapter" for node in nodes.values()))

    def test_recipes_share_techniques_and_backlinks(self):
        nodes, config = self.load()
        index = json.loads(knowledge.generate_index(self.root, nodes, config)["nodes.json"])
        recipes = {"recipe/fireball-readable-core", "recipe/magic-orb-readable-core"}
        for technique in ("technique/mesh-core", "technique/billboard"):
            sources = {edge["source"] for edge in index["backlinks"][technique] if edge["type"] == "candidate"}
            self.assertEqual(sources, recipes)

    def test_one_role_has_multiple_candidates(self):
        nodes, _ = self.load()
        for node in nodes.values():
            if node.metadata["kind"] == "recipe":
                core = [r["target"] for r in node.metadata["relations"] if r["type"] == "candidate" and r.get("role") == "core"]
                self.assertEqual(set(core), {"technique/mesh-core", "technique/billboard"})

    def test_new_nodes_extend_index_search_and_backlinks_without_code_changes(self):
        new_technique = self.node("technique/new-concept", title="新しい技法", aliases=["新技法"])
        new_semantic = self.node("semantic/new-intent")
        new_recipe = self.node("recipe/new-combination", relations=[
            self.relation("semantic/new-intent", "expresses"),
            self.relation("technique/new-concept", "candidate", role="primary"),
            self.relation("technique/mesh-core", "candidate", role="primary"),
        ])
        for data in (new_technique, new_semantic, new_recipe):
            self.write(self.root / "knowledge" / data["kind"] / (data["id"].split("/")[1] + ".md"), data)
        self.assertEqual(self.cli("index")[0], 0)
        self.assertEqual(self.cli("validate", "--check-index")[0], 0)
        index = json.loads((self.root / "index/nodes.json").read_text(encoding="utf-8"))
        self.assertIn("recipe/new-combination", {r["source"] for r in index["backlinks"]["technique/new-concept"]})
        code, output, _ = self.cli("search", "新技法", "--kind", "technique")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output)[0]["id"], "technique/new-concept")

    def test_duplicate_id_is_rejected(self):
        _, data, body = self.data("technique/mesh-core")
        self.write(self.root / "knowledge/techniques/duplicate.md", data, body)
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Duplicate ID"):
            self.load()

    def test_missing_relation_is_rejected(self):
        path, data, body = self.data("technique/mesh-core")
        data["relations"].append(self.relation("technique/not-created", "candidate"))
        self.write(path, data, body)
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Missing reference"):
            self.load()

    def test_evidence_reference_must_refer_to_evidence(self):
        path, data, body = self.data("technique/mesh-core")
        data["evidence"] = ["technique/billboard"]
        self.write(path, data, body)
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Not an Evidence"):
            self.load()

    def test_conditional_mandatory_cycle_is_rejected(self):
        first = self.node("technique/first", relations=[self.relation("technique/second", when="条件Aの場合")])
        second = self.node("technique/second", relations=[self.relation("technique/first", "composes", requirement="required", when="条件Bの場合")])
        self.write(self.root / "knowledge/techniques/first.md", first)
        self.write(self.root / "knowledge/techniques/second.md", second)
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Mandatory dependency cycle"):
            self.load()

    def test_optional_and_general_related_cycles_are_allowed(self):
        first = self.node("technique/first", relations=[self.relation("technique/second", "candidate")])
        second = self.node("technique/second", relations=[self.relation("technique/first", "composes", requirement="optional")])
        self.write(self.root / "knowledge/techniques/first.md", first)
        self.write(self.root / "knowledge/techniques/second.md", second)
        self.assertEqual(len(self.load()[0]), 10)

    def test_candidate_alternative_enhancement_and_all_adapters_are_not_dependencies(self):
        path, data, body = self.data("technique/mesh-core")
        data["relations"].append(self.relation("technique/billboard", "enhances"))
        for engine in ("unity", "unreal", "godot"):
            adapter_id = f"adapter/{engine}-test"
            adapter = self.node(adapter_id, scope="engine-specific", engine=engine, compatibility={
                "engine_version": None, "renderer": None, "platforms": [], "verification": "unverified",
            })
            self.write(self.root / "adapters" / engine / "test.md", adapter)
            data["relations"].append(self.relation(adapter_id, "implemented_by"))
        self.write(path, data, body)
        nodes, config = self.load()
        result = knowledge.resolve_dependencies(nodes, config, self.selection(["recipe/fireball-readable-core", "technique/mesh-core"]))
        self.assertEqual(set(result["required_nodes"]), {"recipe/fireball-readable-core", "composition/projectile", "technique/mesh-core"})
        result = knowledge.resolve_dependencies(nodes, config, self.selection(["technique/mesh-core", "adapter/unity-test"], "unity"))
        self.assertEqual(set(result["required_nodes"]), {"technique/mesh-core", "adapter/unity-test"})
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Engine differs"):
            knowledge.resolve_dependencies(nodes, config, self.selection(["adapter/unity-test", "adapter/godot-test"], "unity"))

    def test_conditional_dependencies_remain_unresolved_without_decision(self):
        path, data, body = self.data("composition/projectile")
        data["relations"].append(self.relation("technique/billboard", when="対象の条件が成立する場合"))
        self.write(path, data, body)
        nodes, config = self.load()
        result = knowledge.resolve_dependencies(nodes, config, self.selection(["composition/projectile"]))
        self.assertEqual(result["required_nodes"], ["composition/projectile"])
        self.assertEqual(len(result["unresolved_conditions"]), 1)
        self.assertFalse(result["conditions_evaluated_automatically"])
        selection_path = self.root / "selection.yaml"
        selection_path.write_text(yaml.safe_dump(self.selection(["composition/projectile"])), encoding="utf-8")
        self.assertEqual(self.cli("dependencies", str(selection_path))[0], 2)

    def test_conditional_decisions_include_or_exclude_without_claiming_automatic_evaluation(self):
        path, data, body = self.data("composition/projectile")
        data["relations"].append(self.relation("technique/billboard", when="人またはAIが確認する条件"))
        self.write(path, data, body)
        nodes, config = self.load()
        decision = {"source": "composition/projectile", "source_revision": 1, "relation_index": 1, "applies": True, "reason": "テスト用の判断。実際の条件評価ではない。"}
        result = knowledge.resolve_dependencies(nodes, config, self.selection(["composition/projectile"], decisions=[decision]))
        self.assertIn("technique/billboard", result["required_nodes"])
        self.assertFalse(result["conditions_evaluated_automatically"])
        decision["applies"] = False
        result = knowledge.resolve_dependencies(nodes, config, self.selection(["composition/projectile"], decisions=[decision]))
        self.assertNotIn("technique/billboard", result["required_nodes"])
        self.assertEqual(len(result["excluded_conditional_dependencies"]), 1)
        decision["source_revision"] = 2
        with self.assertRaisesRegex(knowledge.KnowledgeError, "outdated decision"):
            knowledge.resolve_dependencies(nodes, config, self.selection(["composition/projectile"], decisions=[decision]))

    def test_validated_recipe_is_rejected_without_evidence(self):
        path, data, body = self.data("recipe/fireball-readable-core")
        data["status"] = "validated"
        self.write(path, data, body)
        with self.assertRaisesRegex(knowledge.KnowledgeError, "requires reviewed"):
            self.load()

    def test_documentation_evidence_cannot_validate_recipe_without_engine_execution(self):
        path, data, body = self.data("recipe/fireball-readable-core")
        data["status"] = "validated"
        data["evidence"] = ["evidence/documentation-test"]
        evidence = self.node("evidence/documentation-test", status="reviewed", evidence_details={
            "source_kind": "official-documentation",
            "claims": [{"target": data["id"], "statement": "構造テスト用。実際の仕様確認ではない。"}],
            "conditions": "テスト条件", "result": "テスト用の架空データ", "limitations": "実行なし",
            "sources": ["https://example.com/test"], "checked_at": "2026-10-04",
        })
        self.write(self.root / "evidence/documentation-test.md", evidence)
        self.write(path, data, body)
        with self.assertRaisesRegex(knowledge.KnowledgeError, "needs engine execution"):
            self.load()

    def test_adapter_requires_compatibility_metadata(self):
        adapter = self.node("adapter/test", scope="engine-specific", engine="test")
        self.write(self.root / "adapters/test.md", adapter)
        with self.assertRaisesRegex(knowledge.KnowledgeError, "compatibility"):
            self.load()

    def test_body_changes_make_generated_index_stale(self):
        self.assertEqual(self.cli("index")[0], 0)
        self.assertEqual(self.cli("validate", "--check-index")[0], 0)
        path, data, body = self.data("technique/billboard")
        self.write(path, data, body + "\n本文を変更する。")
        code, _, error = self.cli("validate", "--check-index")
        self.assertEqual(code, 1)
        self.assertIn("Stale generated index", error)
        self.assertEqual(self.cli("index")[0], 0)
        self.assertEqual(self.cli("validate", "--check-index")[0], 0)

    def test_stale_generated_links_do_not_prevent_regeneration(self):
        self.assertEqual(self.cli("index")[0], 0)
        path, _, _ = self.data("semantic/magic-orb")
        destination = path.parent / "moved-orb.md"
        path.rename(destination)
        # The old Markdown link is invalid until the move updates its caller.
        recipe_path = self.root / "knowledge/recipes/magic-orb-readable-core.md"
        recipe_text = recipe_path.read_text(encoding="utf-8").replace("../semantics/magic-orb.md", "../semantics/moved-orb.md")
        recipe_path.write_text(recipe_text, encoding="utf-8", newline="\n")
        self.assertEqual(self.cli("index")[0], 0)
        self.assertEqual(self.cli("validate", "--check-index")[0], 0)

    def test_index_generation_is_deterministic(self):
        nodes, config = self.load()
        self.assertEqual(knowledge.generate_index(self.root, nodes, config), knowledge.generate_index(self.root, nodes, config))

    def test_symmetric_relation_is_derived_without_mutating_source(self):
        nodes, config = self.load()
        index = json.loads(knowledge.generate_index(self.root, nodes, config)["nodes.json"])
        self.assertEqual(nodes["technique/billboard"].metadata["relations"], [])
        inverse = index["symmetric_relations"]["technique/billboard"]
        self.assertEqual(inverse[0]["target"], "technique/mesh-core")
        self.assertTrue(inverse[0]["derived"])

    def test_replacement_cycle_is_rejected(self):
        for source, target in (("first", "second"), ("second", "first")):
            self.write(self.root / f"knowledge/techniques/{source}.md", self.node(f"technique/{source}", status="deprecated", superseded_by=[f"technique/{target}"]))
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Replacement cycle"):
            self.load()

    def test_duplicate_yaml_key_is_rejected(self):
        path, _, _ = self.data("technique/billboard")
        text = path.read_text(encoding="utf-8").replace('revision: 1', 'revision: 1\nrevision: 2')
        path.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Duplicate YAML key"):
            self.load()

    def test_local_markdown_link_must_exist(self):
        (self.root / "README.md").write_text("[missing](not-created.md)\n", encoding="utf-8")
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Missing local link"):
            self.load()

    def test_code_examples_do_not_create_real_link_dependencies(self):
        (self.root / "README.md").write_text("```markdown\n[example](not-created.md)\n```\n`[inline](also-missing.md)`\n", encoding="utf-8")
        self.assertEqual(len(self.load()[0]), 8)

    def test_links_leaving_repository_are_rejected_before_target_access(self):
        (self.root / "README.md").write_text("[outside](../forbidden.md)\n", encoding="utf-8")
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Link leaves repository"):
            self.load()

    def test_invalid_namespace_and_date_are_rejected(self):
        path, data, body = self.data("technique/billboard")
        data["updated_at"] = "2026-02-30"
        self.write(path, data, body)
        with self.assertRaisesRegex(knowledge.KnowledgeError, "not a 'date'"):
            self.load()
        data["updated_at"] = "2026-10-04"
        data["kind"] = "semantic"
        self.write(path, data, body)
        with self.assertRaisesRegex(knowledge.KnowledgeError, "namespace"):
            self.load()

    def test_heading_only_node_is_rejected(self):
        self.write(self.root / "knowledge/techniques/empty.md", self.node("technique/empty"), "# Empty\n\n## TODO")
        with self.assertRaisesRegex(knowledge.KnowledgeError, "Empty knowledge body"):
            self.load()


if __name__ == "__main__":
    unittest.main()
