from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class CollectionsReminderSequence:
    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        COMPLETED = "completed"
        PAUSED = "paused"
        FAILED = "failed"

        def __str__(self):
            return self.value

    class CollectionsReminderSequenceActionLogActionType(Enum):
        SEND_EMAIL = "send_email"

        def __str__(self):
            return self.value

    class CollectionsReminderSequenceActionLogStatus(Enum):
        COMPLETED = "completed"
        SCHEDULED = "scheduled"
        SKIPPED = "skipped"

        def __str__(self):
            return self.value

    class CollectionsReminderSequenceActionLogReasonCode(Enum):
        DATE_ALREADY_PASSED = "date_already_passed"
        BEFORE_INVOICE_DATE = "before_invoice_date"
        TRIGGER_EVENT_NOT_RECEIVED = "trigger_event_not_received"
        SEQUENCE_PAUSED = "sequence_paused"

        def __str__(self):
            return self.value

    class ActionLog(TypedDict):
        action_type: Required[
            "CollectionsReminderSequence.CollectionsReminderSequenceActionLogActionType"
        ]
        status: Required[
            "CollectionsReminderSequence.CollectionsReminderSequenceActionLogStatus"
        ]
        reason_code: NotRequired[
            "CollectionsReminderSequence.CollectionsReminderSequenceActionLogReasonCode"
        ]
        executed_at: NotRequired[int]
        scheduled_at: NotRequired[int]

    pass
