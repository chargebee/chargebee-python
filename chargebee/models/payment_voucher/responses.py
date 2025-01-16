from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class LinkedInvoiceResponse(Model):
    invoice_id: str = None
    txn_id: str = None
    applied_at: int = None


@dataclass
class PaymentVoucherResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    id_at_gateway: str = None
    payment_voucher_type: str = None
    expires_at: int = None
    status: str = None
    subscription_id: str = None
    currency_code: str = None
    amount: int = None
    gateway_account_id: str = None
    payment_source_id: str = None
    gateway: str = None
    payload: str = None
    error_code: str = None
    error_text: str = None
    url: str = None
    date: int = None
    resource_version: int = None
    updated_at: int = None
    customer_id: str = None
    linked_invoices: List[LinkedInvoiceResponse] = None


@dataclass
class CreateResponse(Response):
    payment_voucher: PaymentVoucherResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    payment_voucher: PaymentVoucherResponse
    headers: Dict[str, str] = None


@dataclass
class PaymentVouchersForInvoicePaymentVoucherResponse:
    payment_voucher: PaymentVoucherResponse


@dataclass
class PaymentVouchersForInvoiceResponse:
    list: List[PaymentVouchersForInvoicePaymentVoucherResponse]
    next_offset: str = None
    headers: Dict[str, str] = None


@dataclass
class PaymentVouchersForCustomerPaymentVoucherResponse:
    payment_voucher: PaymentVoucherResponse


@dataclass
class PaymentVouchersForCustomerResponse:
    list: List[PaymentVouchersForCustomerPaymentVoucherResponse]
    next_offset: str = None
    headers: Dict[str, str] = None
