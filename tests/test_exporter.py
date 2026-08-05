import unittest
from spark.exporter import BlueprintExporter

class TestBlueprintExporter(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "title": "Smart Scraper",
            "vision": "Autonomous deal tracker",
            "features": [
                {"title": "Zero-Click Search", "desc": "Proactive search"},
                {"title": "Glassmorphic UI", "desc": "Modern dashboard"}
            ],
            "synergies": {"sieve": "ETL Pipeline", "scribe": "OCR"},
            "mermaid": "graph TD\n  A --> B"
        }

    def test_to_markdown(self):
        md = BlueprintExporter.to_markdown(self.sample_data)
        self.assertIn("Smart Scraper", md)
        self.assertIn("SPARK IDEATION BLUEPRINT", md)

    def test_to_json(self):
        js = BlueprintExporter.to_json(self.sample_data)
        self.assertIn("Smart Scraper", js)

    def test_to_html(self):
        html = BlueprintExporter.to_html(self.sample_data)
        self.assertIn("Smart Scraper", html)
        self.assertIn("<html", html)

if __name__ == "__main__":
    unittest.main()
