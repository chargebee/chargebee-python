from dataclasses import dataclass


@dataclass
class Response:
    is_idempotency_replayed: bool
    http_status_code: int
