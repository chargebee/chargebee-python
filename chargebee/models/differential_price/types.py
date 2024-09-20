from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    DELETED = "deleted"

    def __str__(self):
        return self.value


class ParentPeriodPeriodUnit(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def __str__(self):
        return self.value


class Tier(TypedDict):
    starting_unit: Required[int]
    ending_unit: NotRequired[int]
    price: Required[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class ParentPeriod(TypedDict):
    period_unit: Required[ParentPeriodPeriodUnit]
    period: NotRequired[List[Dict[Any, Any]]]


class CreateParentPeriodParams(TypedDict):
    period_unit: Required[ParentPeriodPeriodUnit]
    period: NotRequired[List[Dict[Any, Any]]]


class CreateTierParams(TypedDict):
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class UpdateParentPeriodParams(TypedDict):
    period_unit: Required[ParentPeriodPeriodUnit]
    period: NotRequired[List[Dict[Any, Any]]]


class UpdateTierParams(TypedDict):
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]
