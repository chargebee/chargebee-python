from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class Token:
    env: environment.Environment

    class Status(Enum):
        NEW = "new"
        EXPIRED = "expired"
        CONSUMED = "consumed"

        def __str__(self):
            return self.value

    class Vault(Enum):
        SPREEDLY = "spreedly"
        GATEWAY = "gateway"

        def __str__(self):
            return self.value

    pass
