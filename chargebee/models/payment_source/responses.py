from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import (
    payment_intent,
    card,
    customer,
    third_party_payment_method,
    download,
)


@dataclass
class CardResponse(Model):
    raw_data: Dict[Any, Any] = None
    first_name: str = None
    last_name: str = None
    iin: str = None
    last4: str = None
    brand: str = None
    funding_type: str = None
    expiry_month: int = None
    expiry_year: int = None
    billing_addr1: str = None
    billing_addr2: str = None
    billing_city: str = None
    billing_state_code: str = None
    billing_state: str = None
    billing_country: str = None
    billing_zip: str = None
    masked_number: str = None


@dataclass
class BankAccountResponse(Model):
    raw_data: Dict[Any, Any] = None
    last4: str = None
    name_on_account: str = None
    first_name: str = None
    last_name: str = None
    direct_debit_scheme: str = None
    bank_name: str = None
    mandate_id: str = None
    account_type: str = None
    echeck_type: str = None
    account_holder_type: str = None
    email: str = None


@dataclass
class CustVoucherSourceResponse(Model):
    raw_data: Dict[Any, Any] = None
    last4: str = None
    first_name: str = None
    last_name: str = None
    email: str = None


@dataclass
class BillingAddressResponse(Model):
    raw_data: Dict[Any, Any] = None
    first_name: str = None
    last_name: str = None
    email: str = None
    company: str = None
    phone: str = None
    line1: str = None
    line2: str = None
    line3: str = None
    city: str = None
    state_code: str = None
    state: str = None
    country: str = None
    zip: str = None
    validation_status: str = None


@dataclass
class AmazonPaymentResponse(Model):
    raw_data: Dict[Any, Any] = None
    email: str = None
    agreement_id: str = None


@dataclass
class UpiResponse(Model):
    raw_data: Dict[Any, Any] = None
    vpa: str = None


@dataclass
class PaypalResponse(Model):
    raw_data: Dict[Any, Any] = None
    email: str = None
    agreement_id: str = None


@dataclass
class VenmoResponse(Model):
    raw_data: Dict[Any, Any] = None
    user_name: str = None


@dataclass
class KlarnaPayNowResponse(Model):
    raw_data: Dict[Any, Any] = None
    email: str = None


@dataclass
class MandateResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    subscription_id: str = None
    created_at: int = None


@dataclass
class PaymentSourceResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    resource_version: int = None
    updated_at: int = None
    created_at: int = None
    customer_id: str = None
    type: str = None
    reference_id: str = None
    status: str = None
    gateway: str = None
    gateway_account_id: str = None
    ip_address: str = None
    issuing_country: str = None
    card: CardResponse = None
    bank_account: BankAccountResponse = None
    boleto: CustVoucherSourceResponse = None
    billing_address: BillingAddressResponse = None
    amazon_payment: AmazonPaymentResponse = None
    upi: UpiResponse = None
    paypal: PaypalResponse = None
    venmo: VenmoResponse = None
    klarna_pay_now: KlarnaPayNowResponse = None
    mandates: List[MandateResponse] = None
    deleted: bool = None
    business_entity_id: str = None


@dataclass
class CreateUsingTempTokenResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class CreateUsingPermanentTokenResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class CreateUsingTokenResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class CreateUsingPaymentIntentResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class CreateVoucherPaymentSourceResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class CreateCardResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class CreateBankAccountResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class UpdateCardResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class UpdateBankAccountResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class VerifyBankAccountResponse(Response):
    is_idempotency_replayed: bool
    payment_source: PaymentSourceResponse


@dataclass
class RetrieveResponse(Response):
    payment_source: PaymentSourceResponse


@dataclass
class ListPaymentSourceResponse:
    payment_source: PaymentSourceResponse


@dataclass
class ListResponse(Response):
    list: List[ListPaymentSourceResponse]
    next_offset: str = None


@dataclass
class SwitchGatewayAccountResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class ExportPaymentSourceResponse(Response):
    is_idempotency_replayed: bool
    third_party_payment_method: (
        "third_party_payment_method.ThirdPartyPaymentMethodResponse"
    )


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse


@dataclass
class DeleteLocalResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
