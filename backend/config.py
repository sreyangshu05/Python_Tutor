import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyCefaJp40KCLNXCsIilcwAfI82E53Yxcsg")
