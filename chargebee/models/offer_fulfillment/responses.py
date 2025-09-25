from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import hosted_page


@dataclass
class ErrorResponse(Model):
    raw_data: Dict[Any, Any] = None
    code: str = None
    message: str = None


@dataclass
class OfferFulfillmentResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    personalized_offer_id: str = None
    option_id: str = None
    processing_type: str = None
    status: str = None
    redirect_url: str = None
    failed_at: int = None
    created_at: int = None
    completed_at: int = None
    error: ErrorResponse = None


@dataclass
class OfferFulfillmentsResponse(Response):
    is_idempotency_replayed: bool
    offer_fulfillment: OfferFulfillmentResponse
    hosted_page: "hosted_page.HostedPageResponse" = None


@dataclass
class OfferFulfillmentsGetResponse(Response):
    offer_fulfillment: OfferFulfillmentResponse


@dataclass
class OfferFulfillmentsUpdateResponse(Response):
    is_idempotency_replayed: bool
    offer_fulfillment: OfferFulfillmentResponse
