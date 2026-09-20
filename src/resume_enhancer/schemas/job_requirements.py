from pydantic import BaseModel

class JobRequirements(BaseModel):
    job_title: str
    company: str | None
    seniority_level: str          # e.g. "Senior", "Lead", "Mid-level" — as stated or clearly implied
    required_skills: list[str]
    preferred_skills: list[str]   # "nice to have" / "bonus" — kept SEPARATE from required,
                                   # since conflating them would corrupt gap analysis later
    education_requirement: str | None
    key_responsibilities: list[str]
    years_experience_required: int | None