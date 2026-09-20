from pydantic import BaseModel

class SkillMatch(BaseModel):
    skill: str
    evidence: str          # the SPECIFIC resume text that supports this match — same
                            # citation discipline as GroundedAnswer from Layer 5

class GapAnalysis(BaseModel):
    matched_required: list[SkillMatch]
    matched_preferred: list[SkillMatch]
    missing_required: list[str]     # JD requires it, nothing in resume supports it
    missing_preferred: list[str]
    partially_evidenced: list[SkillMatch]  # not explicitly listed as a skill, but
                                            # reasonably inferable from achievement text
    overall_fit_summary: str
