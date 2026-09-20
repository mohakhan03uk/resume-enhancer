from pathlib import Path
from resume_enhancer.agents.parser_agent import parse_resume
from resume_enhancer.agents.jd_analyzer_agent import analyze_jd

resume_path = Path("data/sample_resumes/Mohammad_Imran_Khan_resume.md")
resume_text = resume_path.read_text(encoding="utf-8")
profile = parse_resume(resume_text)
print("=== Candidate Profile ===")
print(profile.model_dump_json(indent=2))

jd_path = Path("data/sample_jds/target_jd.txt")
jd_text = jd_path.read_text(encoding="utf-8")
requirements = analyze_jd(jd_text)
print("\n=== Job Requirements ===")
print(requirements.model_dump_json(indent=2))