from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class OfferEventResponse(Model):
    raw_data: Dict[Any, Any] = None


@dataclass
class OfferEventsResponse(Response):
    is_idempotency_replayed: bool
