from typing import TypedDict, Required, NotRequired, Dict, List, Any


class CustomerEntitlements(TypedDict):
    customer_id: Required[str]
    subscription_id: NotRequired[str]
    feature_id: NotRequired[str]
    value: NotRequired[str]
    name: NotRequired[str]
    is_enabled: Required[bool]
