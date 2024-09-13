from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class PaymentIntent:

    class CreateParams(TypedDict):
        business_entity_id: NotRequired[str]
        customer_id: NotRequired[str]
        amount: Required[int]
        currency_code: Required[str]
        gateway_account_id: NotRequired[str]
        reference_id: NotRequired[str]
        payment_method_type: NotRequired[PaymentMethodType]
        success_url: NotRequired[str]
        failure_url: NotRequired[str]

    class UpdateParams(TypedDict):
        amount: NotRequired[int]
        currency_code: NotRequired[str]
        gateway_account_id: NotRequired[str]
        payment_method_type: NotRequired[PaymentMethodType]
        success_url: NotRequired[str]
        failure_url: NotRequired[str]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("payment_intents"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def update(
        id, params: UpdateParams = None, env=None, headers=None
    ) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("payment_intents", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("payment_intents", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )
