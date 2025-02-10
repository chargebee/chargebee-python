from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class InAppSubscription:

    env: environment.Environment

    class StoreStatus(Enum):
        IN_TRIAL = "in_trial"
        ACTIVE = "active"
        CANCELLED = "cancelled"
        PAUSED = "paused"

        def __str__(self):
            return self.value

    class ProcessReceiptProductParams(TypedDict):
        id: Required[str]
        currency_code: Required[str]
        price: Required[int]
        name: NotRequired[str]
        price_in_decimal: NotRequired[str]
        period: NotRequired[str]
        period_unit: NotRequired[str]

    class ProcessReceiptCustomerParams(TypedDict):
        id: NotRequired[str]
        email: NotRequired[str]
        first_name: NotRequired[str]
        last_name: NotRequired[str]

    class ImportReceiptProductParams(TypedDict):
        currency_code: Required[str]

    class ImportReceiptCustomerParams(TypedDict):
        id: NotRequired[str]
        email: NotRequired[str]

    class ImportSubscriptionSubscriptionParams(TypedDict):
        id: Required[str]
        started_at: Required[int]
        term_start: Required[int]
        term_end: Required[int]
        product_id: Required[str]
        currency_code: Required[str]
        transaction_id: Required[str]
        is_trial: NotRequired[bool]

    class ImportSubscriptionCustomerParams(TypedDict):
        id: NotRequired[str]
        email: NotRequired[str]

    class ProcessReceiptParams(TypedDict):
        receipt: Required[str]
        product: Required["InAppSubscription.ProcessReceiptProductParams"]
        customer: NotRequired["InAppSubscription.ProcessReceiptCustomerParams"]

    class ImportReceiptParams(TypedDict):
        receipt: Required[str]
        product: Required["InAppSubscription.ImportReceiptProductParams"]
        customer: NotRequired["InAppSubscription.ImportReceiptCustomerParams"]

    class ImportSubscriptionParams(TypedDict):
        subscription: Required["InAppSubscription.ImportSubscriptionSubscriptionParams"]
        customer: NotRequired["InAppSubscription.ImportSubscriptionCustomerParams"]

    class RetrieveStoreSubsParams(TypedDict):
        receipt: Required[str]

    def process_receipt(
        self, id, params: ProcessReceiptParams, headers=None
    ) -> ProcessReceiptResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("in_app_subscriptions", id, "process_purchase_command"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ProcessReceiptResponse,
            None,
            False,
            jsonKeys,
        )

    def import_receipt(
        self, id, params: ImportReceiptParams, headers=None
    ) -> ImportReceiptResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("in_app_subscriptions", id, "import_receipt"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportReceiptResponse,
            None,
            False,
            jsonKeys,
        )

    def import_subscription(
        self, id, params: ImportSubscriptionParams, headers=None
    ) -> ImportSubscriptionResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("in_app_subscriptions", id, "import_subscription"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportSubscriptionResponse,
            None,
            False,
            jsonKeys,
        )

    def retrieve_store_subs(
        self, id, params: RetrieveStoreSubsParams, headers=None
    ) -> RetrieveStoreSubsResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("in_app_subscriptions", id, "retrieve"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveStoreSubsResponse,
            None,
            False,
            jsonKeys,
        )
