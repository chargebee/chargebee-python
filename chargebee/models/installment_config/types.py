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


class InstallmentConfigs(TypedDict):
    id: Required[str]
    description: NotRequired[str]
    number_of_installments: Required[int]
    period_unit: Required[PeriodUnit]
    period: NotRequired[int]
    preferred_day: NotRequired[int]
    created_at: Required[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    installments: NotRequired[List[Installment]]


class CreateInstallmentParams(TypedDict):
    period: NotRequired[int]
    amount_percentage: NotRequired[float]
