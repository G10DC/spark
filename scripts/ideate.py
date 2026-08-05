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

SPARK_PROMPT = """Sei SPARK, un motore di ideazione creativa, pensiero laterale e sintesi multidisciplinare per software ed AI.
Dato un progetto o un'idea iniziale, applica il framework 4-Lens (Deconstruction, SCAMPER/TRIZ, Friction-to-Feature Inversion, Experience Shift) per generare 3 miglioramenti ad altissimo impatto ("WOW Factor").

Rispondi in formato Markdown strutturato con:
1. Visione Creativa & WOW Factor
2. 3 Funzionalita Breakthrough (Friction -> Feature)
3. Sinergia con le Skill (Sieve, Scribe, Artisan, Keel)
4. Bozza Architetturale (Diagramma Mermaid)
"""

def generate_spark_ideas(concept: str) -> str:
    print(f"[spark] Generazione idee e miglioramenti per: '{concept}'...")
    
    if HAS_LOCAL_LLM:
        try:
            return gemma_worker.query_gemma_local(
                prompt=f"Punto di partenza/Idea: {concept}",
                system_prompt=SPARK_PROMPT
            )
        except Exception as e:
            print(f"[spark LLM Warning]: {e}")

    # Standalone heuristic fallback
    return f"""# SPARK IDEATION BLUEPRINT: {concept}

## 1. Visione Creativa & WOW Factor
Evolvere il concetto '{concept}' da uno strumento passivo ad un ecosistema proattivo, automatizzato ed esteticamente d'impatto.

## 2. Funzionalita Breakthrough (Friction -> Feature Inversion)
1. Automazione Proattiva Zero-Click: L'applicazione anticipa l'esigenza dell'utente tramite trigger in background e notifiche intelligenti.
2. Dashboard Dinamica Glassmorphic: Interfaccia visiva ad alte prestazioni con feedback micro-animato, filtri istantanei e visualizzazione dati query-ready.
3. Integrazione Gemma 4 12B Off-Grid: Categorizzazione, arricchimento ed analisi avanzata a costo zero su hardware locale.

## 3. Sinergia con le Skill
- sieve: Data pipeline ETL a 3 livelli (Raw -> Staged -> Curated) con storico temporale.
- scribe: Loop di estrazione multimodale (Preprocess -> Extract -> Validate -> Repair).
- artisan: Design system avanzato e layout pedagogico d'impatto.

## 4. Bozza Architetturale
```mermaid
graph TD
    Input["Idea / Raw Data"] --> Sieve["sieve Pipeline (Ingest)"]
    Sieve --> LLM["Gemma 4 12B (Local Spark Engine)"]
    LLM --> UI["artisan Dashboard & Interactive Canvas"]
```
"""

if __name__ == "__main__":
    idea = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Progetto Generico"
    print(generate_spark_ideas(idea))
