from typing import Dict, Any

class SkillsMatrix:
    """
    Synergy matrix mapping project concepts to all 33 Antigravity ecosystem skills.
    """
    
    SKILLS_MAP = {
        "anchor": "Contract-first API spec & Pydantic payload validators",
        "antigravity-guide": "AGY Ecosystem documentation & sitemap engine",
        "archaeologist": "Git history, churn & debt hotspot analyzer",
        "artisan": "Pedagogical UI/UX layout & visual hierarchy design engine",
        "artisan-chat": "Standardized AI agent chat tone, styling & footnotes",
        "atlas": "Multi-repository & monorepo dependency orchestrator",
        "beacon": "Automated release notes & changelog generator",
        "bonsai": "Minimal necessary code bias & stdlib-first enforcement",
        "cartographer": "Visual codebase architecture & Mermaid diagram generator",
        "chisel": "Token usage minimization & concise prompt optimizer",
        "chronicle": "Trajectory compression & checkpoint memory manager",
        "forge": "Synthetic test & mutation coverage generator",
        "git-researcher": "GitHub repository discovery & architecture analysis pipeline",
        "hydra": "Hierarchical map-reduce codebase summarizer",
        "keel": "Instruction/data trust boundary & step dispatcher",
        "lookout": "Dependency security & license compliance audit sentinel",
        "loom": "Brainstorm-Spec-Plan-Build-Verify superpower phase spine",
        "mirror": "Multi-perspective pre-commit code reviewer (4 lenses)",
        "prism": "Multi-provider LLM routing & load balancer",
        "prism-search": "Hybrid AST + Vector RAG codebase search indexer",
        "pulse": "Project health & quality composite score synthesizer",
        "schema-lineage": "Database migration & column data lineage mapper",
        "scribe": "Multimodal vision & OCR extraction loop (extract-validate-repair)",
        "sentinel": "Runtime guard, prompt injection filter & egress firewall",
        "shipwright": "Automated repository init, security scan & clean commits",
        "siege": "Authorized security assessment & CTF pentest audit trail",
        "sieve": "Idempotent ETL data pipeline (Raw -> Staged -> Curated)",
        "smith": "AST transformation & propagation engine",
        "spark": "Creative ideation, cross-domain synthesis & project evolution engine",
        "strata": "Cross-service gRPC, OpenAPI & GraphQL topology tracer",
        "tombstone": "Dead code & asset bloat reachability hunter",
        "trellis": "Bidirectional codebase reachability graph engine",
        "warden": "Sanitization of untrusted data & prompt injection firewall"
    }

    @classmethod
    def get_skill_synergies(cls) -> Dict[str, str]:
        return cls.SKILLS_MAP
