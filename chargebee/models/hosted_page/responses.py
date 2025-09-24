from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import contract_term


@dataclass
class HostedPageResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    type: str = None
    url: str = None
    state: str = None
    failure_reason: str = None
    pass_thru_content: str = None
    embed: bool = None
    created_at: int = None
    expires_at: int = None
    content: Dict[Any, Any] = None
    updated_at: int = None
    resource_version: int = None
    checkout_info: Dict[Any, Any] = None
    business_entity_id: str = None


@dataclass
class CheckoutNewResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class CheckoutOneTimeResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class CheckoutOneTimeForItemsResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class CheckoutNewForItemsResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class CheckoutExistingResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class CheckoutExistingForItemsResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class UpdateCardResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class UpdatePaymentMethodResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class ManagePaymentSourcesResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class CollectNowResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class AcceptQuoteResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class ExtendSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class CheckoutGiftResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class CheckoutGiftForItemsResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class ClaimGiftResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class RetrieveAgreementPdfResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class AcknowledgeResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class RetrieveResponse(Response):

    hosted_page: HostedPageResponse


@dataclass
class ListHostedPageResponse:
    hosted_page: HostedPageResponse


@dataclass
class ListResponse(Response):

    list: List[ListHostedPageResponse]
    next_offset: str = None


@dataclass
class PreCancelResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse


@dataclass
class EventsResponse(Response):
    is_idempotency_replayed: bool
    success: bool


@dataclass
class ViewVoucherResponse(Response):
    is_idempotency_replayed: bool
    hosted_page: HostedPageResponse
