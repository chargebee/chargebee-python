from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import third_party_payment_method, customer


@dataclass
class CardResponse(Model):
    raw_data: Dict[Any, Any] = None
    payment_source_id: str = None
    status: str = None
    gateway: str = None
    gateway_account_id: str = None
    ref_tx_id: str = None
    first_name: str = None
    last_name: str = None
    iin: str = None
    last4: str = None
    card_type: str = None
    funding_type: str = None
    expiry_month: int = None
    expiry_year: int = None
    issuing_country: str = None
    billing_addr1: str = None
    billing_addr2: str = None
    billing_city: str = None
    billing_state_code: str = None
    billing_state: str = None
    billing_country: str = None
    billing_zip: str = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
    ip_address: str = None
    powered_by: str = None
    customer_id: str = None
    masked_number: str = None


@dataclass
class RetrieveResponse(Response):

    card: CardResponse


@dataclass
class UpdateCardForCustomerResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    card: CardResponse


@dataclass
class SwitchGatewayForCustomerResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
    card: CardResponse


@dataclass
class CopyCardForCustomerResponse(Response):
    is_idempotency_replayed: bool
    third_party_payment_method: (
        "third_party_payment_method.ThirdPartyPaymentMethodResponse"
    )


@dataclass
class DeleteCardForCustomerResponse(Response):
    is_idempotency_replayed: bool
    customer: "customer.CustomerResponse"
