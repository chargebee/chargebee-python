from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums, unbilled_charge, payment_intent, invoice


class Status(Enum):
    FUTURE = "future"
    IN_TRIAL = "in_trial"
    ACTIVE = "active"
    NON_RENEWING = "non_renewing"
    PAUSED = "paused"
    CANCELLED = "cancelled"
    TRANSFERRED = "transferred"

    def __str__(self):
        return self.value


class CancelReason(Enum):
    NOT_PAID = "not_paid"
    NO_CARD = "no_card"
    FRAUD_REVIEW_FAILED = "fraud_review_failed"
    NON_COMPLIANT_EU_CUSTOMER = "non_compliant_eu_customer"
    TAX_CALCULATION_FAILED = "tax_calculation_failed"
    CURRENCY_INCOMPATIBLE_WITH_GATEWAY = "currency_incompatible_with_gateway"
    NON_COMPLIANT_CUSTOMER = "non_compliant_customer"

    def __str__(self):
        return self.value


class BillingPeriodUnit(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def __str__(self):
        return self.value


class ReferralInfoRewardStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    INVALID = "invalid"

    def __str__(self):
        return self.value


class ContractTermStatus(Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    TERMINATED = "terminated"

    def __str__(self):
        return self.value


class ContractTermActionAtTermEnd(Enum):
    RENEW = "renew"
    EVERGREEN = "evergreen"
    CANCEL = "cancel"
    RENEW_ONCE = "renew_once"

    def __str__(self):
        return self.value


class DiscountType(Enum):
    FIXED_AMOUNT = "fixed_amount"
    PERCENTAGE = "percentage"

    def __str__(self):
        return self.value


class SubscriptionItem(TypedDict):
    item_price_id: Required[str]
    item_type: Required[enums.ItemType]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    metered_quantity: NotRequired[str]
    last_calculated_at: NotRequired[int]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    amount: NotRequired[int]
    amount_in_decimal: NotRequired[str]
    billing_period: NotRequired[int]
    billing_period_unit: NotRequired[BillingPeriodUnit]
    free_quantity: NotRequired[int]
    free_quantity_in_decimal: NotRequired[str]
    trial_end: NotRequired[int]
    billing_cycles: NotRequired[int]
    service_period_days: NotRequired[int]
    charge_on_event: NotRequired[enums.ChargeOnEvent]
    charge_once: NotRequired[bool]
    charge_on_option: NotRequired[enums.ChargeOnOption]
    proration_type: NotRequired[enums.ProrationType]


class ItemTier(TypedDict):
    item_price_id: Required[str]
    starting_unit: Required[int]
    ending_unit: NotRequired[int]
    price: Required[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]
    index: Required[int]


class ChargedItem(TypedDict):
    item_price_id: Required[str]
    last_charged_at: Required[int]


class Coupon(TypedDict):
    coupon_id: Required[str]
    apply_till: NotRequired[int]
    applied_count: Required[int]
    coupon_code: NotRequired[str]


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


class ReferralInfo(TypedDict):
    referral_code: NotRequired[str]
    coupon_code: NotRequired[str]
    referrer_id: NotRequired[str]
    external_reference_id: NotRequired[str]
    reward_status: NotRequired[ReferralInfoRewardStatus]
    referral_system: NotRequired[enums.ReferralSystem]
    account_id: Required[str]
    campaign_id: Required[str]
    external_campaign_id: NotRequired[str]
    friend_offer_type: NotRequired[enums.FriendOfferType]
    referrer_reward_type: NotRequired[enums.ReferrerRewardType]
    notify_referral_system: NotRequired[enums.NotifyReferralSystem]
    destination_url: NotRequired[str]
    post_purchase_widget_enabled: Required[bool]


class ContractTerm(TypedDict):
    id: Required[str]
    status: Required[ContractTermStatus]
    contract_start: Required[int]
    contract_end: Required[int]
    billing_cycle: Required[int]
    action_at_term_end: Required[ContractTermActionAtTermEnd]
    total_contract_value: Required[int]
    total_contract_value_before_tax: Required[int]
    cancellation_cutoff_period: NotRequired[int]
    created_at: Required[int]
    subscription_id: Required[str]
    remaining_billing_cycles: NotRequired[int]


class Discount(TypedDict):
    id: Required[str]
    invoice_name: NotRequired[str]
    type: Required[DiscountType]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    currency_code: NotRequired[str]
    duration_type: Required[enums.DurationType]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: Required[bool]
    apply_on: Required[enums.ApplyOn]
    item_price_id: NotRequired[str]
    created_at: Required[int]
    apply_till: NotRequired[int]
    applied_count: NotRequired[int]
    coupon_id: Required[str]
    index: Required[int]


class Addon(TypedDict):
    id: Required[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    amount: NotRequired[int]
    trial_end: NotRequired[int]
    remaining_billing_cycles: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    amount_in_decimal: NotRequired[str]
    proration_type: NotRequired[enums.ProrationType]


class ChargedEventBasedAddon(TypedDict):
    id: Required[str]
    last_charged_at: Required[int]


class EventBasedAddon(TypedDict):
    id: Required[str]
    quantity: Required[int]
    unit_price: Required[int]
    service_period_in_days: NotRequired[int]
    on_event: Required[enums.OnEvent]
    charge_once: Required[bool]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]


class CreateCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]
    taxability: NotRequired[enums.Taxability]
    entity_code: NotRequired[enums.EntityCode]
    exempt_number: NotRequired[str]
    net_term_days: NotRequired[int]
    taxjar_exemption_category: NotRequired[enums.TaxjarExemptionCategory]
    auto_collection: NotRequired[enums.AutoCollection]
    offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
    allow_direct_debit: NotRequired[bool]
    consolidated_invoicing: NotRequired[bool]
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    entity_identifier_scheme: NotRequired[str]
    entity_identifier_standard: NotRequired[str]
    is_einvoice_enabled: NotRequired[bool]
    einvoicing_method: NotRequired[enums.EinvoicingMethod]
    registered_for_gst: NotRequired[bool]
    business_customer_without_vat_number: NotRequired[bool]
    exemption_details: NotRequired[List[Dict[Any, Any]]]
    customer_type: NotRequired[enums.CustomerType]


class CreateEntityIdentifierParams(TypedDict):
    id: NotRequired[str]
    scheme: NotRequired[str]
    value: NotRequired[str]
    standard: NotRequired[str]


class CreateTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class CreateAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    trial_end: NotRequired[int]


class CreateEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    service_period_in_days: NotRequired[int]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    charge_on: NotRequired[enums.ChargeOn]


class CreateCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    tmp_token: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    number: NotRequired[str]
    expiry_month: NotRequired[int]
    expiry_year: NotRequired[int]
    cvv: NotRequired[str]
    billing_addr1: NotRequired[str]
    billing_addr2: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state_code: NotRequired[str]
    billing_state: NotRequired[str]
    billing_zip: NotRequired[str]
    billing_country: NotRequired[str]
    ip_address: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreateBankAccountParams(TypedDict):
    gateway_account_id: NotRequired[str]
    iban: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str]
    email: NotRequired[str]
    phone: NotRequired[str]
    bank_name: NotRequired[str]
    account_number: NotRequired[str]
    routing_number: NotRequired[str]
    bank_code: NotRequired[str]
    account_type: NotRequired[enums.AccountType]
    account_holder_type: NotRequired[enums.AccountHolderType]
    echeck_type: NotRequired[enums.EcheckType]
    issuing_country: NotRequired[str]
    swedish_identity_number: NotRequired[str]
    billing_address: NotRequired[Dict[Any, Any]]


