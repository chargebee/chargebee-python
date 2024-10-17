from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


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
    headers: Dict[str, str] = None


@dataclass
class CreateResponse(Response):
    feature: FeatureResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateResponse(Response):
    feature: FeatureResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    feature: FeatureResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    feature: FeatureResponse
    headers: Dict[str, str] = None


@dataclass
class ActivateResponse(Response):
    feature: FeatureResponse
    headers: Dict[str, str] = None


@dataclass
class ArchiveResponse(Response):
    feature: FeatureResponse
    headers: Dict[str, str] = None


@dataclass
class ReactivateResponse(Response):
    feature: FeatureResponse
    headers: Dict[str, str] = None
