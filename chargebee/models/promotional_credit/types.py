from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Type(Enum):
    INCREMENT = "increment"
    DECREMENT = "decrement"

    def __str__(self):
        return self.value


class PromotionalCredits(TypedDict):
    id: Required[str]
    customer_id: Required[str]
    type: Required[Type]
    amount_in_decimal: NotRequired[str]
    amount: Required[int]
    currency_code: Required[str]
    description: Required[str]
    credit_type: Required[enums.CreditType]
    reference: NotRequired[str]
    closing_balance: Required[int]
    done_by: NotRequired[str]
    created_at: Required[int]
