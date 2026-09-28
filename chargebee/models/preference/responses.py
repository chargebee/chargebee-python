from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response

@dataclass
class Criteria(Model):
    raw_data: Dict[Any, Any] = None
    operand: str = None
    operator: str = None
    values: List[str] = None


@dataclass
class VariantResponse(Model):
    raw_data: Dict[Any, Any] = None
    value: str = None
    allow_override_in_interface: bool = None
    allow_override_in_api: bool = None
    criteria: List[Criteria] = None


@dataclass
class PreferenceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    setting_group: str = None
    value: str = None
    allow_override_in_interface: bool = None
    allow_override_in_api: bool = None
    variants: List[VariantResponse] = None
    created_at: int = None
    updated_at: int = None


@dataclass
class ListResponse(Response):

    preference: PreferenceResponse

@dataclass
class UpsertResponse(Response):
    is_idempotency_replayed: bool
    preference: PreferenceResponse

