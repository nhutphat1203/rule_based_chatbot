from dataclasses import dataclass
from typing import List

@dataclass
class Trip:
    destination: str
    cost: float
    times: List[str]
