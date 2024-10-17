from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import (
    payment_intent,
    customer,
    third_party_payment_method,
    download,
)


@dataclass
class CardResponse(Model):
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
    last4: str = None
    first_name: str = None
    last_name: str = None
    email: str = None


@dataclass
class BillingAddressResponse(Model):
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
    email: str = None
    agreement_id: str = None


@dataclass
class UpiResponse(Model):
    vpa: str = None


@dataclass
class PaypalResponse(Model):
    email: str = None
    agreement_id: str = None


@dataclass
class VenmoResponse(Model):
    user_name: str = None


@dataclass
class KlarnaPayNowResponse(Model):
    email: str = None


@dataclass
class MandateResponse(Model):
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
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class CreateUsingPermanentTokenResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class CreateUsingTokenResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class CreateUsingPaymentIntentResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class CreateVoucherPaymentSourceResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class CreateCardResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class CreateBankAccountResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateCardResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateBankAccountResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class VerifyBankAccountResponse(Response):
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class ListPaymentSourceResponse:
    payment_source: PaymentSourceResponse


@dataclass
class ListResponse:
    list: List[ListPaymentSourceResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class SwitchGatewayAccountResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class ExportPaymentSourceResponse(Response):
    third_party_payment_method: (
        "third_party_payment_method.ThirdPartyPaymentMethodResponse"
    )
    headers: Dict[str, str] = None


@dataclass
class DeleteResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None


@dataclass
class DeleteLocalResponse(Response):
    customer: "customer.CustomerResponse"
    payment_source: PaymentSourceResponse
    headers: Dict[str, str] = None
