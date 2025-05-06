from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import omnichannel_subscription_item, omnichannel_transaction


@dataclass
class OmnichannelTransactionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    id_at_source: str = None
    app_id: str = None
    price_currency: str = None
    price_units: int = None
    price_nanos: int = None
    type: str = None
    transacted_at: int = None
    created_at: int = None
    resource_version: int = None


@dataclass
class OmnichannelSubscriptionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    id_at_source: str = None
    app_id: str = None
    source: str = None
    customer_id: str = None
    created_at: int = None
    resource_version: int = None
    omnichannel_subscription_items: List[
        "omnichannel_subscription_item.OmnichannelSubscriptionItemResponse"
    ] = None
    initial_purchase_transaction: (
        "omnichannel_transaction.OmnichannelTransactionResponse"
    ) = None


@dataclass
class RetrieveResponse(Response):

    omnichannel_subscription: OmnichannelSubscriptionResponse


@dataclass
class ListOmnichannelSubscriptionResponse:
    omnichannel_subscription: OmnichannelSubscriptionResponse


@dataclass
class ListResponse(Response):

    list: List[ListOmnichannelSubscriptionResponse]
    next_offset: str = None


@dataclass
class OmnichannelTransactionsForOmnichannelSubscriptionOmnichannelSubscriptionResponse:
    omnichannel_transaction: "omnichannel_transaction.OmnichannelTransactionResponse"


@dataclass
class OmnichannelTransactionsForOmnichannelSubscriptionResponse(Response):

    list: List[
        OmnichannelTransactionsForOmnichannelSubscriptionOmnichannelSubscriptionResponse
    ]
    next_offset: str = None
