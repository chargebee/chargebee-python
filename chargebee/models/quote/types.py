from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums, contract_term


class Status(Enum):
    OPEN = "open"
    ACCEPTED = "accepted"
    DECLINED = "declined"
    INVOICED = "invoiced"
    CLOSED = "closed"

    def __str__(self):
        return self.value


class OperationType(Enum):
    CREATE_SUBSCRIPTION_FOR_CUSTOMER = "create_subscription_for_customer"
    CHANGE_SUBSCRIPTION = "change_subscription"
    ONETIME_INVOICE = "onetime_invoice"

    def __str__(self):
        return self.value


class LineItemEntityType(Enum):
    ADHOC = "adhoc"
    PLAN_ITEM_PRICE = "plan_item_price"
    ADDON_ITEM_PRICE = "addon_item_price"
    CHARGE_ITEM_PRICE = "charge_item_price"
    PLAN_SETUP = "plan_setup"
    PLAN = "plan"
    ADDON = "addon"

    def __str__(self):
        return self.value


class DiscountEntityType(Enum):
    ITEM_LEVEL_COUPON = "item_level_coupon"
    DOCUMENT_LEVEL_COUPON = "document_level_coupon"
    PROMOTIONAL_CREDITS = "promotional_credits"
    PRORATED_CREDITS = "prorated_credits"
    ITEM_LEVEL_DISCOUNT = "item_level_discount"
    DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

    def __str__(self):
        return self.value


class LineItemDiscountDiscountType(Enum):
    ITEM_LEVEL_COUPON = "item_level_coupon"
    DOCUMENT_LEVEL_COUPON = "document_level_coupon"
    PROMOTIONAL_CREDITS = "promotional_credits"
    PRORATED_CREDITS = "prorated_credits"
    ITEM_LEVEL_DISCOUNT = "item_level_discount"
    DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

    def __str__(self):
        return self.value


class LineItem(TypedDict):
    id: NotRequired[str]
    subscription_id: NotRequired[str]
    date_from: Required[int]
    date_to: Required[int]
    unit_amount: Required[int]
    quantity: NotRequired[int]
    amount: NotRequired[int]
    pricing_model: NotRequired[enums.PricingModel]
    is_taxed: Required[bool]
    tax_amount: NotRequired[int]
    tax_rate: NotRequired[float]
    unit_amount_in_decimal: NotRequired[str]
    quantity_in_decimal: NotRequired[str]
    amount_in_decimal: NotRequired[str]
    discount_amount: NotRequired[int]
    item_level_discount_amount: NotRequired[int]
    usage_percentage: NotRequired[str]
    reference_line_item_id: NotRequired[str]
    description: Required[str]
    entity_description: NotRequired[str]
    entity_type: Required[LineItemEntityType]
    tax_exempt_reason: NotRequired[enums.TaxExemptReason]
    entity_id: NotRequired[str]
    customer_id: NotRequired[str]


class Discount(TypedDict):
    amount: Required[int]
    description: NotRequired[str]
    entity_type: Required[DiscountEntityType]
    entity_id: NotRequired[str]
    coupon_set_code: NotRequired[str]


class LineItemDiscount(TypedDict):
    line_item_id: Required[str]
    discount_type: Required[LineItemDiscountDiscountType]
    coupon_id: NotRequired[str]
    entity_id: NotRequired[str]
    discount_amount: Required[int]


class Tax(TypedDict):
    name: Required[str]
    amount: Required[int]
    description: NotRequired[str]


class LineItemTax(TypedDict):
    line_item_id: NotRequired[str]
    tax_name: Required[str]
    tax_rate: Required[float]
    date_to: NotRequired[int]
    date_from: NotRequired[int]
    prorated_taxable_amount: NotRequired[float]
    is_partial_tax_applied: NotRequired[bool]
    is_non_compliance_tax: NotRequired[bool]
    taxable_amount: Required[int]
    tax_amount: Required[int]
    tax_juris_type: NotRequired[enums.TaxJurisType]
    tax_juris_name: NotRequired[str]
    tax_juris_code: NotRequired[str]
    tax_amount_in_local_currency: NotRequired[int]
    local_currency_code: NotRequired[str]


class LineItemTier(TypedDict):
    line_item_id: NotRequired[str]
    starting_unit: Required[int]
    ending_unit: NotRequired[int]
    quantity_used: Required[int]
    unit_amount: Required[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    quantity_used_in_decimal: NotRequired[str]
    unit_amount_in_decimal: NotRequired[str]


class ShippingAddress(TypedDict):
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
    country: NotRequired[str]
    zip: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]
    index: Required[int]


class BillingAddress(TypedDict):
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
    country: NotRequired[str]
    zip: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class Quotes(TypedDict):
    id: Required[str]
    name: NotRequired[str]
    po_number: NotRequired[str]
    customer_id: Required[str]
    subscription_id: NotRequired[str]
    invoice_id: NotRequired[str]
    status: Required[Status]
    operation_type: Required[OperationType]
    vat_number: NotRequired[str]
    price_type: Required[enums.PriceType]
    valid_till: Required[int]
    date: Required[int]
    total_payable: NotRequired[int]
    charge_on_acceptance: NotRequired[int]
    sub_total: Required[int]
    total: NotRequired[int]
    credits_applied: NotRequired[int]
    amount_paid: NotRequired[int]
    amount_due: NotRequired[int]
    version: NotRequired[int]
    resource_version: NotRequired[int]
    updated_at: NotRequired[int]
    vat_number_prefix: NotRequired[str]
    line_items: NotRequired[List[LineItem]]
    discounts: NotRequired[List[Discount]]
    line_item_discounts: NotRequired[List[LineItemDiscount]]
    taxes: NotRequired[List[Tax]]
    line_item_taxes: NotRequired[List[LineItemTax]]
    line_item_tiers: NotRequired[List[LineItemTier]]
    tax_category: NotRequired[str]
    currency_code: Required[str]
    notes: NotRequired[List[Dict[Any, Any]]]
    shipping_address: NotRequired[ShippingAddress]
    billing_address: NotRequired[BillingAddress]
    contract_term_start: NotRequired[int]
    contract_term_end: NotRequired[int]
    contract_term_termination_fee: NotRequired[int]
    business_entity_id: NotRequired[str]


class CreateSubForCustomerQuoteSubscriptionParams(TypedDict):
    id: NotRequired[str]
    po_number: NotRequired[str]
    plan_id: Required[str]
    plan_quantity: NotRequired[int]
    plan_quantity_in_decimal: NotRequired[str]
    plan_unit_price: NotRequired[int]
    plan_unit_price_in_decimal: NotRequired[str]
    setup_fee: NotRequired[int]
    trial_end: NotRequired[int]
    start_date: NotRequired[int]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class CreateSubForCustomerQuoteAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    trial_end: NotRequired[int]


class CreateSubForCustomerQuoteEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    service_period_in_days: NotRequired[int]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    charge_on: NotRequired[enums.ChargeOn]


class CreateSubForCustomerQuoteShippingAddressParams(TypedDict):
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


class CreateSubForCustomerQuoteContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class EditCreateSubForCustomerQuoteSubscriptionParams(TypedDict):
    id: NotRequired[str]
    po_number: NotRequired[str]
    plan_id: Required[str]
    plan_quantity: NotRequired[int]
    plan_quantity_in_decimal: NotRequired[str]
    plan_unit_price: NotRequired[int]
    plan_unit_price_in_decimal: NotRequired[str]
    setup_fee: NotRequired[int]
    trial_end: NotRequired[int]
    start_date: NotRequired[int]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class EditCreateSubForCustomerQuoteAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    trial_end: NotRequired[int]


class EditCreateSubForCustomerQuoteEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    service_period_in_days: NotRequired[int]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    charge_on: NotRequired[enums.ChargeOn]


class EditCreateSubForCustomerQuoteShippingAddressParams(TypedDict):
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


class EditCreateSubForCustomerQuoteContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class UpdateSubscriptionQuoteSubscriptionParams(TypedDict):
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
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class UpdateSubscriptionQuoteAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    billing_cycles: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    trial_end: NotRequired[int]


class UpdateSubscriptionQuoteEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    service_period_in_days: NotRequired[int]
    charge_on: NotRequired[enums.ChargeOn]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]


class UpdateSubscriptionQuoteBillingAddressParams(TypedDict):
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


class UpdateSubscriptionQuoteShippingAddressParams(TypedDict):
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


class UpdateSubscriptionQuoteCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    registered_for_gst: NotRequired[bool]


class UpdateSubscriptionQuoteContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class EditUpdateSubscriptionQuoteSubscriptionParams(TypedDict):
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
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class EditUpdateSubscriptionQuoteAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    billing_cycles: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    trial_end: NotRequired[int]


class EditUpdateSubscriptionQuoteEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    service_period_in_days: NotRequired[int]
    charge_on: NotRequired[enums.ChargeOn]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]


class EditUpdateSubscriptionQuoteBillingAddressParams(TypedDict):
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


class EditUpdateSubscriptionQuoteShippingAddressParams(TypedDict):
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


class EditUpdateSubscriptionQuoteCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    registered_for_gst: NotRequired[bool]


class EditUpdateSubscriptionQuoteContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class CreateForOnetimeChargesAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    service_period: NotRequired[int]


class CreateForOnetimeChargesChargeParams(TypedDict):
    amount: NotRequired[int]
    amount_in_decimal: NotRequired[str]
    description: NotRequired[str]
    avalara_sale_type: NotRequired[enums.AvalaraSaleType]
    avalara_transaction_type: NotRequired[int]
    avalara_service_type: NotRequired[int]
    service_period: NotRequired[int]


class CreateForOnetimeChargesShippingAddressParams(TypedDict):
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


class CreateForOnetimeChargesTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class EditOneTimeQuoteAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    service_period: NotRequired[int]


class EditOneTimeQuoteChargeParams(TypedDict):
    amount: NotRequired[int]
    amount_in_decimal: NotRequired[str]
    description: NotRequired[str]
    avalara_sale_type: NotRequired[enums.AvalaraSaleType]
    avalara_transaction_type: NotRequired[int]
    avalara_service_type: NotRequired[int]
    service_period: NotRequired[int]


class EditOneTimeQuoteShippingAddressParams(TypedDict):
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


class EditOneTimeQuoteTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class CreateSubItemsForCustomerQuoteSubscriptionParams(TypedDict):
    id: NotRequired[str]
    po_number: NotRequired[str]
    trial_end: NotRequired[int]
    setup_fee: NotRequired[int]
    start_date: NotRequired[int]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class CreateSubItemsForCustomerQuoteSubscriptionItemParams(TypedDict):
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


class CreateSubItemsForCustomerQuoteDiscountParams(TypedDict):
    apply_on: Required[enums.ApplyOn]
    duration_type: Required[enums.DurationType]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: NotRequired[bool]
    item_price_id: NotRequired[str]


class CreateSubItemsForCustomerQuoteItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CreateSubItemsForCustomerQuoteShippingAddressParams(TypedDict):
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


class CreateSubItemsForCustomerQuoteContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class EditCreateSubCustomerQuoteForItemsSubscriptionParams(TypedDict):
    id: NotRequired[str]
    po_number: NotRequired[str]
    trial_end: NotRequired[int]
    setup_fee: NotRequired[int]
    start_date: NotRequired[int]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class EditCreateSubCustomerQuoteForItemsSubscriptionItemParams(TypedDict):
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


class EditCreateSubCustomerQuoteForItemsDiscountParams(TypedDict):
    apply_on: Required[enums.ApplyOn]
    duration_type: Required[enums.DurationType]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: NotRequired[bool]
    item_price_id: NotRequired[str]


class EditCreateSubCustomerQuoteForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class EditCreateSubCustomerQuoteForItemsShippingAddressParams(TypedDict):
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


class EditCreateSubCustomerQuoteForItemsContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class UpdateSubscriptionQuoteForItemsSubscriptionParams(TypedDict):
    id: Required[str]
    setup_fee: NotRequired[int]
    start_date: NotRequired[int]
    trial_end: NotRequired[int]
    coupon: NotRequired[str]
    auto_collection: NotRequired[enums.AutoCollection]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class UpdateSubscriptionQuoteForItemsSubscriptionItemParams(TypedDict):
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


class UpdateSubscriptionQuoteForItemsDiscountParams(TypedDict):
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


class UpdateSubscriptionQuoteForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class UpdateSubscriptionQuoteForItemsBillingAddressParams(TypedDict):
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


class UpdateSubscriptionQuoteForItemsShippingAddressParams(TypedDict):
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


class UpdateSubscriptionQuoteForItemsCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    registered_for_gst: NotRequired[bool]


class UpdateSubscriptionQuoteForItemsContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class EditUpdateSubscriptionQuoteForItemsSubscriptionItemParams(TypedDict):
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


class EditUpdateSubscriptionQuoteForItemsSubscriptionParams(TypedDict):
    setup_fee: NotRequired[int]
    start_date: NotRequired[int]
    trial_end: NotRequired[int]
    coupon: NotRequired[str]
    auto_collection: NotRequired[enums.AutoCollection]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class EditUpdateSubscriptionQuoteForItemsDiscountParams(TypedDict):
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


class EditUpdateSubscriptionQuoteForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class EditUpdateSubscriptionQuoteForItemsBillingAddressParams(TypedDict):
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


class EditUpdateSubscriptionQuoteForItemsShippingAddressParams(TypedDict):
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


class EditUpdateSubscriptionQuoteForItemsCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    registered_for_gst: NotRequired[bool]


class EditUpdateSubscriptionQuoteForItemsContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class CreateForChargeItemsAndChargesItemPriceParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    service_period_days: NotRequired[int]


class CreateForChargeItemsAndChargesItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CreateForChargeItemsAndChargesChargeParams(TypedDict):
    amount: NotRequired[int]
    amount_in_decimal: NotRequired[str]
    description: NotRequired[str]
    avalara_sale_type: NotRequired[enums.AvalaraSaleType]
    avalara_transaction_type: NotRequired[int]
    avalara_service_type: NotRequired[int]
    service_period: NotRequired[int]


class CreateForChargeItemsAndChargesShippingAddressParams(TypedDict):
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


class CreateForChargeItemsAndChargesDiscountParams(TypedDict):
    percentage: NotRequired[float]
    amount: NotRequired[int]
    apply_on: Required[enums.ApplyOn]
    item_price_id: NotRequired[str]


class CreateForChargeItemsAndChargesTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class EditForChargeItemsAndChargesItemPriceParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    service_period_days: NotRequired[int]


class EditForChargeItemsAndChargesItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class EditForChargeItemsAndChargesChargeParams(TypedDict):
    amount: NotRequired[int]
    amount_in_decimal: NotRequired[str]
    description: NotRequired[str]
    avalara_sale_type: NotRequired[enums.AvalaraSaleType]
    avalara_transaction_type: NotRequired[int]
    avalara_service_type: NotRequired[int]
    service_period: NotRequired[int]


class EditForChargeItemsAndChargesShippingAddressParams(TypedDict):
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


class EditForChargeItemsAndChargesDiscountParams(TypedDict):
    percentage: NotRequired[float]
    amount: NotRequired[int]
    apply_on: Required[enums.ApplyOn]
    item_price_id: NotRequired[str]


class EditForChargeItemsAndChargesTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class ConvertSubscriptionParams(TypedDict):
    id: NotRequired[str]
    auto_collection: NotRequired[enums.AutoCollection]
    po_number: NotRequired[str]
    auto_close_invoices: NotRequired[bool]
