from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


class ContractTerm:
    class Status(Enum):
        ACTIVE = "active"
        COMPLETED = "completed"
        CANCELLED = "cancelled"
        TERMINATED = "terminated"

        def __str__(self):
            return self.value

    class ActionAtTermEnd(Enum):
        RENEW = "renew"
        EVERGREEN = "evergreen"
        CANCEL = "cancel"
        RENEW_ONCE = "renew_once"

        def __str__(self):
            return self.value

    pass
