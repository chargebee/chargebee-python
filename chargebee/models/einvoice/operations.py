from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class Einvoice:
    env: environment.Environment

    class Status(Enum):
        SCHEDULED = "scheduled"
        SKIPPED = "skipped"
        IN_PROGRESS = "in_progress"
        SUCCESS = "success"
        FAILED = "failed"
        REGISTERED = "registered"
        ACCEPTED = "accepted"
        REJECTED = "rejected"
        MESSAGE_ACKNOWLEDGEMENT = "message_acknowledgement"
        IN_PROCESS = "in_process"
        UNDER_QUERY = "under_query"
        CONDITIONALLY_ACCEPTED = "conditionally_accepted"
        PAID = "paid"

        def __str__(self):
            return self.value

    pass
