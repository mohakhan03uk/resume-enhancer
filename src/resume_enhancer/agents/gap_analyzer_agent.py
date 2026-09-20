
from resume_enhancer.llm_client import client
from resume_enhancer.config import Config
from resume_enhancer.schemas.candidate_profile import CandidateProfile
from resume_enhancer.schemas.job_requirements import JobRequirements
from resume_enhancer.schemas.gap_analysis import GapAnalysis

GAP_ANALYZER_POLICY = """You compare a candidate's profile against job requirements to
identify matches and gaps.

Rules:
- A skill counts as MATCHED only if it is either explicitly listed in the candidate's
  skills, OR clearly demonstrated by specific achievement text. Every match MUST include
  the exact evidence (quoted or closely paraphrased from the actual profile) that supports it.
- Use "partially_evidenced" for skills that aren't explicitly listed as a skill, but are
  reasonably inferable from what an achievement describes (e.g. a JD requiring "concurrency"
  when the resume describes "thread synchronization" work) — do not silently upgrade these
  to full matches; the distinction matters for how confidently this gets presented later.
- If you cannot point to real evidence for a skill, it goes in missing_required or
  missing_preferred — never guess or give benefit of the doubt without evidence.
- overall_fit_summary should be honest and specific, not generically positive.
"""

def reconcile_gap_analysis(gap: GapAnalysis) -> GapAnalysis:
    partial_skills = {m.skill for m in gap.partially_evidenced}
    gap.missing_required = [s for s in gap.missing_required if s not in partial_skills]
    gap.missing_preferred = [s for s in gap.missing_preferred if s not in partial_skills]
    return gap

def analyze_gap(profile: CandidateProfile, requirements: JobRequirements) -> GapAnalysis:
    response = client.beta.chat.completions.parse(
        model=Config.GAP_ANALYZER_MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": GAP_ANALYZER_POLICY},
            {"role": "user", "content": (
                f"Candidate Profile:\n{profile.model_dump_json(indent=2)}\n\n"
                f"Job Requirements:\n{requirements.model_dump_json(indent=2)}"
            )},
        ],
        response_format=GapAnalysis,
    )
    gap = response.choices[0].message.parsed
    return reconcile_gap_analysis(gap)   # apply the fix now, not just discuss it