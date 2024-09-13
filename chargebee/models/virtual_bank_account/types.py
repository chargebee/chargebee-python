from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Scheme(Enum):
    ACH_CREDIT = "ach_credit"
    SEPA_CREDIT = "sepa_credit"
    US_AUTOMATED_BANK_TRANSFER = "us_automated_bank_transfer"
    GB_AUTOMATED_BANK_TRANSFER = "gb_automated_bank_transfer"
    EU_AUTOMATED_BANK_TRANSFER = "eu_automated_bank_transfer"
    JP_AUTOMATED_BANK_TRANSFER = "jp_automated_bank_transfer"
    MX_AUTOMATED_BANK_TRANSFER = "mx_automated_bank_transfer"

    def __str__(self):
        return self.value


class VirtualBankAccounts(TypedDict):
    id: Required[str]
    customer_id: Required[str]
    email: Required[str]
    scheme: NotRequired[Scheme]
    bank_name: NotRequired[str]
    account_number: Required[str]
    routing_number: NotRequired[str]
    swift_code: Required[str]
    gateway: Required[enums.Gateway]
    gateway_account_id: Required[str]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    created_at: Required[int]
    reference_id: Required[str]
    deleted: Required[bool]
