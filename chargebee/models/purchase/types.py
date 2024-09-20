from typing import TypedDict, Required, NotRequired, Dict, List, Any
from chargebee.models import enums, contract_term


class CreatePurchaseItemParams(TypedDict):
    index: Required[int]
    item_price_id: Required[str]
    quantity: NotRequired[int]
    unit_amount: NotRequired[int]
    unit_amount_in_decimal: NotRequired[str]
    quantity_in_decimal: NotRequired[str]


class CreateItemTierParams(TypedDict):
    index: Required[int]
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


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
    state: NotRequired[str]
    state_code: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class CreateDiscountParams(TypedDict):
    index: NotRequired[int]
    coupon_id: NotRequired[str]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    included_in_mrr: NotRequired[bool]


class CreateSubscriptionInfoParams(TypedDict):
    index: Required[int]
    subscription_id: NotRequired[str]
    billing_cycles: NotRequired[int]
    contract_term_billing_cycle_on_renewal: NotRequired[int]
    meta_data: NotRequired[Dict[Any, Any]]


class CreateContractTermParams(TypedDict):
    index: Required[int]
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class CreateInvoiceInfoParams(TypedDict):
    po_number: NotRequired[str]
    notes: NotRequired[str]


class CreateStatementDescriptorParams(TypedDict):
    descriptor: NotRequired[str]


class CreateInstallmentInfoParams(TypedDict):
    config_id: NotRequired[str]
    amount: NotRequired[int]


class EstimatePurchaseItemParams(TypedDict):
    index: Required[int]
    item_price_id: Required[str]
    quantity: NotRequired[int]
    unit_amount: NotRequired[int]
    unit_amount_in_decimal: NotRequired[str]
    quantity_in_decimal: NotRequired[str]


class EstimateItemTierParams(TypedDict):
    index: Required[int]
    item_price_id: NotRequired[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class EstimateShippingAddressParams(TypedDict):
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: NotRequired[str]
    company: NotRequired[str]
    phone: NotRequired[str]
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    state_code: NotRequired[str]
    country: NotRequired[str]
    zip: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]


class EstimateDiscountParams(TypedDict):
    index: NotRequired[int]
    coupon_id: NotRequired[str]
    percentage: NotRequired[float]
    amount: NotRequired[int]
    included_in_mrr: NotRequired[bool]


class EstimateSubscriptionInfoParams(TypedDict):
    index: Required[int]
    subscription_id: NotRequired[str]
    billing_cycles: NotRequired[int]
    contract_term_billing_cycle_on_renewal: NotRequired[int]


class EstimateContractTermParams(TypedDict):
    index: Required[int]
    action_at_term_end: NotRequired["contract_term.ActionAtTermEnd"]
    cancellation_cutoff_period: NotRequired[int]


class EstimateCustomerParams(TypedDict):
    vat_number: NotRequired[str]
    vat_number_prefix: NotRequired[str]
    registered_for_gst: NotRequired[bool]
    taxability: NotRequired[enums.Taxability]
    entity_code: NotRequired[enums.EntityCode]
    exempt_number: NotRequired[str]
    exemption_details: NotRequired[List[Dict[Any, Any]]]
    customer_type: NotRequired[enums.CustomerType]


class EstimateBillingAddressParams(TypedDict):
    line1: NotRequired[str]
    line2: NotRequired[str]
    line3: NotRequired[str]
    city: NotRequired[str]
    state_code: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    validation_status: NotRequired[enums.ValidationStatus]
