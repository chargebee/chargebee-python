from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class LedgerEntry:
    env: environment.Environment

    class AccountType(Enum):
        PROVISIONED = "provisioned"
        OVERDRAFT = "overdraft"

        def __str__(self):
            return self.value

    class UnitType(Enum):
        CREDIT_UNIT = "credit_unit"

        def __str__(self):
            return self.value

    pass
