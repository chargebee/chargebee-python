from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import gateway_error_detail


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
    status: Required[PaymentAttemptStatus]
    payment_method_type: NotRequired[PaymentMethodType]
    id_at_gateway: NotRequired[str]
    error_code: NotRequired[str]
    error_text: NotRequired[str]
    created_at: Required[int]
    modified_at: Required[int]
    error_detail: NotRequired[gateway_error_detail.GatewayErrorDetailResponse]
