import json
from typing import Dict, Any
from pathlib import Path

class BlueprintExporter:
    """
    Exports Spark Ideation Blueprints into Markdown, JSON, and interactive HTML dashboards.
    """

    @staticmethod
    def to_markdown(blueprint_data: Dict[str, Any]) -> str:
        title = blueprint_data.get("title", "Project Concept")
        vision = blueprint_data.get("vision", "")
        features = blueprint_data.get("features", [])
        synergies = blueprint_data.get("synergies", {})
        mermaid = blueprint_data.get("mermaid", "")

        feat_md = "\n".join([f"{i+1}. **{f.get('title', 'Feature')}**: {f.get('desc', '')}" for i, f in enumerate(features)])
        syn_md = "\n".join([f"- **`{k}`**: {v}" for k, v in synergies.items()])

        return f"""# ⚡ SPARK IDEATION BLUEPRINT: {title}

## 💡 1. Visione Creativa & WOW Factor
{vision}

## 🚀 2. Breakthrough Features (Friction -> Feature Inversion)
{feat_md}

## 🧩 3. Antigravity Skill Synergy Matrix
{syn_md}

## 🏗️ 4. Conceptual Architecture
```mermaid
{mermaid}
```
"""

    @staticmethod
    def to_json(blueprint_data: Dict[str, Any]) -> str:
        return json.dumps(blueprint_data, ensure_ascii=False, indent=2)

    @staticmethod
    def to_html(blueprint_data: Dict[str, Any]) -> str:
        title = blueprint_data.get("title", "Project Concept")
        vision = blueprint_data.get("vision", "")
        features = blueprint_data.get("features", [])
        
        feat_html = "".join([
            f'<div class="feature-card"><h3>🚀 {f.get("title")}</h3><p>{f.get("desc")}</p></div>' 
            for f in features
        ])

        return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <title>Spark Blueprint - {title}</title>
  <style>
    body {{ background: #0f172a; color: #f8fafc; font-family: system-ui, sans-serif; padding: 2rem; }}
    h1 {{ color: #38bdf8; }}
    .container {{ max-width: 900px; margin: 0 auto; }}
    .vision {{ background: rgba(30, 41, 59, 0.7); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 2rem; }}
    .feature-card {{ background: rgba(30, 41, 59, 0.7); padding: 1.25rem; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.3); margin-bottom: 1rem; }}
    .feature-card h3 {{ margin-bottom: 0.5rem; color: #38bdf8; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>⚡ Spark Ideation Blueprint: {title}</h1>
    <div class="vision">
      <h2>💡 Visione Creativa</h2>
      <p>{vision}</p>
    </div>
    <h2>🚀 Breakthrough Features</h2>
    {feat_html}
  </div>
</body>
</html>
"""
