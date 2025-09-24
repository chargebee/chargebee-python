from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class GatewayErrorDetailResponse(Model):
    raw_data: Dict[Any, Any] = None
    request_id: str = None
    error_category: str = None
    error_code: str = None
    error_message: str = None
    decline_code: str = None
    decline_message: str = None
    network_error_code: str = None
    network_error_message: str = None
    error_field: str = None
    recommendation_code: str = None
    recommendation_message: str = None
    processor_error_code: str = None
    processor_error_message: str = None
    error_cause_id: str = None
    processor_advice_code: str = None
