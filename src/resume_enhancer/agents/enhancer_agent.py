from resume_enhancer.llm_client import client
from resume_enhancer.config import Config
from resume_enhancer.schemas.candidate_profile import CandidateProfile
from resume_enhancer.schemas.job_requirements import JobRequirements
from resume_enhancer.schemas.gap_analysis import GapAnalysis
from resume_enhancer.schemas.enhanced_resume import EnhancedResume

ENHANCER_POLICY = """You rewrite resume content to better align with a target job description.

ABSOLUTE RULES — violating these makes the output actively harmful, not just lower quality:
- NEVER claim, imply, or hint that the candidate has a skill listed in missing_required or
  missing_preferred. Do not use those skill names anywhere in enhanced bullets or the summary,
  even indirectly ("familiar with algorithms" when algorithms is missing is a violation).
- Every enhanced_achievements bullet's `grounded_in` field MUST be a real, exact or
  near-exact excerpt from the candidate's ACTUAL original achievement text. If you cannot
  point to real original text supporting a rewrite, do not include that rewrite.
- Rewriting is REPHRASING for clarity, relevance, and impact — using terminology closer to
  the JD's language where it genuinely describes the same real work (e.g. resume says
  "thread synchronization", JD says "concurrency" — rephrasing to mention concurrency is
  fine IF the underlying work is the same). It is NEVER adding new claims, new metrics, or
  new scope not present in the original.
- skills_to_highlight must come ONLY from matched_required, matched_preferred, and
  partially_evidenced — never from missing_required or missing_preferred.
- honest_gaps_note must clearly and specifically name what's missing for this role, in
  plain language the candidate can act on (e.g. "no direct evidence of data structures/
  algorithms — consider adding a project or coursework example if you have one").
- You MUST include an entry in experiences for EVERY SINGLE experience in the candidate's
  original profile — do not omit, skip, or summarize away any role, even if it seems less
  relevant to this specific JD. If a role has no bullets worth enhancing for this JD, still
  include it with its original achievements lightly rephrased for clarity, never dropped.
"""

def enhance_resume(
    profile: CandidateProfile,
    requirements: JobRequirements,
    gap: GapAnalysis,
) -> EnhancedResume:
    response = client.beta.chat.completions.parse(
        model=Config.ENHANCER_MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": ENHANCER_POLICY},
            {"role": "user", "content": (
                f"Candidate Profile:\n{profile.model_dump_json(indent=2)}\n\n"
                f"Job Requirements:\n{requirements.model_dump_json(indent=2)}\n\n"
                f"Gap Analysis:\n{gap.model_dump_json(indent=2)}"
            )},
        ],
        response_format=EnhancedResume,
    )
    return response.choices[0].message.parsed


def verify_no_missing_skills_leaked(enhanced: EnhancedResume, gap: GapAnalysis) -> list[str]:
    """Checks that no missing skill name appears anywhere in the enhanced output —
    the highest-severity check in this whole pipeline, since a violation here means
    the tool generated a claim that could get someone caught misrepresenting themselves."""
    forbidden = set(s.lower() for s in gap.missing_required + gap.missing_preferred)

    full_text = enhanced.tailored_summary.lower()
    full_text += " " + " ".join(s.lower() for s in enhanced.skills_to_highlight)
    for exp in enhanced.experiences:
        for bullet in exp.enhanced_achievements:
            full_text += " " + bullet.enhanced.lower()

    return [skill for skill in forbidden if skill in full_text]

def verify_all_experiences_present(enhanced: EnhancedResume, profile: CandidateProfile) -> list[str]:
    original_titles = {(e.title, e.duration) for e in profile.experiences}
    enhanced_titles = {(e.title, e.duration) for e in enhanced.experiences}
    missing = original_titles - enhanced_titles
    return [f"{title} ({duration})" for title, duration in missing]