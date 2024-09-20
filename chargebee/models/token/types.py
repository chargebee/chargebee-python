from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


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
