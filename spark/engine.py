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
        system_prompt = """You are SPARK, a creative ideation, lateral thinking, and multidisciplinary synthesis engine for software and AI.
Given an initial project idea or concept, apply the 4-Lens Framework (Deconstruction, SCAMPER/TRIZ, Friction-to-Feature Inversion, Experience Shift) to generate 3 high-impact breakthrough features ("WOW Factor").

Respond in structured Markdown with:
1. Creative Vision & WOW Factor
2. 3 Breakthrough Features (Friction -> Feature Inversion)
3. Skill Synergy Matrix (Sieve, Scribe, Artisan, Keel, Warden)
4. Conceptual Architecture (Mermaid Diagram)
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

        features_md = "\n".join([f"{i+1}. **{f['breakthrough']}**: Inverts '{f['friction']}'." for i, f in enumerate(frictions)])
        synergies_md = "\n".join([f"- **`{k}`**: {v}" for k, v in synergies.items()])

        return f"""# SPARK IDEATION BLUEPRINT: {concept}

## 1. Creative Vision & WOW Factor
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
