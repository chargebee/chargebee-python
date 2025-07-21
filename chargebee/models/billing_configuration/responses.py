from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class BillingDateResponse(Model):
    raw_data: Dict[Any, Any] = None
    start_date: int = None
    end_date: int = None


@dataclass
class BillingConfigurationResponse(Model):
    raw_data: Dict[Any, Any] = None
    is_calendar_billing_enabled: bool = None
    billing_dates: List[BillingDateResponse] = None
