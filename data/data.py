
import json
from typing import List
from model import Trip

def load_data(path) -> List[Trip]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Trip(**item) for item in data]