from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import column_definition, feature


@dataclass
class MeterResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    description: str = None
    type: str = None
    status: str = None
    query: str = None
    created_at: int = None
    updated_at: int = None
    column_definitions: List["column_definition.ColumnDefinitionResponse"] = None
    features: List["feature.FeatureResponse"] = None


@dataclass
class ListMeterResponse:
    meter: MeterResponse


@dataclass
class ListResponse(Response):
    list: List[ListMeterResponse]
    next_offset: str = None
