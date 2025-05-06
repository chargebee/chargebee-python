from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response
from chargebee.models import (
    unbilled_charge,
    payment_intent,
    invoice,
    card,
    advance_invoice_schedule,
    customer,
    card,
    invoice,
    unbilled_charge,
    credit_note,
    estimate,
    contract_term,
    payment_source,
    discount,
)


@dataclass
class SubscriptionItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    item_type: str = None
    quantity: int = None
    quantity_in_decimal: str = None
    metered_quantity: str = None
    last_calculated_at: int = None
    unit_price: int = None
    unit_price_in_decimal: str = None
    amount: int = None
    current_term_start: int = None
    current_term_end: int = None
    next_billing_at: int = None
    amount_in_decimal: str = None
    billing_period: int = None
    billing_period_unit: str = None
    free_quantity: int = None
    free_quantity_in_decimal: str = None
    trial_end: int = None
    billing_cycles: int = None
    service_period_days: int = None
    charge_on_event: str = None
    charge_once: bool = None
    charge_on_option: str = None
    proration_type: str = None
    usage_accumulation_reset_frequency: str = None


@dataclass
class ItemTierResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    starting_unit: int = None
    ending_unit: int = None
    price: int = None
    starting_unit_in_decimal: str = None
    ending_unit_in_decimal: str = None
    price_in_decimal: str = None
    pricing_type: str = None
    package_size: int = None
    index: int = None


@dataclass
class ChargedItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    item_price_id: str = None
    last_charged_at: int = None


@dataclass
class CouponResponse(Model):
    raw_data: Dict[Any, Any] = None
    coupon_id: str = None
    apply_till: int = None
    applied_count: int = None
    coupon_code: str = None


@dataclass
class ShippingAddressResponse(Model):
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
    index: int = None


@dataclass
class ReferralInfoResponse(Model):
    raw_data: Dict[Any, Any] = None
    referral_code: str = None
    coupon_code: str = None
    referrer_id: str = None
    external_reference_id: str = None
    reward_status: str = None
    referral_system: str = None
    account_id: str = None
    campaign_id: str = None
    external_campaign_id: str = None
    friend_offer_type: str = None
    referrer_reward_type: str = None
    notify_referral_system: str = None
    destination_url: str = None
    post_purchase_widget_enabled: bool = None


@dataclass
class BillingOverrideResponse(Model):
    raw_data: Dict[Any, Any] = None
    max_excess_payment_usage: int = None
    max_refundable_credits_usage: int = None


@dataclass
class ContractTermResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    status: str = None
    contract_start: int = None
    contract_end: int = None
    billing_cycle: int = None
    action_at_term_end: str = None
    total_contract_value: int = None
    total_contract_value_before_tax: int = None
    cancellation_cutoff_period: int = None
    created_at: int = None
    subscription_id: str = None
    remaining_billing_cycles: int = None


@dataclass
class DiscountResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    invoice_name: str = None
    type: str = None
    percentage: float = None
    amount: int = None
    currency_code: str = None
    duration_type: str = None
    period: int = None
    period_unit: str = None
    included_in_mrr: bool = None
    apply_on: str = None
    item_price_id: str = None
    created_at: int = None
    apply_till: int = None
    applied_count: int = None
    coupon_id: str = None
    index: int = None


@dataclass
class AddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    quantity: int = None
    unit_price: int = None
    amount: int = None
    trial_end: int = None
    remaining_billing_cycles: int = None
    quantity_in_decimal: str = None
    unit_price_in_decimal: str = None
    amount_in_decimal: str = None
    proration_type: str = None


@dataclass
class ChargedEventBasedAddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    last_charged_at: int = None


@dataclass
class EventBasedAddonResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    quantity: int = None
    unit_price: int = None
    service_period_in_days: int = None
    on_event: str = None
    charge_once: bool = None
    quantity_in_decimal: str = None
    unit_price_in_decimal: str = None


@dataclass
class SubscriptionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    currency_code: str = None
    plan_id: str = None
    plan_quantity: int = None
    plan_unit_price: int = None
    setup_fee: int = None
    billing_period: int = None
    billing_period_unit: str = None
    start_date: int = None
    trial_end: int = None
    remaining_billing_cycles: int = None
    po_number: str = None
    auto_collection: str = None
    plan_quantity_in_decimal: str = None
    plan_unit_price_in_decimal: str = None
    customer_id: str = None
    plan_amount: int = None
    plan_free_quantity: int = None
    status: str = None
    trial_start: int = None
    trial_end_action: str = None
    current_term_start: int = None
    current_term_end: int = None
    next_billing_at: int = None
    created_at: int = None
    started_at: int = None
    activated_at: int = None
    gift_id: str = None
    contract_term_billing_cycle_on_renewal: int = None
    override_relationship: bool = None
    pause_date: int = None
    resume_date: int = None
    cancelled_at: int = None
    cancel_reason: str = None
    affiliate_token: str = None
    created_from_ip: str = None
    resource_version: int = None
    updated_at: int = None
    has_scheduled_advance_invoices: bool = None
    has_scheduled_changes: bool = None
    payment_source_id: str = None
    plan_free_quantity_in_decimal: str = None
    plan_amount_in_decimal: str = None
    cancel_schedule_created_at: int = None
    offline_payment_method: str = None
    channel: str = None
    net_term_days: int = None
    active_id: str = None
    subscription_items: List[SubscriptionItemResponse] = None
    item_tiers: List[ItemTierResponse] = None
    charged_items: List[ChargedItemResponse] = None
    due_invoices_count: int = None
    due_since: int = None
    total_dues: int = None
    mrr: int = None
    arr: int = None
    exchange_rate: float = None
    base_currency_code: str = None
    addons: List[AddonResponse] = None
    event_based_addons: List[EventBasedAddonResponse] = None
    charged_event_based_addons: List[ChargedEventBasedAddonResponse] = None
    coupon: str = None
    coupons: List[CouponResponse] = None
    shipping_address: ShippingAddressResponse = None
    referral_info: ReferralInfoResponse = None
    billing_override: BillingOverrideResponse = None
    invoice_notes: str = None
    meta_data: Dict[Any, Any] = None
    deleted: bool = None
    changes_scheduled_at: int = None
    contract_term: ContractTermResponse = None
    cancel_reason_code: str = None
    free_period: int = None
    free_period_unit: str = None
    create_pending_invoices: bool = None
    auto_close_invoices: bool = None
    discounts: List[DiscountResponse] = None
    business_entity_id: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None


