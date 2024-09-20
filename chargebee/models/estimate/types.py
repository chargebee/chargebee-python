from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import (
    enums,
    payment_intent,
    contract_term,
    subscription_estimate,
    invoice_estimate,
    credit_note_estimate,
    unbilled_charge,
)


class UnbilledChargeEntityType(Enum):
    ADHOC = "adhoc"
    PLAN_ITEM_PRICE = "plan_item_price"
    ADDON_ITEM_PRICE = "addon_item_price"
    CHARGE_ITEM_PRICE = "charge_item_price"
    PLAN_SETUP = "plan_setup"
    PLAN = "plan"
    ADDON = "addon"

    def __str__(self):
        return self.value


class CreateSubscriptionSubscriptionParams(TypedDict):
    id: NotRequired[str]
    plan_id: Required[str]
    plan_quantity: NotRequired[int]
    plan_quantity_in_decimal: NotRequired[str]
    plan_unit_price: NotRequired[int]
    plan_unit_price_in_decimal: NotRequired[str]
    setup_fee: NotRequired[int]
    trial_end: NotRequired[int]
    start_date: NotRequired[int]
    coupon: NotRequired[str]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    free_period: NotRequired[int]
    free_period_unit: NotRequired[enums.FreePeriodUnit]
    contract_term_billing_cycle_on_renewal: NotRequired[int]
    trial_end_action: NotRequired[enums.TrialEndAction]


class CreateSubscriptionAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    trial_end: NotRequired[int]


class CreateSubscriptionEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    service_period_in_days: NotRequired[int]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    charge_on: NotRequired[enums.ChargeOn]


class CreateSubscriptionBillingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateSubscriptionShippingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateSubscriptionCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    registered_for_gst: NotRequired[bool]
    taxability: NotRequired[enums.Taxability]
    entity_code: NotRequired[enums.EntityCode]
    exempt_number: NotRequired[str]
    exemption_details: NotRequired[List[Dict[Any, Any]]]
    customer_type: NotRequired[enums.CustomerType]


class CreateSubscriptionContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class CreateSubscriptionTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class CreateSubItemEstimateSubscriptionParams(TypedDict):
    id: NotRequired[str]
    trial_end: NotRequired[int]
    setup_fee: NotRequired[int]
    start_date: NotRequired[int]
    coupon: NotRequired[str]
    free_period: NotRequired[int]
    free_period_unit: NotRequired[enums.FreePeriodUnit]
    contract_term_billing_cycle_on_renewal: NotRequired[int]
    trial_end_action: NotRequired[enums.TrialEndAction]