class CreatePaymentMethodParams(TypedDict):
    type: NotRequired[enums.Type]
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    reference_id: NotRequired[str]
    tmp_token: NotRequired[str]
    issuing_country: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreatePaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreateBillingAddressParams(TypedDict):
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


class CreateShippingAddressParams(TypedDict):
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


class CreateStatementDescriptorParams(TypedDict):
    descriptor: NotRequired[str]


class CreateContractTermParams(TypedDict):
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    cancellation_cutoff_period: NotRequired[int]


class CreateCouponParams(TypedDict):
    coupon_id: NotRequired[str]
    apply_till: NotRequired[int]


class CreateForCustomerAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]
    trial_end: NotRequired[int]


class CreateForCustomerEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    service_period_in_days: NotRequired[int]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    charge_on: NotRequired[enums.ChargeOn]


class CreateForCustomerShippingAddressParams(TypedDict):
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


class CreateForCustomerStatementDescriptorParams(TypedDict):
    descriptor: NotRequired[str]


class CreateForCustomerPaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreateForCustomerContractTermParams(TypedDict):
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    cancellation_cutoff_period: NotRequired[int]


class CreateForCustomerCouponParams(TypedDict):
    coupon_id: NotRequired[str]
    apply_till: NotRequired[int]


class CreateWithItemsSubscriptionItemParams(TypedDict):
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


