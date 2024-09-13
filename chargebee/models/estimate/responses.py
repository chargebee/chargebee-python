from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.models import (
    payment_intent,
    contract_term,
    subscription_estimate,
    invoice_estimate,
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
    next_invoice_estimate: "invoice_estimate.InvoiceEstimatesResponse" = None
    credit_note_estimates: List["credit_note_estimate.CreditNoteEstimateResponse"] = (
        None
    )
    unbilled_charge_estimates: List["unbilled_charge.UnbilledChargeResponse"] = None


@dataclass
class CreateSubscriptionResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateSubItemEstimateResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateSubForCustomerEstimateResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateSubItemForCustomerEstimateResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateSubscriptionResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpdateSubscriptionForItemsResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RenewalEstimateResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class AdvanceInvoiceEstimateResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RegenerateInvoiceEstimateResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class UpcomingInvoicesEstimateResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ChangeTermEndResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CancelSubscriptionResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CancelSubscriptionForItemsResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class PauseSubscriptionResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ResumeSubscriptionResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class GiftSubscriptionResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class GiftSubscriptionForItemsResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateInvoiceResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class CreateInvoiceForItemsResponse:
    estimate: EstimateResponse
    response_headers: Dict[Any, Any] = None
