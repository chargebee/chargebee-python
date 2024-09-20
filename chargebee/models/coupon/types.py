from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class DiscountType(Enum):
    FIXED_AMOUNT = "fixed_amount"
    PERCENTAGE = "percentage"

    def __str__(self):
        return self.value


class DurationType(Enum):
    ONE_TIME = "one_time"
    FOREVER = "forever"
    LIMITED_PERIOD = "limited_period"

    def __str__(self):
        return self.value


class Status(Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    ARCHIVED = "archived"
    DELETED = "deleted"

    def __str__(self):
        return self.value


class ApplyDiscountOn(Enum):
    PLANS = "plans"
    PLANS_AND_ADDONS = "plans_and_addons"
    PLANS_WITH_QUANTITY = "plans_with_quantity"
    NOT_APPLICABLE = "not_applicable"

    def __str__(self):
        return self.value


class ApplyOn(Enum):
    INVOICE_AMOUNT = "invoice_amount"
    EACH_SPECIFIED_ITEM = "each_specified_item"

    def __str__(self):
        return self.value


class AddonConstraint(Enum):
    NONE = "none"
    ALL = "all"
    SPECIFIC = "specific"
    NOT_APPLICABLE = "not_applicable"

    def __str__(self):
        return self.value


class PlanConstraint(Enum):
    NONE = "none"
    ALL = "all"
    SPECIFIC = "specific"
    NOT_APPLICABLE = "not_applicable"

    def __str__(self):
        return self.value


class ItemConstraintItemType(Enum):
    PLAN = "plan"
    ADDON = "addon"
    CHARGE = "charge"

    def __str__(self):
        return self.value


class ItemConstraintConstraint(Enum):
    NONE = "none"
    ALL = "all"
    SPECIFIC = "specific"
    CRITERIA = "criteria"

    def __str__(self):
        return self.value


class ItemConstraintCriteriaItemType(Enum):
    PLAN = "plan"
    ADDON = "addon"
    CHARGE = "charge"

    def __str__(self):
        return self.value


class CouponConstraintEntityType(Enum):
    CUSTOMER = "customer"

    def __str__(self):
        return self.value


class CouponConstraintType(Enum):
    MAX_REDEMPTIONS = "max_redemptions"
    UNIQUE_BY = "unique_by"

    def __str__(self):
        return self.value


class ItemConstraint(TypedDict):
    item_type: Required[ItemConstraintItemType]
    constraint: Required[ItemConstraintConstraint]
    item_price_ids: NotRequired[List[Dict[Any, Any]]]


class ItemConstraintCriteria(TypedDict):
    item_type: Required[ItemConstraintCriteriaItemType]
    currencies: NotRequired[List[Dict[Any, Any]]]
    item_family_ids: NotRequired[List[Dict[Any, Any]]]
    item_price_periods: NotRequired[List[Dict[Any, Any]]]


class CouponConstraint(TypedDict):
    entity_type: Required[CouponConstraintEntityType]
    type: Required[CouponConstraintType]
    value: NotRequired[str]


class CreateForItemsItemConstraintParams(TypedDict):
    constraint: Required[ItemConstraintConstraint]
    item_type: Required[ItemConstraintItemType]
    item_price_ids: NotRequired[List[Dict[Any, Any]]]


class CreateForItemsItemConstraintCriteriaParams(TypedDict):
    item_type: NotRequired[ItemConstraintCriteriaItemType]
    item_family_ids: NotRequired[List[Dict[Any, Any]]]
    currencies: NotRequired[List[Dict[Any, Any]]]
    item_price_periods: NotRequired[List[Dict[Any, Any]]]


class CreateForItemsCouponConstraintParams(TypedDict):
    entity_type: Required[CouponConstraintEntityType]
    type: Required[CouponConstraintType]
    value: NotRequired[str]


class UpdateForItemsItemConstraintParams(TypedDict):
    constraint: Required[ItemConstraintConstraint]
    item_type: Required[ItemConstraintItemType]
    item_price_ids: NotRequired[List[Dict[Any, Any]]]


class UpdateForItemsItemConstraintCriteriaParams(TypedDict):
    item_type: NotRequired[ItemConstraintCriteriaItemType]
    item_family_ids: NotRequired[List[Dict[Any, Any]]]
    currencies: NotRequired[List[Dict[Any, Any]]]
    item_price_periods: NotRequired[List[Dict[Any, Any]]]


class UpdateForItemsCouponConstraintParams(TypedDict):
    entity_type: Required[CouponConstraintEntityType]
    type: Required[CouponConstraintType]
    value: NotRequired[str]
