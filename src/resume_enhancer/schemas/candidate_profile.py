from pydantic import BaseModel

class Experience(BaseModel):
    title: str
    company: str
    duration: str
    achievements: list[str]   # kept as raw bullet strings, not over-structured —
                               # we want the enhancer working from real phrasing later

class SkillCategory(BaseModel):
    category: str   # e.g. "Languages", "Cloud and Platforms", "Data and Messaging"
    skills: list[str]

class CandidateProfile(BaseModel):
    name: str
    total_years_experience: int
    skills: list[SkillCategory]
    experiences: list[Experience]
    certifications: list[str]
    education: list[str]
    summary: str