class CreateSubItemEstimateSubscriptionItemParams(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    trial_end: NotRequired[int]
    service_period_days: NotRequired[int]
    charge_on_event: NotRequired[enums.ChargeOnEvent]
    charge_once: NotRequired[bool]
    item_type: NotRequired[enums.ItemType]
    charge_on_option: NotRequired[enums.ChargeOnOption]


class CreateSubItemEstimateDiscountParams(TypedDict):
    apply_on: Required[enums.ApplyOn]
    duration_type: Required[enums.DurationType]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: NotRequired[bool]
    item_price_id: NotRequired[str]


class CreateSubItemEstimateItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CreateSubItemEstimateBillingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateSubItemEstimateShippingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateSubItemEstimateCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    registered_for_gst: NotRequired[bool]
    taxability: NotRequired[enums.Taxability]
    entity_code: NotRequired[enums.EntityCode]
    exempt_number: NotRequired[str]
    exemption_details: NotRequired[List[Dict[Any, Any]]]
    customer_type: NotRequired[enums.CustomerType]


class CreateSubItemEstimateContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    contract_start: NotRequired[int]
    cancellation_cutoff_period: NotRequired[int]


class CreateSubItemEstimateTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class CreateSubForCustomerEstimateSubscriptionParams(TypedDict):
    id: NotRequired[str]
    plan_id: Required[str]
    plan_quantity: NotRequired[int]
    plan_quantity_in_decimal: NotRequired[str]
    plan_unit_price: NotRequired[int]
    plan_unit_price_in_decimal: NotRequired[str]
    setup_fee: NotRequired[int]
    trial_end: NotRequired[int]
    start_date: NotRequired[int]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    free_period: NotRequired[int]
    free_period_unit: NotRequired[enums.FreePeriodUnit]
    contract_term_billing_cycle_on_renewal: NotRequired[int]
    trial_end_action: NotRequired[enums.TrialEndAction]


class CreateSubForCustomerEstimateAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    trial_end: NotRequired[int]


class CreateSubForCustomerEstimateEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    service_period_in_days: NotRequired[int]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    charge_on: NotRequired[enums.ChargeOn]


class CreateSubForCustomerEstimateShippingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateSubForCustomerEstimateContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class CreateSubItemForCustomerEstimateSubscriptionParams(TypedDict):
    id: NotRequired[str]
    trial_end: NotRequired[int]
    setup_fee: NotRequired[int]
    start_date: NotRequired[int]
    free_period: NotRequired[int]
    free_period_unit: NotRequired[enums.FreePeriodUnit]
    contract_term_billing_cycle_on_renewal: NotRequired[int]
    trial_end_action: NotRequired[enums.TrialEndAction]


class CreateSubItemForCustomerEstimateSubscriptionItemParams(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    trial_end: NotRequired[int]
    service_period_days: NotRequired[int]
    charge_on_event: NotRequired[enums.ChargeOnEvent]
    charge_once: NotRequired[bool]
    item_type: NotRequired[enums.ItemType]
    charge_on_option: NotRequired[enums.ChargeOnOption]


class CreateSubItemForCustomerEstimateDiscountParams(TypedDict):
    apply_on: Required[enums.ApplyOn]
    duration_type: Required[enums.DurationType]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: NotRequired[bool]
    item_price_id: NotRequired[str]


class CreateSubItemForCustomerEstimateItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CreateSubItemForCustomerEstimateShippingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateSubItemForCustomerEstimateBillingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateSubItemForCustomerEstimateContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    contract_start: NotRequired[int]
    cancellation_cutoff_period: NotRequired[int]


class UpdateSubscriptionSubscriptionParams(TypedDict):
    id: Required[str]
    plan_id: NotRequired[str]
    plan_quantity: NotRequired[int]
    plan_unit_price: NotRequired[int]
    setup_fee: NotRequired[int]
    plan_quantity_in_decimal: NotRequired[str]
    plan_unit_price_in_decimal: NotRequired[str]
    start_date: NotRequired[int]
    trial_end: NotRequired[int]
    coupon: NotRequired[str]
    auto_collection: NotRequired[enums.AutoCollection]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    free_period: NotRequired[int]
    free_period_unit: NotRequired[enums.FreePeriodUnit]
    trial_end_action: NotRequired[enums.TrialEndAction]


class UpdateSubscriptionAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    billing_cycles: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    trial_end: NotRequired[int]
    proration_type: NotRequired[enums.ProrationType]


class UpdateSubscriptionEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    service_period_in_days: NotRequired[int]
    charge_on: NotRequired[enums.ChargeOn]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]


class UpdateSubscriptionBillingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class UpdateSubscriptionShippingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class UpdateSubscriptionCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    registered_for_gst: NotRequired[bool]
    taxability: NotRequired[enums.Taxability]


class UpdateSubscriptionForItemsSubscriptionParams(TypedDict):
    id: Required[str]
    setup_fee: NotRequired[int]
    start_date: NotRequired[int]
    trial_end: NotRequired[int]
    coupon: NotRequired[str]
    auto_collection: NotRequired[enums.AutoCollection]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    free_period: NotRequired[int]
    free_period_unit: NotRequired[enums.FreePeriodUnit]
    trial_end_action: NotRequired[enums.TrialEndAction]


class UpdateSubscriptionForItemsSubscriptionItemParams(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    trial_end: NotRequired[int]
    service_period_days: NotRequired[int]
    charge_on_event: NotRequired[enums.ChargeOnEvent]
    charge_once: NotRequired[bool]
    charge_on_option: NotRequired[enums.ChargeOnOption]
    item_type: NotRequired[enums.ItemType]
    proration_type: NotRequired[enums.ProrationType]


class UpdateSubscriptionForItemsDiscountParams(TypedDict):
    apply_on: Required[enums.ApplyOn]
    duration_type: Required[enums.DurationType]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: NotRequired[bool]
    item_price_id: NotRequired[str]
    operation_type: Required[enums.OperationType]
    id: NotRequired[str]


class UpdateSubscriptionForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class UpdateSubscriptionForItemsBillingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class UpdateSubscriptionForItemsShippingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class UpdateSubscriptionForItemsCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    registered_for_gst: NotRequired[bool]
    taxability: NotRequired[enums.Taxability]


class AdvanceInvoiceEstimateSpecificDatesScheduleParams(TypedDict):
    terms_to_charge: NotRequired[int]
    date: NotRequired[int]


class AdvanceInvoiceEstimateFixedIntervalScheduleParams(TypedDict):
    number_of_occurrences: NotRequired[int]
    days_before_renewal: NotRequired[int]
    end_schedule_on: NotRequired[enums.EndScheduleOn]
    end_date: NotRequired[int]


class CancelSubscriptionEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    service_period_in_days: NotRequired[int]


class CancelSubscriptionForItemsSubscriptionItemParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    service_period_days: NotRequired[int]


class PauseSubscriptionSubscriptionParams(TypedDict):
    pause_date: NotRequired[int]
    resume_date: NotRequired[int]
    skip_billing_cycles: NotRequired[int]


class ResumeSubscriptionSubscriptionParams(TypedDict):
    resume_date: NotRequired[int]


class GiftSubscriptionGiftParams(TypedDict):
    scheduled_at: NotRequired[int]
    auto_claim: NotRequired[bool]
    no_expiry: NotRequired[bool]
    claim_expiry_date: NotRequired[int]


class GiftSubscriptionGifterParams(TypedDict):
    customer_id: Required[str]
    signature: Required[str]
    note: NotRequired[str]
    payment_src_id: NotRequired[str]


class GiftSubscriptionGiftReceiverParams(TypedDict):
    customer_id: Required[str]
    first_name: Required[str]
    last_name: Required[str]
    email: Required[str]


class GiftSubscriptionPaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class GiftSubscriptionShippingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class GiftSubscriptionSubscriptionParams(TypedDict):
    plan_id: Required[str]
    plan_quantity: NotRequired[int]
    plan_quantity_in_decimal: NotRequired[str]


class GiftSubscriptionAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]


class GiftSubscriptionForItemsGiftParams(TypedDict):
    scheduled_at: NotRequired[int]
    auto_claim: NotRequired[bool]
    no_expiry: NotRequired[bool]
    claim_expiry_date: NotRequired[int]


class GiftSubscriptionForItemsGifterParams(TypedDict):
    customer_id: Required[str]
    signature: Required[str]
    note: NotRequired[str]
    payment_src_id: NotRequired[str]


class GiftSubscriptionForItemsGiftReceiverParams(TypedDict):
    customer_id: Required[str]
    first_name: Required[str]
    last_name: Required[str]
    email: Required[str]


class GiftSubscriptionForItemsPaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class GiftSubscriptionForItemsShippingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class GiftSubscriptionForItemsSubscriptionItemParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]


