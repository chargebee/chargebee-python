from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ContactResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    label: str = None
    enabled: bool = None
    send_account_email: bool = None
    send_billing_email: bool = None
