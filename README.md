# Resume Enhancer

A multi-agent tool that compares a candidate's resume against a specific job description,
finds real matches and real gaps, and produces a tailored, rewritten resume — without ever
inventing skills or experience the candidate doesn't actually have.

## What it does

You give it two things:
1. A resume (currently loaded from a local file)
2. A job description (pasted text)

It runs four AI agents in sequence, each with one clear job:

1. **Parser Agent** — reads the resume and turns it into structured data: skills (grouped
   by category), work experience, certifications, education.
2. **JD Analyzer Agent** — reads the job description and extracts what it actually asks
   for: required skills, preferred skills, responsibilities, education requirements.
3. **Gap Analyzer Agent** — compares the two. For every skill the job asks for, it checks
   whether the resume actually proves the candidate has it, and points to the exact line
   of the resume that proves it. If there's no real proof, the skill goes in a "missing"
   list — never guessed at.
4. **Enhancer Agent** — rewrites the resume's bullet points to speak more directly to the
   job description, using clearer and more natural language. It is only allowed to
   rephrase what's already true. It is never allowed to add a skill that Gap Analyzer
   marked as missing.

The output is a rewritten resume, plus an honest note explaining exactly what the
candidate doesn't yet have evidence for — so nothing is hidden or oversold.

## Why it's built this way

The most important design decision in this whole project is simple: **a tool that helps
you improve your resume must never let you accidentally lie on it.**

Every stage of this pipeline is built to be checked, not just trusted:

- The Gap Analyzer must point to real text as evidence for every match it claims.
- After the Enhancer runs, the code independently checks the final output for any of the
  "missing" skills — if even one slipped through, it gets flagged loudly before you'd ever
  see it as a finished resume.
- The Enhancer is also checked to make sure it didn't quietly skip any job from the
  original resume.

None of this is optional or a "nice to have." It's the actual point of the project.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-key-here
```

Put your resume in `data/sample_resumes/` and your target job description in
`data/sample_jds/target_jd.txt`, then run:

```powershell
python main.py
```

## What's proven to work

This isn't a first draft that "looks right" — every part of it was tested against a real
resume and a real job posting, and every bug that came up was tracked down and fixed:

- The skill list is grouped into real categories, matching how the original resume
  organizes them, instead of one long undifferentiated list.
- The job description analyzer was caught inventing a skill ("Docker") that wasn't
  actually in the posting — fixed, and a permanent check now runs on every output to catch
  this automatically going forward.
- Early on, results changed noticeably every time the pipeline ran on the exact same
  inputs. This was tracked down to the AI model's default randomness setting, which is now
  turned off for every agent — results are now stable and repeatable.
- The Enhancer agent was silently dropping most of the candidate's work history from its
  output on longer resumes. This was fixed by having it process one job at a time instead
  of trying to rewrite the whole resume in one go.

## What's left / possible next steps

- Currently reads the resume and job description from local files — a real "portal" would
  need file upload and a proper user interface.
- The rewritten resume is only printed as structured data right now, not formatted into an
  actual downloadable document.
- Could be extended to score how well the candidate matches multiple job descriptions at
  once, not just one.