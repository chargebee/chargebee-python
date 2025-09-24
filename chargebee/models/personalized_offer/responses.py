from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import brand


@dataclass
class ContentResponse(Model):
    raw_data: Dict[Any, Any] = None
    title: str = None
    description: str = None


@dataclass
class OptionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    label: str = None
    processing_type: str = None
    processing_layout: str = None
    redirect_url: str = None


@dataclass
class PersonalizedOfferResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    offer_id: str = None
    content: ContentResponse = None
    options: List[OptionResponse] = None


@dataclass
class PersonalizedOffersResponse(Response):
    is_idempotency_replayed: bool
    personalized_offers: List[PersonalizedOfferResponse]
    expires_at: int
    brand: "brand.BrandResponse" = None
