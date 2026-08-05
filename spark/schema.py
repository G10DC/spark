from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class LensResult(BaseModel):
    lens_name: str
    description: str
    insights: List[str] = Field(default_factory=list)

class SkillSynergy(BaseModel):
    skill_name: str
    original_purpose: str
    applied_innovation: str

class SparkConcept(BaseModel):
    title: str
    description: str
    target_domain: Optional[str] = None
    tags: List[str] = Field(default_factory=list)

class IdeationBlueprint(BaseModel):
    concept: SparkConcept
    vision: str
    breakthrough_features: List[Dict[str, str]] = Field(default_factory=list)
    skill_synergies: List[SkillSynergy] = Field(default_factory=list)
    architecture_mermaid: str
    poc_snippet: Optional[str] = None
