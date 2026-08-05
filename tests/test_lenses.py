import unittest
from spark.lenses import IdeationLenses
from spark.skills_matrix import SkillsMatrix

class TestIdeationLenses(unittest.TestCase):
    def test_deconstruct(self):
        decon = IdeationLenses.deconstruct("Scraper")
        self.assertIn("ingestion", decon)
        self.assertIn("processing", decon)
        self.assertIn("interface", decon)

    def test_friction_inversion(self):
        frictions = IdeationLenses.friction_to_feature_inversion("Scraper")
        self.assertTrue(len(frictions) >= 3)

    def test_skills_matrix(self):
        synergies = SkillsMatrix.get_skill_synergies()
        self.assertIn("sieve", synergies)
        self.assertIn("scribe", synergies)
        self.assertIn("artisan", synergies)

if __name__ == "__main__":
    unittest.main()
