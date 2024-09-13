from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums, contract_term


class Type(Enum):
    CHECKOUT_NEW = "checkout_new"
    CHECKOUT_EXISTING = "checkout_existing"
    UPDATE_PAYMENT_METHOD = "update_payment_method"
    MANAGE_PAYMENT_SOURCES = "manage_payment_sources"
    COLLECT_NOW = "collect_now"
    EXTEND_SUBSCRIPTION = "extend_subscription"
    CHECKOUT_ONE_TIME = "checkout_one_time"
    PRE_CANCEL = "pre_cancel"
    VIEW_VOUCHER = "view_voucher"
    CHECKOUT_GIFT = "checkout_gift"
    CLAIM_GIFT = "claim_gift"

    def __str__(self):
        return self.value


class State(Enum):
    CREATED = "created"
    REQUESTED = "requested"
    SUCCEEDED = "succeeded"
    CANCELLED = "cancelled"
    ACKNOWLEDGED = "acknowledged"

    def __str__(self):
        return self.value


class FailureReason(Enum):
    CARD_ERROR = "card_error"
    SERVER_ERROR = "server_error"

    def __str__(self):
        return self.value


class HostedPages(TypedDict):
    id: NotRequired[str]
    type: NotRequired[Type]
    url: NotRequired[str]
    state: NotRequired[State]
    failure_reason: NotRequired[FailureReason]
    pass_thru_content: NotRequired[str]
    embed: Required[bool]
    created_at: NotRequired[int]
    expires_at: NotRequired[int]
    content: Required[Dict[Any, Any]]
    updated_at: NotRequired[int]
    resource_version: NotRequired[int]
    checkout_info: NotRequired[Dict[Any, Any]]
    business_entity_id: NotRequired[str]


class CheckoutNewSubscriptionParams(TypedDict):
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
    auto_collection: NotRequired[enums.AutoCollection]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    invoice_notes: NotRequired[str]
    affiliate_token: NotRequired[str]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class CheckoutNewCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]
    taxability: NotRequired[enums.Taxability]
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    consolidated_invoicing: NotRequired[bool]


class CheckoutNewAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]


class CheckoutNewEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    service_period_in_days: NotRequired[int]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    charge_on: NotRequired[enums.ChargeOn]


class CheckoutNewCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class CheckoutNewBillingAddressParams(TypedDict):
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


class CheckoutNewShippingAddressParams(TypedDict):
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


class CheckoutNewContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class CheckoutOneTimeCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]
    taxability: NotRequired[enums.Taxability]
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    consolidated_invoicing: NotRequired[bool]


class CheckoutOneTimeAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class CheckoutOneTimeChargeParams(TypedDict):
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


class CheckoutOneTimeInvoiceParams(TypedDict):
    po_number: NotRequired[str]


class CheckoutOneTimeCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class CheckoutOneTimeBillingAddressParams(TypedDict):
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


class CheckoutOneTimeShippingAddressParams(TypedDict):
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


class CheckoutOneTimeForItemsCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]
    taxability: NotRequired[enums.Taxability]
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    einvoicing_method: NotRequired[enums.EinvoicingMethod]
    is_einvoice_enabled: NotRequired[bool]
    entity_identifier_scheme: NotRequired[str]
    entity_identifier_standard: NotRequired[str]
    consolidated_invoicing: NotRequired[bool]


class CheckoutOneTimeForItemsItemPriceParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class CheckoutOneTimeForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CheckoutOneTimeForItemsChargeParams(TypedDict):
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


class CheckoutOneTimeForItemsDiscountParams(TypedDict):
    percentage: NotRequired[float]
    amount: NotRequired[int]
    apply_on: Required[enums.ApplyOn]
    item_price_id: NotRequired[str]


class CheckoutOneTimeForItemsInvoiceParams(TypedDict):
    po_number: NotRequired[str]


class CheckoutOneTimeForItemsCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class CheckoutOneTimeForItemsEntityIdentifierParams(TypedDict):
    id: NotRequired[str]
    scheme: NotRequired[str]
    value: NotRequired[str]
    operation: NotRequired[enums.Operation]
    standard: NotRequired[str]


class CheckoutOneTimeForItemsBillingAddressParams(TypedDict):
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


class CheckoutOneTimeForItemsShippingAddressParams(TypedDict):
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


