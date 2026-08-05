import sys
import json
import os
from pathlib import Path

# Add project root to path
sys.path.append(r"C:\Users\GdC\.unsloth\studio")

try:
    import gemma_worker
    HAS_LOCAL_LLM = True
except Exception:
    HAS_LOCAL_LLM = False

SPARK_PROMPT = """You are SPARK, a creative ideation, lateral thinking, and multidisciplinary synthesis engine for software and AI.
Given an initial project idea or concept, apply the 4-Lens Framework (Deconstruction, SCAMPER/TRIZ, Friction-to-Feature Inversion, Experience Shift) to generate 3 high-impact breakthrough features ("WOW Factor").

Respond in structured Markdown with:
1. Creative Vision & WOW Factor
2. 3 Breakthrough Features (Friction -> Feature Inversion)
3. Skill Synergy Matrix (Sieve, Scribe, Artisan, Keel, Warden)
4. Conceptual Architecture (Mermaid Diagram)
"""

def generate_spark_ideas(concept: str) -> str:
    print(f"[spark] Generating creative ideas and enhancements for: '{concept}'...")
    
    if HAS_LOCAL_LLM:
        try:
            return gemma_worker.query_gemma_local(
                prompt=f"Concept Idea: {concept}",
                system_prompt=SPARK_PROMPT
            )
        except Exception as e:
            print(f"[spark LLM Warning]: {e}")

    # Standalone heuristic fallback
    return f"""# SPARK IDEATION BLUEPRINT: {concept}

## 1. Creative Vision & WOW Factor
Evolve '{concept}' from a passive utility into a proactive, automated, state-of-the-art ecosystem.

## 2. Breakthrough Features (Friction -> Feature Inversion)
1. Zero-Click Proactive Automation: Anticipates user needs via background triggers and smart notifications.
2. Dynamic Glassmorphic Dashboard: High-performance visual UI with micro-interactions, live search, and query-ready data.
3. Off-Grid Gemma 4 12B Integration: Zero-cost categorization, enrichment, and deep local analysis.

## 3. Antigravity Skill Synergy Matrix
- sieve: Idempotent 3-layer ETL data pipeline (Raw -> Staged -> Curated) with historical snapshots.
- scribe: Multimodal vision & OCR extraction loop (Extract -> Validate -> Repair).
- artisan: Advanced design system & pedagogical visual layout.

## 4. Conceptual Architecture
```mermaid
graph TD
    Input["Concept / Raw Data"] --> Sieve["sieve Pipeline (Ingest)"]
    Sieve --> LLM["Gemma 4 12B (Local Spark Engine)"]
    LLM --> UI["artisan Dashboard & Interactive Canvas"]
```
"""

if __name__ == "__main__":
    idea = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Generic Project"
    print(generate_spark_ideas(idea))
