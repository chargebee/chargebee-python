from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
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
class CheckoutNewResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CheckoutOneTimeResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CheckoutOneTimeForItemsResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CheckoutNewForItemsResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CheckoutExistingResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CheckoutExistingForItemsResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateCardResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdatePaymentMethodResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ManagePaymentSourcesResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CollectNowResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class AcceptQuoteResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ExtendSubscriptionResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CheckoutGiftResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CheckoutGiftForItemsResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ClaimGiftResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveAgreementPdfResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class AcknowledgeResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListHostedPageResponse:
    hosted_page: HostedPageResponse


@dataclass
class ListResponse:
    list: List[ListHostedPageResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class PreCancelResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class EventsResponse:
    success: bool
    response_headers: Dict[Any, Any] = None


@dataclass
class ViewVoucherResponse:
    hosted_page: HostedPageResponse
    response_headers: Dict[Any, Any] = None
