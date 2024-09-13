from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class ForexType(Enum):
    MANUAL = "manual"
    AUTO = "auto"

    def __str__(self):
        return self.value


class Currencies(TypedDict):
    id: NotRequired[str]
    enabled: Required[bool]
    forex_type: NotRequired[ForexType]
    currency_code: NotRequired[str]
    is_base_currency: NotRequired[bool]
    manual_exchange_rate: NotRequired[str]
