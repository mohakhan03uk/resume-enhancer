import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PARSER_MODEL = "gpt-4o-mini"
    JD_ANALYZER_MODEL = "gpt-4o-mini"
    GAP_ANALYZER_MODEL = "gpt-4o-mini"
    ENHANCER_MODEL = "gpt-4o-mini"   # separate settings per agent on purpose —
                                      # lets you upgrade just the enhancer to a
                                      # stronger model later without touching the rest

    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not found — check your .env file")