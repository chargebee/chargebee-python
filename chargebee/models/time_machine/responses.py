from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class TimeMachineResponse(Model):
    raw_data: Dict[Any, Any] = None
    name: str = None
    time_travel_status: str = None
    genesis_time: int = None
    destination_time: int = None
    failure_code: str = None
    failure_reason: str = None
    error_json: str = None


@dataclass
class RetrieveResponse(Response):
    time_machine: TimeMachineResponse


@dataclass
class StartAfreshResponse(Response):
    is_idempotency_replayed: bool
    time_machine: TimeMachineResponse


@dataclass
class TravelForwardResponse(Response):
    is_idempotency_replayed: bool
    time_machine: TimeMachineResponse
