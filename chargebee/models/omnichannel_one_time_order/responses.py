from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import omnichannel_one_time_order_item, omnichannel_transaction


@dataclass
class OmnichannelOneTimeOrderResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    app_id: str = None
    customer_id: str = None
    id_at_source: str = None
    origin: str = None
    source: str = None
    created_at: int = None
    resource_version: int = None
    omnichannel_one_time_order_items: List[
        "omnichannel_one_time_order_item.OmnichannelOneTimeOrderItemResponse"
    ] = None
    purchase_transaction: "omnichannel_transaction.OmnichannelTransactionResponse" = (
        None
    )


@dataclass
class RetrieveResponse(Response):
    omnichannel_one_time_order: OmnichannelOneTimeOrderResponse


@dataclass
class ListOmnichannelOneTimeOrderResponse:
    omnichannel_one_time_order: OmnichannelOneTimeOrderResponse


@dataclass
class ListResponse(Response):
    list: List[ListOmnichannelOneTimeOrderResponse]
    next_offset: str = None
