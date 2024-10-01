from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


class InAppSubscription:
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

    @staticmethod
    def process_receipt(
        id, params: ProcessReceiptParams, env=None, headers=None
    ) -> ProcessReceiptResponse:
        return request.send(
            "post",
            request.uri_path("in_app_subscriptions", id, "process_purchase_command"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ProcessReceiptResponse,
        )

    @staticmethod
    def import_receipt(
        id, params: ImportReceiptParams, env=None, headers=None
    ) -> ImportReceiptResponse:
        return request.send(
            "post",
            request.uri_path("in_app_subscriptions", id, "import_receipt"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportReceiptResponse,
        )

    @staticmethod
    def import_subscription(
        id, params: ImportSubscriptionParams, env=None, headers=None
    ) -> ImportSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("in_app_subscriptions", id, "import_subscription"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportSubscriptionResponse,
        )

    @staticmethod
    def retrieve_store_subs(
        id, params: RetrieveStoreSubsParams, env=None, headers=None
    ) -> RetrieveStoreSubsResponse:
        return request.send(
            "post",
            request.uri_path("in_app_subscriptions", id, "retrieve"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RetrieveStoreSubsResponse,
        )
