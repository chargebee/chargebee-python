from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import gateway_error_detail


@dataclass
class PaymentIntent:
    env: environment.Environment

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
        PAYCONIQ_BY_BANCONTACT = "payconiq_by_bancontact"
        ELECTRONIC_PAYMENT_STANDARD = "electronic_payment_standard"
        KBC_PAYMENT_BUTTON = "kbc_payment_button"
        PAY_BY_BANK = "pay_by_bank"
        TRUSTLY = "trustly"
        STABLECOIN = "stablecoin"

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
        checkout_details: NotRequired[str]
        created_at: Required[int]
        modified_at: Required[int]
        error_detail: NotRequired[gateway_error_detail.GatewayErrorDetailResponse]

    class PaymentAttempt(TypedDict):
        id: NotRequired[str]
        status: Required["PaymentIntent.PaymentAttemptStatus"]
        payment_method_type: NotRequired["PaymentIntent.PaymentMethodType"]
        id_at_gateway: NotRequired[str]
        error_code: NotRequired[str]
        error_text: NotRequired[str]
        checkout_details: NotRequired[str]
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

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_intents"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("payment_intents", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("payment_intents", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )
