from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class OrganizationDetailResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    organization_name: str = None
    email: str = None
    address_line1: str = None
    address_line2: str = None
    address_line3: str = None
    city: str = None
    state_code: str = None
    state: str = None
    country_code: str = None
    zip: str = None
    phone: str = None
    fax: str = None
    website: str = None
    is_vat_number_present: bool = None
    vat_number: str = None
    resource_version: int = None
    updated_at: int = None
    business_entity_id: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    organization_detail: OrganizationDetailResponse


@dataclass
class RetrieveResponse(Response):
    organization_detail: OrganizationDetailResponse


@dataclass
class ListOrganizationDetailResponse:
    organization_detail: OrganizationDetailResponse


@dataclass
class ListResponse(Response):
    list: List[ListOrganizationDetailResponse]
    next_offset: str = None