class CheckoutNewForItemsSubscriptionParams(TypedDict):
    id: NotRequired[str]
    trial_end: NotRequired[int]
    setup_fee: NotRequired[int]
    start_date: NotRequired[int]
    coupon: NotRequired[str]
    auto_collection: NotRequired[enums.AutoCollection]
    invoice_notes: NotRequired[str]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class CheckoutNewForItemsCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]
    taxability: NotRequired[enums.Taxability]
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    is_einvoice_enabled: NotRequired[bool]
    entity_identifier_scheme: NotRequired[str]
    entity_identifier_standard: NotRequired[str]
    einvoicing_method: NotRequired[enums.EinvoicingMethod]


class CheckoutNewForItemsSubscriptionItemParams(TypedDict):
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


class CheckoutNewForItemsDiscountParams(TypedDict):
    apply_on: Required[enums.ApplyOn]
    duration_type: Required[enums.DurationType]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: NotRequired[bool]
    item_price_id: NotRequired[str]


class CheckoutNewForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CheckoutNewForItemsCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class CheckoutNewForItemsEntityIdentifierParams(TypedDict):
    id: NotRequired[str]
    scheme: NotRequired[str]
    value: NotRequired[str]
    operation: NotRequired[enums.Operation]
    standard: NotRequired[str]


class CheckoutNewForItemsBillingAddressParams(TypedDict):
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


class CheckoutNewForItemsShippingAddressParams(TypedDict):
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


class CheckoutNewForItemsContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class CheckoutExistingSubscriptionParams(TypedDict):
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
    invoice_notes: NotRequired[str]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class CheckoutExistingAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    billing_cycles: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]


class CheckoutExistingEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    service_period_in_days: NotRequired[int]
    charge_on: NotRequired[enums.ChargeOn]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]


class CheckoutExistingCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]


class CheckoutExistingCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class CheckoutExistingContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class CheckoutExistingForItemsSubscriptionParams(TypedDict):
    id: Required[str]
    setup_fee: NotRequired[int]
    start_date: NotRequired[int]
    trial_end: NotRequired[int]
    coupon: NotRequired[str]
    auto_collection: NotRequired[enums.AutoCollection]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    invoice_notes: NotRequired[str]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class CheckoutExistingForItemsSubscriptionItemParams(TypedDict):
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


class CheckoutExistingForItemsDiscountParams(TypedDict):
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


class CheckoutExistingForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CheckoutExistingForItemsCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    is_einvoice_enabled: NotRequired[bool]
    entity_identifier_scheme: NotRequired[str]
    entity_identifier_standard: NotRequired[str]


class CheckoutExistingForItemsEntityIdentifierParams(TypedDict):
    id: NotRequired[str]
    scheme: NotRequired[str]
    value: NotRequired[str]
    operation: NotRequired[enums.Operation]
    standard: NotRequired[str]


class CheckoutExistingForItemsCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class CheckoutExistingForItemsContractTermParams(TypedDict):
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class UpdateCardCustomerParams(TypedDict):
    id: Required[str]
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]


class UpdateCardCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class UpdatePaymentMethodCustomerParams(TypedDict):
    id: Required[str]
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]


class UpdatePaymentMethodCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class ManagePaymentSourcesCustomerParams(TypedDict):
    id: Required[str]


class ManagePaymentSourcesCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class CollectNowCustomerParams(TypedDict):
    id: Required[str]


class CollectNowCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]


class AcceptQuoteQuoteParams(TypedDict):
    id: Required[str]


class ExtendSubscriptionSubscriptionParams(TypedDict):
    id: Required[str]


class CheckoutGiftGifterParams(TypedDict):
    customer_id: NotRequired[str]


class CheckoutGiftSubscriptionParams(TypedDict):
    plan_id: Required[str]
    plan_quantity: NotRequired[int]
    plan_quantity_in_decimal: NotRequired[str]
    coupon: NotRequired[str]


class CheckoutGiftAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]


class CheckoutGiftForItemsGifterParams(TypedDict):
    customer_id: NotRequired[str]


class CheckoutGiftForItemsSubscriptionItemParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]


class ClaimGiftGiftParams(TypedDict):
    id: Required[str]


class ClaimGiftCustomerParams(TypedDict):
    locale: NotRequired[str]


class PreCancelSubscriptionParams(TypedDict):
    id: Required[str]


class ViewVoucherPaymentVoucherParams(TypedDict):
    id: Required[str]


class ViewVoucherCustomerParams(TypedDict):
    locale: NotRequired[str]
