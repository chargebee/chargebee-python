from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class ScheduleType(Enum):
    FIXED_INTERVALS = "fixed_intervals"
    SPECIFIC_DATES = "specific_dates"

    def __str__(self):
        return self.value


class FixedIntervalSchedule(TypedDict):
    end_schedule_on: NotRequired[enums.EndScheduleOn]
    number_of_occurrences: NotRequired[int]
    days_before_renewal: NotRequired[int]
    end_date: NotRequired[int]
    created_at: Required[int]
    terms_to_charge: NotRequired[int]


class SpecificDatesSchedule(TypedDict):
    terms_to_charge: NotRequired[int]
    date: NotRequired[int]
    created_at: Required[int]


class AdvanceInvoiceSchedules(TypedDict):
    id: Required[str]
    schedule_type: NotRequired[ScheduleType]
    fixed_interval_schedule: NotRequired[FixedIntervalSchedule]
    specific_dates_schedule: NotRequired[SpecificDatesSchedule]
