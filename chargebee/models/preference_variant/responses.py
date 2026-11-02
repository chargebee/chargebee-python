from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class PreferenceVariantResponse(Model):
    raw_data: Dict[Any, Any] = None
    value: str = None
    allow_override_in_interface: bool = None
    allow_override_in_api: bool = None
