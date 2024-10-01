from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import gateway_error_detail


class PaymentIntent:
    class Status(Enum):
        INITED = "inited"
        IN_PROGRESS = "in_progress"
        AUTHORIZED = "authorized"
        CONSUMED = "consumed"
        EXPIRED = "expired"

        def __str__(self):
            return self.value

    class PaymentMethodType(Enum):
        CARD = "card"
        IDEAL = "ideal"
        SOFORT = "sofort"
        BANCONTACT = "bancontact"
        GOOGLE_PAY = "google_pay"
        DOTPAY = "dotpay"
        GIROPAY = "giropay"
        APPLE_PAY = "apple_pay"
        UPI = "upi"
        NETBANKING_EMANDATES = "netbanking_emandates"
        PAYPAL_EXPRESS_CHECKOUT = "paypal_express_checkout"
        DIRECT_DEBIT = "direct_debit"
        BOLETO = "boleto"
        VENMO = "venmo"
        AMAZON_PAYMENTS = "amazon_payments"
        PAY_TO = "pay_to"
        FASTER_PAYMENTS = "faster_payments"
        SEPA_INSTANT_TRANSFER = "sepa_instant_transfer"
        KLARNA_PAY_NOW = "klarna_pay_now"
        ONLINE_BANKING_POLAND = "online_banking_poland"

        def __str__(self):
            return self.value

    class PaymentAttemptStatus(Enum):
        INITED = "inited"
        REQUIRES_IDENTIFICATION = "requires_identification"
        REQUIRES_CHALLENGE = "requires_challenge"
        REQUIRES_REDIRECTION = "requires_redirection"
        AUTHORIZED = "authorized"
        REFUSED = "refused"
        PENDING_AUTHORIZATION = "pending_authorization"

        def __str__(self):
            return self.value

    class PaymentAttempt(TypedDict):
        id: NotRequired[str]
        status: Required["PaymentIntent.PaymentAttemptStatus"]
        payment_method_type: NotRequired["PaymentIntent.PaymentMethodType"]
        id_at_gateway: NotRequired[str]
        error_code: NotRequired[str]
        error_text: NotRequired[str]
        created_at: Required[int]
        modified_at: Required[int]
        error_detail: NotRequired[gateway_error_detail.GatewayErrorDetailResponse]

    class CreateParams(TypedDict):
        business_entity_id: NotRequired[str]
        customer_id: NotRequired[str]
        amount: Required[int]
        currency_code: Required[str]
        gateway_account_id: NotRequired[str]
        reference_id: NotRequired[str]
        payment_method_type: NotRequired["PaymentIntent.PaymentMethodType"]
        success_url: NotRequired[str]
        failure_url: NotRequired[str]

    class UpdateParams(TypedDict):
        amount: NotRequired[int]
        currency_code: NotRequired[str]
        gateway_account_id: NotRequired[str]
        payment_method_type: NotRequired["PaymentIntent.PaymentMethodType"]
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