@dataclass
class CreateForCustomerResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None


@dataclass
class CreateWithItemsResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None


@dataclass
class ListSubscriptionResponse:
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None


@dataclass
class ListResponse(Response):

    list: List[ListSubscriptionResponse]
    next_offset: str = None


@dataclass
class SubscriptionsForCustomerSubscriptionResponse:
    subscription: SubscriptionResponse


@dataclass
class SubscriptionsForCustomerResponse(Response):

    list: List[SubscriptionsForCustomerSubscriptionResponse]
    next_offset: str = None


@dataclass
class ContractTermsForSubscriptionSubscriptionResponse:
    contract_term: "contract_term.ContractTermResponse"


@dataclass
class ContractTermsForSubscriptionResponse(Response):

    list: List[ContractTermsForSubscriptionSubscriptionResponse]
    next_offset: str = None


@dataclass
class ListDiscountsSubscriptionResponse:
    discount: "discount.DiscountResponse"


@dataclass
class ListDiscountsResponse(Response):

    list: List[ListDiscountsSubscriptionResponse]
    next_offset: str = None


@dataclass
class RetrieveResponse(Response):

    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None


@dataclass
class RetrieveWithScheduledChangesResponse(Response):

    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None


@dataclass
class RemoveScheduledChangesResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    credit_notes: List["credit_note.CreditNoteResponse"] = None


@dataclass
class RemoveScheduledCancellationResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None


@dataclass
class RemoveCouponsResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None


@dataclass
class UpdateResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None
    credit_notes: List["credit_note.CreditNoteResponse"] = None


@dataclass
class UpdateForItemsResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None
    credit_notes: List["credit_note.CreditNoteResponse"] = None


@dataclass
class ChangeTermEndResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None
    credit_notes: List["credit_note.CreditNoteResponse"] = None


@dataclass
class ReactivateResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None


@dataclass
class AddChargeAtTermEndResponse(Response):
    is_idempotency_replayed: bool
    estimate: "estimate.EstimateResponse"


@dataclass
class ChargeAddonAtTermEndResponse(Response):
    is_idempotency_replayed: bool
    estimate: "estimate.EstimateResponse"


@dataclass
class ChargeFutureRenewalsResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    advance_invoice_schedules: List[
        "advance_invoice_schedule.AdvanceInvoiceScheduleResponse"
    ] = None


@dataclass
class EditAdvanceInvoiceScheduleResponse(Response):
    is_idempotency_replayed: bool
    advance_invoice_schedules: List[
        "advance_invoice_schedule.AdvanceInvoiceScheduleResponse"
    ]


@dataclass
class RetrieveAdvanceInvoiceScheduleResponse(Response):

    advance_invoice_schedules: List[
        "advance_invoice_schedule.AdvanceInvoiceScheduleResponse"
    ]


@dataclass
class RemoveAdvanceInvoiceScheduleResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    advance_invoice_schedules: List[
        "advance_invoice_schedule.AdvanceInvoiceScheduleResponse"
    ] = None


@dataclass
class RegenerateInvoiceResponse(Response):
    is_idempotency_replayed: bool
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None


@dataclass
class ImportSubscriptionResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None


@dataclass
class ImportForCustomerResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None


@dataclass
class ImportContractTermResponse(Response):
    is_idempotency_replayed: bool
    contract_term: "contract_term.ContractTermResponse"


@dataclass
class ImportUnbilledChargesResponse(Response):
    is_idempotency_replayed: bool
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"]


@dataclass
class ImportForItemsResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None


@dataclass
class OverrideBillingProfileResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    payment_source: "payment_source.PaymentSourceResponse" = None


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None


@dataclass
class PauseResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None
    credit_notes: List["credit_note.CreditNoteResponse"] = None


@dataclass
class CancelResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None
    credit_notes: List["credit_note.CreditNoteResponse"] = None


@dataclass
class CancelForItemsResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None
    credit_notes: List["credit_note.CreditNoteResponse"] = None


@dataclass
class ResumeResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None
    invoice: "invoice.InvoiceResponse" = None
    unbilled_charges: List["unbilled_charge.UnbilledChargeResponse"] = None


@dataclass
class RemoveScheduledPauseResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None


@dataclass
class RemoveScheduledResumptionResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
    customer: "customer.CustomerResponse"
    card: "card.CardResponse" = None


@dataclass
class MoveResponse(Response):
    is_idempotency_replayed: bool
    subscription: SubscriptionResponse