class CreateInvoiceInvoiceParams(TypedDict):
    customer_id: NotRequired[str]
    subscription_id: NotRequired[str]
    po_number: NotRequired[str]


class CreateInvoiceAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class CreateInvoiceChargeParams(TypedDict):
    amount: NotRequired[int]
    amount_in_decimal: NotRequired[str]
    description: NotRequired[str]
    taxable: NotRequired[bool]
    tax_profile_id: NotRequired[str]
    avalara_tax_code: NotRequired[str]
    hsn_code: NotRequired[str]
    taxjar_product_code: NotRequired[str]
    avalara_sale_type: NotRequired[enums.AvalaraSaleType]
    avalara_transaction_type: NotRequired[int]
    avalara_service_type: NotRequired[int]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class CreateInvoiceNotesToRemoveParams(TypedDict):
    entity_type: NotRequired[enums.EntityType]
    entity_id: NotRequired[str]


class CreateInvoiceShippingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateInvoiceTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class CreateInvoiceForItemsInvoiceParams(TypedDict):
    customer_id: NotRequired[str]
    subscription_id: NotRequired[str]
    po_number: NotRequired[str]


class CreateInvoiceForItemsItemPriceParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class CreateInvoiceForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CreateInvoiceForItemsChargeParams(TypedDict):
    amount: NotRequired[int]
    amount_in_decimal: NotRequired[str]
    description: NotRequired[str]
    taxable: NotRequired[bool]
    tax_profile_id: NotRequired[str]
    avalara_tax_code: NotRequired[str]
    hsn_code: NotRequired[str]
    taxjar_product_code: NotRequired[str]
    avalara_sale_type: NotRequired[enums.AvalaraSaleType]
    avalara_transaction_type: NotRequired[int]
    avalara_service_type: NotRequired[int]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class CreateInvoiceForItemsNotesToRemoveParams(TypedDict):
    entity_type: NotRequired[enums.EntityType]
    entity_id: NotRequired[str]


class CreateInvoiceForItemsDiscountParams(TypedDict):
    percentage: NotRequired[float]
    amount: NotRequired[int]
    apply_on: Required[enums.ApplyOn]
    item_price_id: NotRequired[str]


class CreateInvoiceForItemsShippingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateInvoiceForItemsTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]
