import os
import sys
import json
import requests
from typing import Dict, Any
from spark.lenses import IdeationLenses
from spark.skills_matrix import SkillsMatrix

GEMMA_WORKER_DIR = r"C:\Users\GdC\.unsloth\studio"

class SparkEngine:
    def __init__(self, studio_url: str = "http://127.0.0.1:8888"):
        self.studio_url = studio_url
        self.gemma_worker = None
        self._init_local_llm()

    def _init_local_llm(self):
        if GEMMA_WORKER_DIR not in sys.path:
            sys.path.append(GEMMA_WORKER_DIR)
        try:
            import gemma_worker
            self.gemma_worker = gemma_worker
        except Exception:
            self.gemma_worker = None

    def ideate(self, concept: str) -> str:
        prompt = f"Idea Concept: {concept}"
        system_prompt = """Sei SPARK, un motore di ideazione creativa, pensiero laterale e sintesi multidisciplinare per software ed AI.
Dato un progetto o un'idea iniziale, applica il framework 4-Lens (Deconstruction, SCAMPER/TRIZ, Friction-to-Feature Inversion, Experience Shift) per generare 3 miglioramenti ad altissimo impatto ("WOW Factor").

Rispondi in formato Markdown strutturato con:
1. Visione Creativa & WOW Factor
2. 3 Funzionalita Breakthrough (Friction -> Feature)
3. Sinergia con le Skill (Sieve, Scribe, Artisan, Keel)
4. Bozza Architetturale (Diagramma Mermaid)
"""
        if self.gemma_worker:
            try:
                return self.gemma_worker.query_gemma_local(prompt, system_prompt=system_prompt)
            except Exception:
                pass

        # High quality fallback blueprint
        return self._generate_rule_blueprint(concept)

    def _generate_rule_blueprint(self, concept: str) -> str:
        decon = IdeationLenses.deconstruct(concept)
        frictions = IdeationLenses.friction_to_feature_inversion(concept)
        synergies = SkillsMatrix.get_skill_synergies()

        features_md = "\n".join([f"{i+1}. **{f['breakthrough']}**: Resets '{f['friction']}'." for i, f in enumerate(frictions)])
        synergies_md = "\n".join([f"- **`{k}`**: {v}" for k, v in synergies.items()])

        return f"""# SPARK IDEATION BLUEPRINT: {concept}

## 1. Visione Creativa & WOW Factor
Transform '{concept}' from a passive utility into an autonomous, proactive, state-of-the-art ecosystem.

## 2. Breakthrough Features (Friction -> Feature Inversion)
{features_md}

## 3. Antigravity Skill Synergy Matrix
{synergies_md}

## 4. Conceptual Architecture
```mermaid
graph TD
    Input["Concept / Raw Data"] --> Sieve["sieve Data Pipeline"]
    Sieve --> Spark["Gemma 4 12B Spark Engine"]
    Spark --> UI["artisan Glassmorphic UI Dashboard"]
```
"""
