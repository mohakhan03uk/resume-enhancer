from openai import OpenAI
from langsmith.wrappers import wrap_openai
from resume_enhancer.config import Config

_raw_client = OpenAI(api_key=Config.OPENAI_API_KEY)

# wrap_openai instruments every .chat.completions.create/.parse call automatically —
# no changes needed in any agent file. LANGSMITH_TRACING/LANGSMITH_API_KEY/LANGSMITH_PROJECT
# are read directly from the environment by the langsmith SDK itself.
client = wrap_openai(_raw_client) if Config.LANGSMITH_TRACING else _raw_client