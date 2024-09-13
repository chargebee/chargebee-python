from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class Status(Enum):
    NEW = "new"
    EXPIRED = "expired"
    CONSUMED = "consumed"

    def __str__(self):
        return self.value


class Vault(Enum):
    SPREEDLY = "spreedly"
    GATEWAY = "gateway"

    def __str__(self):
        return self.value


class Tokens(TypedDict):
    id: Required[str]
    gateway: Required[enums.Gateway]
    gateway_account_id: Required[str]
    payment_method_type: Required[enums.PaymentMethodType]
    status: Required[Status]
    id_at_vault: Required[str]
    vault: Required[Vault]
    ip_address: NotRequired[str]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    created_at: Required[int]
    expired_at: NotRequired[int]
