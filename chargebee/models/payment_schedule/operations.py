from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import transaction


@dataclass
class PaymentSchedule:
    env: environment.Environment

    class EntityType(Enum):
        INVOICE = "invoice"

        def __str__(self):
            return self.value

    class ScheduleEntryStatus(Enum):
        POSTED = "posted"
        PAYMENT_DUE = "payment_due"
        PAID = "paid"

        def __str__(self):
            return self.value

    class ScheduleEntry(TypedDict):
        id: Required[str]
        date: Required[int]
        amount: Required[int]
        scheduled_amount: Required[int]
        status: Required["PaymentSchedule.ScheduleEntryStatus"]

    class ReferenceTransaction(TypedDict):
        schedule_entry_id: Required[str]
        applied_amount: NotRequired[int]
        txn_id: Required[str]
        txn_status: NotRequired["transaction.Transaction.Status"]
        txn_date: NotRequired[int]
        txn_amount: NotRequired[int]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        invoice_id: NotRequired[Filters.StringFilter]
        id: NotRequired[Filters.StringFilter]
        updated_at: NotRequired[Filters.TimestampFilter]

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("payment_schedules"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="paymentSchedule",
            operation="list",
        )
