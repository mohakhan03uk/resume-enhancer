from openai import OpenAI
from resume_enhancer.config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)
