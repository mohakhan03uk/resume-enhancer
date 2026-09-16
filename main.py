from pathlib import Path
from resume_enhancer.agents.parser_agent import parse_resume

resume_path = Path("data/sample_resumes/Mohammad_Imran_Khan_resume.md")
resume_text = resume_path.read_text(encoding="utf-8")

profile = parse_resume(resume_text)
print(profile.model_dump_json(indent=2))