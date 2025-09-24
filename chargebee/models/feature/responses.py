from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class LevelResponse(Model):
    raw_data: Dict[Any, Any] = None
    name: str = None
    value: str = None
    level: int = None
    is_unlimited: bool = None


@dataclass
class FeatureResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    description: str = None
    status: str = None
    type: str = None
    unit: str = None
    resource_version: int = None
    updated_at: int = None
    created_at: int = None
    levels: List[LevelResponse] = None


@dataclass
class ListFeatureResponse:
    feature: FeatureResponse


@dataclass
class ListResponse(Response):

    list: List[ListFeatureResponse]
    next_offset: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    feature: FeatureResponse


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    feature: FeatureResponse


@dataclass
class RetrieveResponse(Response):

    feature: FeatureResponse


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    feature: FeatureResponse


@dataclass
class ActivateResponse(Response):
    is_idempotency_replayed: bool
    feature: FeatureResponse


@dataclass
class ArchiveResponse(Response):
    is_idempotency_replayed: bool
    feature: FeatureResponse


@dataclass
class ReactivateResponse(Response):
    is_idempotency_replayed: bool
    feature: FeatureResponse
