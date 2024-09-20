from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Status(Enum):
    NOT_REDEEMED = "not_redeemed"
    REDEEMED = "redeemed"
    ARCHIVED = "archived"

    def __str__(self):
        return self.value
