from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class PeriodUnit(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"

    def __str__(self):
        return self.value


class Installment(TypedDict):
    period: NotRequired[int]
    amount_percentage: NotRequired[float]


class CreateInstallmentParams(TypedDict):
    period: NotRequired[int]
    amount_percentage: NotRequired[float]
