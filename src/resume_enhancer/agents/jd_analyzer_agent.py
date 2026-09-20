import unicodedata
import re

from resume_enhancer.llm_client import client
from resume_enhancer.config import Config
from resume_enhancer.schemas.job_requirements import JobRequirements

JD_ANALYZER_POLICY = """You extract structured requirements from a job description.

Rules:
- Distinguish REQUIRED skills (stated with strong/mandatory language: "strong experience",
  "must have", listed as core requirements) from PREFERRED (softer language: "familiarity
  with", "exposure to", "nice to have"). If the JD doesn't clearly separate them, use the
  language strength of each item as your signal — do not default everything to required.
- Extract skills GRANULARLY — if the JD lists "data structures, algorithms, concurrency,
  memory management" as one sentence, extract each as a SEPARATE skill, not a summary
  category. Do not compress a specific list into a vaguer restatement.
- education_requirement: the exact stated degree requirement, or null if none stated.
- NEVER add a skill/technology that is not literally present in the JD text, even if it's
  a common companion technology for this type of role. If you are not 100% certain a term
  appears in the source text, leave it out.
"""

def analyze_jd(jd_text: str) -> JobRequirements:
    response = client.beta.chat.completions.parse(
        model=Config.JD_ANALYZER_MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": JD_ANALYZER_POLICY},
            {"role": "user", "content": f"Job Description:\n{jd_text}"},
        ],
        response_format=JobRequirements,
    )
    return response.choices[0].message.parsed

def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
    return text.lower()

def verify_no_fabrication(requirements: JobRequirements, jd_text: str, min_word_overlap: float = 0.6) -> list[str]:
    jd_norm = normalize_text(jd_text)
    jd_words = set(re.findall(r'\w+', jd_norm))

    unverified = []
    all_skills = requirements.required_skills + requirements.preferred_skills
    for skill in all_skills:
        skill_words = set(re.findall(r'\w+', normalize_text(skill)))
        if not skill_words:
            continue
        overlap = len(skill_words & jd_words) / len(skill_words)
        if overlap < min_word_overlap:
            unverified.append(skill)
    return unverified

