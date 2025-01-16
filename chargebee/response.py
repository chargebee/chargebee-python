from dataclasses import dataclass


@dataclass
class Response:
    is_idempotency_replayed: bool
