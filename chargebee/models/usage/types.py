from typing import TypedDict, Required, NotRequired, Dict, List, Any
from chargebee.models import enums


class PdfInvoiceParams(TypedDict):
    id: Required[str]
