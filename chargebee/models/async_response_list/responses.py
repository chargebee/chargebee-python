from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.models import async_response


@dataclass
class AsyncResponseListResponse(Model):
    raw_data: Dict[Any, Any] = None
    list: List["async_response.AsyncResponseResponse"] = None
