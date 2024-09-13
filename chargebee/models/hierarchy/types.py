from typing import TypedDict, Required, NotRequired, Dict, List, Any


class Hierarchies(TypedDict):
    customer_id: Required[str]
    parent_id: NotRequired[str]
    payment_owner_id: Required[str]
    invoice_owner_id: Required[str]
    children_ids: NotRequired[List[str]]
