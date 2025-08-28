from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import (
    payment_intent,
    contract_term,
    subscription_estimate,
    invoice_estimate,
    payment_schedule_estimate,
    credit_note_estimate,
    unbilled_charge,
)


@dataclass
class EstimateResponse(Model):
    raw_data: Dict[Any, Any] = None
    created_at: int = None
    subscription_estimate: "subscription_estimate.SubscriptionEstimateResponse" = None
    subscription_estimates: List[
        "subscription_estimate.SubscriptionEstimateResponse"
    ] = None
    invoice_estimate: "invoice_estimate.InvoiceEstimateResponse" = None
    invoice_estimates: List["invoice_estimate.InvoiceEstimateResponse"] = None
    payment_schedule_estimates: List[
        "payment_schedule_estimate.PaymentScheduleEstimateResponse"
    ] = None
    next_invoice_estimate: "invoice_estimate.InvoiceEstimateResponse" = None
    credit_note_estimates: List["credit_note_estimate.CreditNoteEstimateResponse"] = (
        None
    )
    unbilled_charge_estimates: List["unbilled_charge.UnbilledChargeResponse"] = None


@dataclass
class CreateSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class CreateSubItemEstimateResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class CreateSubForCustomerEstimateResponse(Response):
    estimate: EstimateResponse


@dataclass
class CreateSubItemForCustomerEstimateResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class UpdateSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class UpdateSubscriptionForItemsResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class RenewalEstimateResponse(Response):
    estimate: EstimateResponse


@dataclass
class AdvanceInvoiceEstimateResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class RegenerateInvoiceEstimateResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class UpcomingInvoicesEstimateResponse(Response):
    estimate: EstimateResponse


@dataclass
class ChangeTermEndResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class CancelSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class CancelSubscriptionForItemsResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class PauseSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class ResumeSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class GiftSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class GiftSubscriptionForItemsResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class CreateInvoiceResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class CreateInvoiceForItemsResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse


@dataclass
class PaymentSchedulesResponse(Response):
    is_idempotency_replayed: bool
    estimate: EstimateResponse