class CreateWithItemsDiscountParams(TypedDict):
    apply_on: Required[enums.ApplyOn]
    duration_type: Required[enums.DurationType]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: NotRequired[bool]
    item_price_id: NotRequired[str]


class CreateWithItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CreateWithItemsShippingAddressParams(TypedDict):
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


class CreateWithItemsStatementDescriptorParams(TypedDict):
    descriptor: NotRequired[str]


class CreateWithItemsPaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreateWithItemsContractTermParams(TypedDict):
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    contract_start: NotRequired[int]
    cancellation_cutoff_period: NotRequired[int]


class CreateWithItemsCouponParams(TypedDict):
    coupon_id: NotRequired[str]
    apply_till: NotRequired[int]


class UpdateAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    billing_cycles: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    trial_end: NotRequired[int]
    proration_type: NotRequired[enums.ProrationType]


class UpdateEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    service_period_in_days: NotRequired[int]
    charge_on: NotRequired[enums.ChargeOn]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]


class UpdateCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    tmp_token: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    number: NotRequired[str]
    expiry_month: NotRequired[int]
    expiry_year: NotRequired[int]
    cvv: NotRequired[str]
    billing_addr1: NotRequired[str]
    billing_addr2: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state_code: NotRequired[str]
    billing_state: NotRequired[str]
    billing_zip: NotRequired[str]
    billing_country: NotRequired[str]
    ip_address: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class UpdatePaymentMethodParams(TypedDict):
    type: NotRequired[enums.Type]
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    reference_id: NotRequired[str]
    tmp_token: NotRequired[str]
    issuing_country: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class UpdatePaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class UpdateBillingAddressParams(TypedDict):
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


class UpdateShippingAddressParams(TypedDict):
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


class UpdateStatementDescriptorParams(TypedDict):
    descriptor: NotRequired[str]


class UpdateCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    entity_identifier_scheme: NotRequired[str]
    is_einvoice_enabled: NotRequired[bool]
    einvoicing_method: NotRequired[enums.EinvoicingMethod]
    entity_identifier_standard: NotRequired[str]
    business_customer_without_vat_number: NotRequired[bool]
    registered_for_gst: NotRequired[bool]


class UpdateContractTermParams(TypedDict):
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    cancellation_cutoff_period: NotRequired[int]


class UpdateCouponParams(TypedDict):
    coupon_id: NotRequired[str]
    apply_till: NotRequired[int]


class UpdateForItemsSubscriptionItemParams(TypedDict):
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


class UpdateForItemsDiscountParams(TypedDict):
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


class UpdateForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class UpdateForItemsCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    tmp_token: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    number: NotRequired[str]
    expiry_month: NotRequired[int]
    expiry_year: NotRequired[int]
    cvv: NotRequired[str]
    billing_addr1: NotRequired[str]
    billing_addr2: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state_code: NotRequired[str]
    billing_state: NotRequired[str]
    billing_zip: NotRequired[str]
    billing_country: NotRequired[str]
    ip_address: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class UpdateForItemsPaymentMethodParams(TypedDict):
    type: NotRequired[enums.Type]
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    reference_id: NotRequired[str]
    tmp_token: NotRequired[str]
    issuing_country: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class UpdateForItemsPaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class UpdateForItemsBillingAddressParams(TypedDict):
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


class UpdateForItemsShippingAddressParams(TypedDict):
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


class UpdateForItemsStatementDescriptorParams(TypedDict):
    descriptor: NotRequired[str]


class UpdateForItemsCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    entity_identifier_scheme: NotRequired[str]
    is_einvoice_enabled: NotRequired[bool]
    einvoicing_method: NotRequired[enums.EinvoicingMethod]
    entity_identifier_standard: NotRequired[str]
    business_customer_without_vat_number: NotRequired[bool]
    registered_for_gst: NotRequired[bool]


