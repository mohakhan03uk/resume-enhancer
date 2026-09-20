from resume_enhancer.llm_client import client
from resume_enhancer.config import Config
from resume_enhancer.schemas.candidate_profile import CandidateProfile

PARSER_POLICY = """You extract structured candidate information from resume text.

Rules:
- Only extract information EXPLICITLY present in the resume text. Never infer, assume,
  or add skills/experience not stated.
- total_years_experience should be your best estimate from the dates given, not invented
  if genuinely unclear — use 0 if you cannot determine it.
- achievements should be extracted close to the original wording, not rewritten or
  embellished at this stage — this is extraction, not enhancement.
- For skills: if the resume already groups skills under headings (e.g. "Languages:",
  "Cloud and Platforms:"), preserve those exact category names. If skills appear
  ungrouped, infer reasonable, standard categories (e.g. "Languages", "Cloud",
  "Frameworks") — but never invent a skill that isn't listed, only categorize
  what's actually there.
"""

def parse_resume(resume_text: str) -> CandidateProfile:
    response = client.beta.chat.completions.parse(
        model=Config.PARSER_MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": PARSER_POLICY},
            {"role": "user", "content": f"Resume:\n{resume_text}"},
        ],
        response_format=CandidateProfile,
    )
    return response.choices[0].message.parsed