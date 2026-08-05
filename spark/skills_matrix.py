from typing import Dict, Any

class SkillsMatrix:
    """
    Synergy matrix linking project concepts to Antigravity ecosystem skills.
    """
    
    SKILLS_MAP = {
        "sieve": "Data Pipeline ETL (Raw -> Staged -> Curated) & Idempotent Persistence",
        "scribe": "Multimodal Vision & OCR Loop (Preprocess -> Extract -> Validate -> Repair)",
        "artisan": "Pedagogical UI/UX & Glassmorphic Interactive Design System",
        "keel": "Instruction/Data Boundaries, Audit Trail & Structured Concurrency",
        "warden": "Sanitization of Untrusted Inputs & Anti-Prompt-Injection Safeguards",
        "beacon": "Automated Release Notes & Daily Executive Markdown Digest"
    }

    @classmethod
    def get_skill_synergies(cls) -> Dict[str, str]:
        return cls.SKILLS_MAP
