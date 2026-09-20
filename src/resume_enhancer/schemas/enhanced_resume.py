from pydantic import BaseModel

class EnhancedBullet(BaseModel):
    original: str
    enhanced: str
    grounded_in: str   # the exact original achievement text this rewrite is based on —
                        # same discipline as GapAnalysis.SkillMatch.evidence

class EnhancedExperience(BaseModel):
    title: str
    company: str
    duration: str
    enhanced_achievements: list[EnhancedBullet]

class EnhancedResume(BaseModel):
    tailored_summary: str
    experiences: list[EnhancedExperience]
    skills_to_highlight: list[str]   # ONLY from matched_required + matched_preferred +
                                      # partially_evidenced — never from missing_*
    honest_gaps_note: str            # explicit, upfront: what this candidate does NOT
                                      # evidence for this role — never hidden or glossed over