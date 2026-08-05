from typing import Dict, Any, List

class IdeationLenses:
    """
    Implements the 4-Lens Lateral Thinking Framework:
    1. Atomic Deconstruction
    2. SCAMPER / TRIZ Lateral Shift
    3. Aesthetic & Experience Lift
    4. Friction-to-Feature Inversion
    """

    @staticmethod
    def deconstruct(concept: str) -> Dict[str, str]:
        return {
            "ingestion": f"Raw data and inputs for {concept}",
            "processing": f"Processing & transformation engine for {concept}",
            "persistence": f"Storage, caching, and state management for {concept}",
            "interface": f"User interaction and visual experience for {concept}",
            "security": f"Trust, privacy, and execution boundaries for {concept}"
        }

    @staticmethod
    def friction_to_feature_inversion(concept: str) -> List[Dict[str, str]]:
        return [
            {
                "friction": "Manual configuration or explicit user triggers",
                "breakthrough": "Zero-Click Proactive Background Automation"
            },
            {
                "friction": "Static tabular data presentation",
                "breakthrough": "Interactive Glassmorphic Visual Canvas with Real-Time Filtering"
            },
            {
                "friction": "Cloud API latency and recurring token costs",
                "breakthrough": "Off-Grid Local LLM Processing via Gemma 4 12B"
            }
        ]
