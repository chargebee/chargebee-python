from typing import TypedDict, Required, NotRequired, Dict, List, Any
from chargebee.models import enums


class Usages(TypedDict):
    id: NotRequired[str]
    usage_date: Required[int]
    subscription_id: Required[str]
    item_price_id: Required[str]
    invoice_id: NotRequired[str]
    line_item_id: NotRequired[str]
    quantity: Required[str]
    source: NotRequired[enums.Source]
    note: NotRequired[str]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    created_at: Required[int]


class PdfInvoiceParams(TypedDict):
    id: Required[str]
