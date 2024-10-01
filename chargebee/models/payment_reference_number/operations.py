from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


class PaymentReferenceNumber:
    class Type(Enum):
        KID = "kid"
        OCR = "ocr"
        FRN = "frn"
        FIK = "fik"
        SWISS_REFERENCE = "swiss_reference"

        def __str__(self):
            return self.value

    pass
