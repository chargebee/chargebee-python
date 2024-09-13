from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class LevelResponse(Model):
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
class ListResponse:
    list: List[ListFeatureResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateResponse:
    feature: FeatureResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateResponse:
    feature: FeatureResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    feature: FeatureResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    feature: FeatureResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ActivateResponse:
    feature: FeatureResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ArchiveResponse:
    feature: FeatureResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ReactivateResponse:
    feature: FeatureResponse
    response_headers: Dict[Any, Any] = None