class UpdateForItemsContractTermParams(TypedDict):
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    cancellation_cutoff_period: NotRequired[int]
    contract_start: NotRequired[int]


class UpdateForItemsCouponParams(TypedDict):
    coupon_id: NotRequired[str]
    apply_till: NotRequired[int]


class ReactivateContractTermParams(TypedDict):
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    cancellation_cutoff_period: NotRequired[int]


class ReactivateStatementDescriptorParams(TypedDict):
    descriptor: NotRequired[str]


class ReactivatePaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class ChargeFutureRenewalsSpecificDatesScheduleParams(TypedDict):
    terms_to_charge: NotRequired[int]
    date: NotRequired[int]


class ChargeFutureRenewalsFixedIntervalScheduleParams(TypedDict):
    number_of_occurrences: NotRequired[int]
    days_before_renewal: NotRequired[int]
    end_schedule_on: NotRequired[enums.EndScheduleOn]
    end_date: NotRequired[int]


class EditAdvanceInvoiceScheduleSpecificDatesScheduleParams(TypedDict):
    id: NotRequired[str]
    terms_to_charge: NotRequired[int]
    date: NotRequired[int]


class EditAdvanceInvoiceScheduleFixedIntervalScheduleParams(TypedDict):
    number_of_occurrences: NotRequired[int]
    days_before_renewal: NotRequired[int]
    end_schedule_on: NotRequired[enums.EndScheduleOn]
    end_date: NotRequired[int]


class RemoveAdvanceInvoiceScheduleSpecificDatesScheduleParams(TypedDict):
    id: NotRequired[str]


class ImportSubscriptionCustomerParams(TypedDict):
    id: NotRequired[str]
    email: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    locale: NotRequired[str]
    taxability: NotRequired[enums.Taxability]
    entity_code: NotRequired[enums.EntityCode]
    exempt_number: NotRequired[str]
    net_term_days: NotRequired[int]
    taxjar_exemption_category: NotRequired[enums.TaxjarExemptionCategory]
    customer_type: NotRequired[enums.CustomerType]
    auto_collection: NotRequired[enums.AutoCollection]
    allow_direct_debit: NotRequired[bool]
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]


class ImportSubscriptionAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]


class ImportSubscriptionEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    service_period_in_days: NotRequired[int]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]


class ImportSubscriptionChargedEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    last_charged_at: NotRequired[int]


class ImportSubscriptionContractTermParams(TypedDict):
    id: NotRequired[str]
    created_at: NotRequired[int]
    contract_start: NotRequired[int]
    billing_cycle: NotRequired[int]
    total_amount_raised: NotRequired[int]
    total_amount_raised_before_tax: NotRequired[int]
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    cancellation_cutoff_period: NotRequired[int]


