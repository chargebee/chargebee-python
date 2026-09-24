from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class EmailLogResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    template_name: str = None
    from_address: str = None
    to_address: str = None
    subject: str = None
    status: str = None
    sent_on: int = None
    customer_id: str = None
    site_id: str = None
    business_entity_id: str = None
    brand_id: str = None
    error_message: str = None


@dataclass
class EmailLogsForCustomerEmailLogResponse:
    email_log: EmailLogResponse


@dataclass
class EmailLogsForCustomerResponse(Response):
    list: List[EmailLogsForCustomerEmailLogResponse]
    next_offset: str = None
