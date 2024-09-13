from typing import TypedDict, Required, NotRequired, Dict, List, Any
from chargebee.models import enums


class ThirdPartyPaymentMethods(TypedDict):
    type: Required[enums.Type]
    gateway: Required[enums.Gateway]
    gateway_account_id: NotRequired[str]
    reference_id: Required[str]
