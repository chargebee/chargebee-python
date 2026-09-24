from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class ArtifactResponse(Model):
    raw_data: Dict[Any, Any] = None
    artifact_type: str = None
    direction: str = None
    status: str = None
    code: str = None
    external_artifact_id: str = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    deleted: bool = None


@dataclass
class EinvoiceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    entity_type: str = None
    entity_id: str = None
    reference_id: str = None
    reference_number: str = None
    status: str = None
    message: str = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    deleted: bool = None
    provider_references: List[Dict[Any, Any]] = None
    business_entity_id: str = None
    artifacts: List[ArtifactResponse] = None


@dataclass
class RetrieveResponse(Response):
    einvoice: EinvoiceResponse


@dataclass
class ListEinvoicesEinvoiceResponse:
    einvoice: EinvoiceResponse


@dataclass
class ListEinvoicesResponse(Response):
    list: List[ListEinvoicesEinvoiceResponse]
    next_offset: str = None
