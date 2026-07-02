import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, continue without it

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

APP_NAME = "ASTRA"
FULL_NAME = "Artificial Student Tracking and Research Assistant"
VERSION = "1.0"