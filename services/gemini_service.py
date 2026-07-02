import os
import google.generativeai as genai

try:
    from config import GEMINI_API_KEY
except ImportError:
    GEMINI_API_KEY = None

api_key = os.getenv("GEMINI_API_KEY") or GEMINI_API_KEY

if not api_key:
    raise ValueError(
        "Gemini API key not found. Set GEMINI_API_KEY in Streamlit Secrets or config.py."
    )

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

