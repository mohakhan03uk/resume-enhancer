from pathlib import Path
from resume_enhancer.agents.parser_agent import parse_resume
from resume_enhancer.agents.jd_analyzer_agent import analyze_jd, verify_no_fabrication
from resume_enhancer.agents.gap_analyzer_agent import analyze_gap
from resume_enhancer.agents.enhancer_agent import enhance_resume, verify_no_missing_skills_leaked, verify_all_experiences_present#

resume_path = Path("data/sample_resumes/Mohammad_Imran_Khan_resume.md")
resume_text = resume_path.read_text(encoding="utf-8")
profile = parse_resume(resume_text)
print("=== Candidate Profile ===")
print(profile.model_dump_json(indent=2))

jd_path = Path("data/sample_jds/target_jd.txt")
jd_text = jd_path.read_text(encoding="utf-8")

requirements = analyze_jd(jd_text)
flagged = verify_no_fabrication(requirements, jd_text)
if flagged:
    print(f"  UNVERIFIED (not found in source JD): {flagged}")

print("\n=== Job Requirements ===")
print(requirements.model_dump_json(indent=2))


gap = analyze_gap(profile, requirements)

print("\n=== Gap Analysis ===")

print(gap.model_dump_json(indent=2))




# ... existing profile, requirements, gap code ...

enhanced = enhance_resume(profile, requirements, gap)
print("\n=== Enhanced Resume ===")
print(enhanced.model_dump_json(indent=2))

leaked = verify_no_missing_skills_leaked(enhanced, gap)
if leaked:
    print(f"\n🚨 CRITICAL: missing skills leaked into enhanced output: {leaked}")
else:
    print("\n✅ No missing skills leaked into enhanced output.")

missing_roles = verify_all_experiences_present(enhanced, profile)
if missing_roles:
    print(f"\n🚨 EXPERIENCES DROPPED: {missing_roles}")