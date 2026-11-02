from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class CollectionsPaymentPromise:
    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        FULFILLED = "fulfilled"
        BROKEN = "broken"
        CANCELLED = "cancelled"

        def __str__(self):
            return self.value

    class ListCollectionsPaymentPromisesParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        customer_id: NotRequired[Filters.StringFilter]
        invoice_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]

    class CreateCollectionsPaymentPromiseParams(TypedDict):
        customer_id: Required[str]
        invoice_id: NotRequired[str]
        amount: Required[int]
        currency_code: NotRequired[str]
        promised_on: Required[int]
        reason: NotRequired[str]
        promised_by: NotRequired[str]

    class UpdateCollectionsPaymentPromiseParams(TypedDict):
        promised_on: NotRequired[int]
        reason: NotRequired[str]
        promised_by: NotRequired[str]

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("collections_payment_promises", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="collectionsPaymentPromise",
            operation="retrieve",
        )

    def list_collections_payment_promises(
        self, params: ListCollectionsPaymentPromisesParams = None, headers=None
    ) -> ListCollectionsPaymentPromisesResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("collections_payment_promises"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListCollectionsPaymentPromisesResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="collectionsPaymentPromise",
            operation="listCollectionsPaymentPromises",
        )

    def create_collections_payment_promise(
        self, params: CreateCollectionsPaymentPromiseParams, headers=None
    ) -> CreateCollectionsPaymentPromiseResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("collections_payment_promises"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateCollectionsPaymentPromiseResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="collectionsPaymentPromise",
            operation="createCollectionsPaymentPromise",
        )

    def update_collections_payment_promise(
        self, id, params: UpdateCollectionsPaymentPromiseParams = None, headers=None
    ) -> UpdateCollectionsPaymentPromiseResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("collections_payment_promises", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateCollectionsPaymentPromiseResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="collectionsPaymentPromise",
            operation="updateCollectionsPaymentPromise",
        )

    def cancel(self, id, headers=None) -> CancelResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("collections_payment_promises", id, "cancel"),
            self.env,
            None,
            headers,
            CancelResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="collectionsPaymentPromise",
            operation="cancel",
        )
