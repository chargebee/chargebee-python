from dataclasses import dataclass
from typing import Dict


@dataclass
class Response:
    http_status_code: int
    headers: Dict[str, str]
