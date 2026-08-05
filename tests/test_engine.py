import unittest
from spark.engine import SparkEngine

class TestSparkEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SparkEngine()

    def test_ideate_output_contains_concept(self):
        concept = "Test Automated System"
        blueprint = self.engine.ideate(concept)
        self.assertIn("Test Automated System", blueprint)
        self.assertIn("SPARK IDEATION BLUEPRINT", blueprint)
        self.assertIn("mermaid", blueprint)

if __name__ == "__main__":
    unittest.main()
