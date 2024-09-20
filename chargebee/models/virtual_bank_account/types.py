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
