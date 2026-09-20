from resume_enhancer.llm_client import client
from resume_enhancer.config import Config
from resume_enhancer.schemas.job_requirements import JobRequirements

JD_ANALYZER_POLICY = """You extract structured requirements from a job description.

Rules:
- Distinguish clearly between REQUIRED skills (must-have, explicitly stated as required/
  essential) and PREFERRED skills (nice-to-have, bonus, desirable). Do not merge them.
- If years of experience isn't explicitly stated, use null rather than guessing a number.
- key_responsibilities should reflect actual stated duties, not skills restated as duties.
- Only extract what's explicitly in the JD text — do not add industry-standard
  assumptions about what a role "probably" also requires.
"""

def analyze_jd(jd_text: str) -> JobRequirements:
    response = client.beta.chat.completions.parse(
        model=Config.JD_ANALYZER_MODEL,
        messages=[
            {"role": "system", "content": JD_ANALYZER_POLICY},
            {"role": "user", "content": f"Job Description:\n{jd_text}"},
        ],
        response_format=JobRequirements,
    )
    return response.choices[0].message.parsed