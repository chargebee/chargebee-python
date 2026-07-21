from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import column_definition, feature, meter


@dataclass
class MeteredFeatureResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    description: str = None
    type: str = None
    status: str = None
    query: str = None
    column_definitions: List["column_definition.ColumnDefinitionResponse"] = None
    features: List["feature.FeatureResponse"] = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    meter: "meter.MeterResponse"


@dataclass
class ArchiveResponse(Response):
    is_idempotency_replayed: bool
    meter: "meter.MeterResponse"


@dataclass
class ReactivateResponse(Response):
    is_idempotency_replayed: bool
    meter: "meter.MeterResponse"


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    meter: "meter.MeterResponse"
