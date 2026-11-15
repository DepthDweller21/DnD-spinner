import json
from pathlib import Path


def load(data,root="datatables"):
    BASE_DIR = Path(__file__).parent.parent.parent

    with open(BASE_DIR / root / f"{data}.json", "r") as file:
        data = json.load(file)
    
    return data