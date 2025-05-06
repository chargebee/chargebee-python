from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class FixedIntervalScheduleResponse(Model):
    raw_data: Dict[Any, Any] = None
    end_schedule_on: str = None
    number_of_occurrences: int = None
    days_before_renewal: int = None
    end_date: int = None
    created_at: int = None
    terms_to_charge: int = None


@dataclass
class SpecificDatesScheduleResponse(Model):
    raw_data: Dict[Any, Any] = None
    terms_to_charge: int = None
    date: int = None
    created_at: int = None


@dataclass
class AdvanceInvoiceScheduleResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    schedule_type: str = None
    fixed_interval_schedule: FixedIntervalScheduleResponse = None
    specific_dates_schedule: SpecificDatesScheduleResponse = None
