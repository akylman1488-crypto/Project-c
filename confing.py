import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

class Config:
    GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")
    WORKSPACE = BASE_DIR / "workspace"
    MEMORY_FILE = BASE_DIR / "memory.json"
    REALTIME_DATA = BASE_DIR / "network_data.json"
    
    def __init__(self):
        self.WORKSPACE.mkdir(exist_ok=True)
        if not self.GOOGLE_KEY:
            raise ValueError("No Google API Key found in .env")

cfg = Config()
