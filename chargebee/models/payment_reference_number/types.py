from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum


class Type(Enum):
    KID = "kid"
    OCR = "ocr"
    FRN = "frn"
    FIK = "fik"
    SWISS_REFERENCE = "swiss_reference"

    def __str__(self):
        return self.value


class PaymentReferenceNumbers(TypedDict):
    id: Required[str]
    type: Required[Type]
    number: Required[str]
    invoice_id: NotRequired[str]
