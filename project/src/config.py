from typing import Optional
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"

print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)
print("API_KEY:", get_key("API_KEY"))
