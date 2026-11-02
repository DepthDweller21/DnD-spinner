import json
from pathlib import Path


def load(data):
    BASE_DIR = Path(__file__).parent.parent.parent

    with open(BASE_DIR / "datatables" / f"{data}.json", "r") as file:
        data = json.load(file)
    
    return data