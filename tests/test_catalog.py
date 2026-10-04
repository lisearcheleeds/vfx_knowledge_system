"""Reusable catalog and project binding boundaries; no engine execution."""

from collections import Counter
import json
from pathlib import Path
import unittest

from tools import knowledge


REPOSITORY = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nodes, cls.config = knowledge.load_repository(REPOSITORY)
        cls.bindings = json.loads((REPOSITORY / "projects/dungeon-inn/BINDINGS.json").read_text(encoding="utf-8"))["bindings"]

    def resolve(self, selected):
        return knowledge.resolve_dependencies(self.nodes, self.config, {
            "selected_nodes": selected, "engine": None, "conditional_decisions": [],
        })

    def test_common_nodes_have_no_project_ids_or_project_document_dependencies(self):
        for node_id, node in self.nodes.items():
            self.assertNotIn("dungeon-inn", node_id)
            self.assertNotIn("DungeonInn", node.body)
            self.assertNotRegex(node.body, r"(?:SkillId|ActorEffectId|ItemId)\s*\d+")
            self.assertNotRegex(node.body, r"\]\([^)]*projects/")
            self.assertNotIn("projects", node.path.relative_to(REPOSITORY).parts)

    def test_grain_consumption_can_be_reused_without_adopting_health_or_attack_states(self):
        selected = ["recipe/grain-consumption"]
        result = self.resolve(selected)
        required = set(result["required_nodes"])
        self.assertIn("technique/particle-emission", required)
        self.assertIn("technique/billboard", required)
        self.assertNotIn("recipe/food-health-restoration", required)
        self.assertNotIn("recipe/meal-vitality", required)
        self.assertFalse(result["unresolved_conditions"])
        # An independent adopter can choose a different actual response.
        healing = self.resolve(selected + ["recipe/food-health-restoration"])
        self.assertIn("recipe/food-health-restoration", healing["required_nodes"])
        self.assertIn("technique/orbit-glyphs", healing["required_nodes"])

    def test_project_bindings_cover_supplied_targets_and_all_references_exist(self):
        self.assertEqual(Counter(b["category"] for b in self.bindings), {
            "weapons": 16, "skills": 15, "states": 14, "items": 16,
        })
        keys = [(b["category"], b["key"]) for b in self.bindings]
        self.assertEqual(len(keys), len(set(keys)))
        for binding in self.bindings:
            if "adopted_selection" in binding:
                path = (REPOSITORY / "projects/dungeon-inn" / binding["adopted_selection"]["path"]).resolve()
                self.assertTrue(path.is_relative_to(REPOSITORY))
                selection = knowledge.load_yaml(path.read_text(encoding="utf-8"))
                knowledge.validate_schema(knowledge.schema_validator(REPOSITORY, "selection.schema.json"), selection, str(path))
                result = knowledge.resolve_dependencies(self.nodes, self.config, selection)
            else:
                result = self.resolve(binding["recommended_recipes"])
            self.assertFalse(result["unresolved_conditions"])
            for _, target, _, _ in binding["visual_adjustments"]["layers"]:
                self.assertIn(target, self.nodes)
        # Same appearance category can map to different gameplay states.
        by_item = {b["key"]: b for b in self.bindings if b["category"] == "items"}
        state_for_item = {
            "2001": "periodic-health-restoration", "2002": "enhanced-health-restoration",
            "2003": "premium-restoration-burst", "2004": "periodic-mana-restoration",
            "2101": "food-health-restoration", "2102": "food-health-restoration",
            "2103": "food-health-restoration", "2104": "food-health-restoration",
            "2105": "food-health-restoration", "2106": "food-health-restoration",
            "2107": "restoration-and-vitality", "2108": "restoration-and-vitality",
            "2109": "restoration-and-vitality", "2110": "food-health-restoration",
            "2111": "food-health-restoration", "2112": "restoration-and-vitality",
        }
        for item_id, state in state_for_item.items():
            self.assertEqual(by_item[item_id]["recommended_recipes"][1], "recipe/" + state)
        self.assertEqual(by_item["2110"]["recommended_recipes"][0], by_item["2112"]["recommended_recipes"][0])
        self.assertNotEqual(by_item["2110"]["recommended_recipes"][1], by_item["2112"]["recommended_recipes"][1])

    def test_latest_fireball_adoption_keeps_baseline_out_of_flight_dependencies(self):
        binding = next(b for b in self.bindings if b["category"] == "skills" and b["key"] == "103")
        self.assertEqual(binding["recommended_recipes"], [])
        self.assertEqual(binding["adopted_selection"]["scope"], "flight-preview")
        project = REPOSITORY / "projects/dungeon-inn"
        selection = knowledge.load_yaml((project / binding["adopted_selection"]["path"]).read_text(encoding="utf-8"))
        required = set(knowledge.resolve_dependencies(self.nodes, self.config, selection)["required_nodes"])
        self.assertTrue({"technique/surface-density-core", "technique/folded-axial-billboard"}.issubset(required))
        self.assertTrue({"recipe/volumetric-fireball", "technique/volume-density", "technique/directional-flow-surface", "technique/history-ribbon", "technique/surface-sigil"}.isdisjoint(required))
        baseline = binding["quality_baseline"]
        historical = knowledge.load_yaml((project / baseline["selection"]).read_text(encoding="utf-8"))
        historical_required = set(knowledge.resolve_dependencies(self.nodes, self.config, historical)["required_nodes"])
        self.assertTrue({"technique/volume-density", "technique/directional-flow-surface", "technique/history-ribbon"}.issubset(historical_required))
        active_layers = {layer[0]: layer[1] for layer in binding["visual_adjustments"]["layers"]}
        self.assertEqual(active_layers["core"], "technique/surface-density-core")
        self.assertEqual(active_layers["release"], "technique/volume-density")
        self.assertEqual(active_layers["explosion-shell"], "technique/volume-density")
        self.assertTrue({"flame-shell", "tail", "smoke-wake", "embers", "footprint"}.isdisjoint(active_layers))
        self.assertIn("flame-shell", {layer[0] for layer in baseline["visual_adjustments"]["layers"]})

    def test_primary_attack_recipes_resolve_shared_techniques_without_candidates(self):
        fireball = set(self.resolve(["recipe/volumetric-fireball"])["required_nodes"])
        self.assertTrue({"technique/volume-density", "technique/directional-flow-surface", "technique/history-ribbon", "resource/periodic-density-noise"}.issubset(fireball))
        self.assertNotIn("technique/mesh-core", fireball)
        sword = set(self.resolve(["recipe/weapon-sword"])["required_nodes"])
        axe = set(self.resolve(["recipe/weapon-axe"])["required_nodes"])
        self.assertIn("technique/arc-sweep", sword & axe)
        self.assertIn("recipe/impact-cut", sword & axe)
        weakening = set(self.resolve(["recipe/weakening-thrust"])["required_nodes"])
        self.assertNotIn("recipe/attack-reduction", weakening)
        self.assertNotIn("recipe/strong-attack-reduction", weakening)
        self.assertFalse(any(node.startswith("adapter/") for node in fireball | sword | axe))


if __name__ == "__main__":
    unittest.main()