class ImportSubscriptionCardParams(TypedDict):
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    tmp_token: NotRequired[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    number: NotRequired[str]
    expiry_month: NotRequired[int]
    expiry_year: NotRequired[int]
    cvv: NotRequired[str]
    billing_addr1: NotRequired[str]
    billing_addr2: NotRequired[str]
    billing_city: NotRequired[str]
    billing_state_code: NotRequired[str]
    billing_state: NotRequired[str]
    billing_zip: NotRequired[str]
    billing_country: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class ImportSubscriptionPaymentMethodParams(TypedDict):
    type: NotRequired[enums.Type]
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    reference_id: NotRequired[str]
    issuing_country: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class ImportSubscriptionBillingAddressParams(TypedDict):
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


class ImportSubscriptionShippingAddressParams(TypedDict):
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


class ImportSubscriptionTransactionParams(TypedDict):
    amount: NotRequired[int]
    payment_method: NotRequired[enums.PaymentMethod]
    reference_number: NotRequired[str]
    date: NotRequired[int]


class ImportSubscriptionCouponParams(TypedDict):
    coupon_id: NotRequired[str]
    apply_till: NotRequired[int]


class ImportForCustomerAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    billing_cycles: NotRequired[int]


class ImportForCustomerEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    service_period_in_days: NotRequired[int]
    on_event: NotRequired[enums.OnEvent]
    charge_once: NotRequired[bool]


class ImportForCustomerChargedEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    last_charged_at: NotRequired[int]


class ImportForCustomerContractTermParams(TypedDict):
    id: NotRequired[str]
    created_at: NotRequired[int]
    contract_start: NotRequired[int]
    billing_cycle: NotRequired[int]
    total_amount_raised: NotRequired[int]
    total_amount_raised_before_tax: NotRequired[int]
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    cancellation_cutoff_period: NotRequired[int]


class ImportForCustomerTransactionParams(TypedDict):
    amount: NotRequired[int]
    payment_method: NotRequired[enums.PaymentMethod]
    reference_number: NotRequired[str]
    date: NotRequired[int]


class ImportForCustomerShippingAddressParams(TypedDict):
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


class ImportForCustomerCouponParams(TypedDict):
    coupon_id: NotRequired[str]
    apply_till: NotRequired[int]


class ImportContractTermContractTermParams(TypedDict):
    id: NotRequired[str]
    created_at: NotRequired[int]
    contract_start: NotRequired[int]
    contract_end: NotRequired[int]
    status: NotRequired[ContractTermStatus]
    total_amount_raised: NotRequired[int]
    total_amount_raised_before_tax: NotRequired[int]
    total_contract_value: NotRequired[int]
    total_contract_value_before_tax: NotRequired[int]
    billing_cycle: NotRequired[int]
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    cancellation_cutoff_period: NotRequired[int]


class ImportUnbilledChargesUnbilledChargeParams(TypedDict):
    id: NotRequired[str]
    date_from: Required[int]
    date_to: Required[int]
    entity_type: Required["unbilled_charge.EntityType"]
    entity_id: NotRequired[str]
    description: NotRequired[str]
    unit_amount: NotRequired[int]
    quantity: NotRequired[int]
    amount: NotRequired[int]
    unit_amount_in_decimal: NotRequired[str]
    quantity_in_decimal: NotRequired[str]
    amount_in_decimal: NotRequired[str]
    discount_amount: NotRequired[int]
    use_for_proration: NotRequired[bool]
    is_advance_charge: NotRequired[bool]


class ImportUnbilledChargesDiscountParams(TypedDict):
    unbilled_charge_id: NotRequired[str]
    entity_type: NotRequired["invoice.DiscountEntityType"]
    entity_id: NotRequired[str]
    description: NotRequired[str]
    amount: Required[int]


class ImportUnbilledChargesTierParams(TypedDict):
    unbilled_charge_id: Required[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    quantity_used: NotRequired[int]
    unit_amount: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    quantity_used_in_decimal: NotRequired[str]
    unit_amount_in_decimal: NotRequired[str]


class ImportForItemsSubscriptionItemParams(TypedDict):
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


class ImportForItemsDiscountParams(TypedDict):
    apply_on: Required[enums.ApplyOn]
    duration_type: Required[enums.DurationType]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    period: NotRequired[int]
    period_unit: NotRequired[enums.PeriodUnit]
    included_in_mrr: NotRequired[bool]
    item_price_id: NotRequired[str]


class ImportForItemsChargedItemParams(TypedDict):
    item_price_id: NotRequired[str]
    last_charged_at: NotRequired[int]


class ImportForItemsItemTierParams(TypedDict):
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class ImportForItemsContractTermParams(TypedDict):
    id: NotRequired[str]
    created_at: NotRequired[int]
    contract_start: NotRequired[int]
    billing_cycle: NotRequired[int]
    total_amount_raised: NotRequired[int]
    total_amount_raised_before_tax: NotRequired[int]
    action_at_term_end: NotRequired[ContractTermActionAtTermEnd]
    cancellation_cutoff_period: NotRequired[int]


class ImportForItemsTransactionParams(TypedDict):
    amount: NotRequired[int]
    payment_method: NotRequired[enums.PaymentMethod]
    reference_number: NotRequired[str]
    date: NotRequired[int]


class ImportForItemsShippingAddressParams(TypedDict):
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


class ImportForItemsCouponParams(TypedDict):
    coupon_id: NotRequired[str]
    apply_till: NotRequired[int]


class CancelEventBasedAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    service_period_in_days: NotRequired[int]


class CancelForItemsSubscriptionItemParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    service_period_days: NotRequired[int]


class ResumePaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]
