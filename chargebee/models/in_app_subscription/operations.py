from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class InAppSubscription:

    class ProcessReceiptParams(TypedDict):
        receipt: Required[str]
        product: Required[ProcessReceiptProductParams]
        customer: NotRequired[ProcessReceiptCustomerParams]

    class ImportReceiptParams(TypedDict):
        receipt: Required[str]
        product: Required[ImportReceiptProductParams]
        customer: NotRequired[ImportReceiptCustomerParams]

    class ImportSubscriptionParams(TypedDict):
        subscription: Required[ImportSubscriptionSubscriptionParams]
        customer: NotRequired[ImportSubscriptionCustomerParams]

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
