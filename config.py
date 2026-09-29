# config.py
import os
from dotenv import load_dotenv

# Force dotenv to overwrite any environment variables cached in PowerShell
load_dotenv(override=True)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma_data")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not all([GITHUB_TOKEN, OPENAI_API_KEY]):
    raise ValueError("Missing critical environment variables (GITHUB_TOKEN, OPENAI_API_KEY)")