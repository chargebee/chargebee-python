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
    subscription_estimate: "subscription_estimate.SubscriptionEstimatesResponse" = None
    subscription_estimates: List[
        "subscription_estimate.SubscriptionEstimatesResponse"
    ] = None
    invoice_estimate: "invoice_estimate.InvoiceEstimatesResponse" = None
    invoice_estimates: List["invoice_estimate.InvoiceEstimatesResponse"] = None
    payment_schedule_estimates: List[
        "payment_schedule_estimate.PaymentScheduleEstimateResponse"
    ] = None
    next_invoice_estimate: "invoice_estimate.InvoiceEstimatesResponse" = None
    credit_note_estimates: List["credit_note_estimate.CreditNoteEstimateResponse"] = (
        None
    )
    unbilled_charge_estimates: List["unbilled_charge.UnbilledChargeResponse"] = None


@dataclass
class CreateSubscriptionResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class CreateSubItemEstimateResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class CreateSubForCustomerEstimateResponse:
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class CreateSubItemForCustomerEstimateResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateSubscriptionResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class UpdateSubscriptionForItemsResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class RenewalEstimateResponse:
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class AdvanceInvoiceEstimateResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class RegenerateInvoiceEstimateResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class UpcomingInvoicesEstimateResponse:
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class ChangeTermEndResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class CancelSubscriptionResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class CancelSubscriptionForItemsResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class PauseSubscriptionResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class ResumeSubscriptionResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class GiftSubscriptionResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class GiftSubscriptionForItemsResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class CreateInvoiceResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class CreateInvoiceForItemsResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None


@dataclass
class PaymentSchedulesResponse(Response):
    estimate: EstimateResponse
    headers: Dict[str, str] = None
