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
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class CheckoutOneTimeResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class CheckoutOneTimeForItemsResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class CheckoutNewForItemsResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class CheckoutExistingResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class CheckoutExistingForItemsResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateCardResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class UpdatePaymentMethodResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class ManagePaymentSourcesResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class CollectNowResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class AcceptQuoteResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class ExtendSubscriptionResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class CheckoutGiftResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class CheckoutGiftForItemsResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class ClaimGiftResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveAgreementPdfResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class AcknowledgeResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class ListHostedPageResponse:
    hosted_page: HostedPageResponse


@dataclass
class ListResponse:
    list: List[ListHostedPageResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class PreCancelResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None


@dataclass
class EventsResponse(Response):
    success: bool
    headers: Dict[str, str] = None


@dataclass
class ViewVoucherResponse(Response):
    hosted_page: HostedPageResponse
    headers: Dict[str, str] = None
