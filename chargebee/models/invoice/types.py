from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import (
    enums,
    credit_note,
    payment_reference_number,
    payment_intent,
    transaction,
)


class Status(Enum):
    PAID = "paid"
    POSTED = "posted"
    PAYMENT_DUE = "payment_due"
    NOT_PAID = "not_paid"
    VOIDED = "voided"
    PENDING = "pending"

    def __str__(self):
        return self.value


class DunningStatus(Enum):
    IN_PROGRESS = "in_progress"
    EXHAUSTED = "exhausted"
    STOPPED = "stopped"
    SUCCESS = "success"

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


class LinkedOrderStatus(Enum):
    NEW = "new"
    PROCESSING = "processing"
    COMPLETE = "complete"
    CANCELLED = "cancelled"
    VOIDED = "voided"
    QUEUED = "queued"
    AWAITING_SHIPMENT = "awaiting_shipment"
    ON_HOLD = "on_hold"
    DELIVERED = "delivered"
    SHIPPED = "shipped"
    PARTIALLY_DELIVERED = "partially_delivered"
    RETURNED = "returned"

    def __str__(self):
        return self.value


class LinkedOrderOrderType(Enum):
    MANUAL = "manual"
    SYSTEM_GENERATED = "system_generated"

    def __str__(self):
        return self.value


class NoteEntityType(Enum):
    COUPON = "coupon"
    SUBSCRIPTION = "subscription"
    CUSTOMER = "customer"
    PLAN_ITEM_PRICE = "plan_item_price"
    ADDON_ITEM_PRICE = "addon_item_price"
    CHARGE_ITEM_PRICE = "charge_item_price"
    TAX = "tax"
    PLAN = "plan"
    ADDON = "addon"

    def __str__(self):
        return self.value


class EinvoiceStatus(Enum):
    SCHEDULED = "scheduled"
    SKIPPED = "skipped"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    FAILED = "failed"
    REGISTERED = "registered"

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


class LinkedPayment(TypedDict):
    txn_id: Required[str]
    applied_amount: Required[int]
    applied_at: Required[int]
    txn_status: NotRequired["transaction.Status"]
    txn_date: NotRequired[int]
    txn_amount: NotRequired[int]


class DunningAttempt(TypedDict):
    attempt: Required[int]
    transaction_id: NotRequired[str]
    dunning_type: Required[enums.DunningType]
    created_at: NotRequired[int]
    txn_status: NotRequired["transaction.Status"]
    txn_amount: NotRequired[int]


class AppliedCredit(TypedDict):
    cn_id: Required[str]
    applied_amount: Required[int]
    applied_at: Required[int]
    cn_reason_code: NotRequired["credit_note.ReasonCode"]
    cn_create_reason_code: NotRequired[str]
    cn_date: NotRequired[int]
    cn_status: Required["credit_note.Status"]


class AdjustmentCreditNote(TypedDict):
    cn_id: Required[str]
    cn_reason_code: NotRequired["credit_note.ReasonCode"]
    cn_create_reason_code: NotRequired[str]
    cn_date: NotRequired[int]
    cn_total: NotRequired[int]
    cn_status: Required["credit_note.Status"]


class IssuedCreditNote(TypedDict):
    cn_id: Required[str]
    cn_reason_code: NotRequired["credit_note.ReasonCode"]
    cn_create_reason_code: NotRequired[str]
    cn_date: NotRequired[int]
    cn_total: NotRequired[int]
    cn_status: Required["credit_note.Status"]


class LinkedOrder(TypedDict):
    id: Required[str]
    document_number: NotRequired[str]
    status: NotRequired[LinkedOrderStatus]
    order_type: NotRequired[LinkedOrderOrderType]
    reference_id: NotRequired[str]
    fulfillment_status: NotRequired[str]
    batch_id: NotRequired[str]
    created_at: Required[int]


class Note(TypedDict):
    entity_type: Required[NoteEntityType]
    note: Required[str]
    entity_id: NotRequired[str]


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


class StatementDescriptor(TypedDict):
    id: Required[str]
    descriptor: NotRequired[str]


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


class Einvoice(TypedDict):
    id: Required[str]
    reference_number: NotRequired[str]
    status: Required[EinvoiceStatus]
    message: NotRequired[str]


class SiteDetailsAtCreation(TypedDict):
    timezone: NotRequired[str]
    organization_address: NotRequired[Dict[Any, Any]]


class TaxOrigin(TypedDict):
    country: NotRequired[str]
    registration_number: NotRequired[str]


class CreateAddonParams(TypedDict):
    id: NotRequired[str]
    quantity: NotRequired[int]
    unit_price: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price_in_decimal: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class CreateChargeParams(TypedDict):
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


class CreateTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class CreateNotesToRemoveParams(TypedDict):
    entity_type: NotRequired[enums.EntityType]
    entity_id: NotRequired[str]


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


class CreateForChargeItemsAndChargesItemPriceParams(TypedDict):
    item_price_id: NotRequired[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


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


class CreateForChargeItemsAndChargesNotesToRemoveParams(TypedDict):
    entity_type: NotRequired[enums.EntityType]
    entity_id: NotRequired[str]


class CreateForChargeItemsAndChargesTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class CreateForChargeItemsAndChargesDiscountParams(TypedDict):
    percentage: NotRequired[float]
    amount: NotRequired[int]
    apply_on: Required[enums.ApplyOn]
    item_price_id: NotRequired[str]


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


class CreateForChargeItemsAndChargesStatementDescriptorParams(TypedDict):
    descriptor: NotRequired[str]


class CreateForChargeItemsAndChargesCardParams(TypedDict):
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


class CreateForChargeItemsAndChargesBankAccountParams(TypedDict):
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


class CreateForChargeItemsAndChargesPaymentMethodParams(TypedDict):
    type: NotRequired[enums.Type]
    gateway: NotRequired[enums.Gateway]
    gateway_account_id: NotRequired[str]
    reference_id: NotRequired[str]
    tmp_token: NotRequired[str]
    issuing_country: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class CreateForChargeItemsAndChargesPaymentIntentParams(TypedDict):
    id: NotRequired[str]
    gateway_account_id: NotRequired[str]
    gw_token: NotRequired[str]
    payment_method_type: NotRequired["payment_intent.PaymentMethodType"]
    reference_id: NotRequired[str]
    gw_payment_method_id: NotRequired[str]
    additional_information: NotRequired[Dict[Any, Any]]


class ChargeTaxProvidersFieldParams(TypedDict):
    provider_name: NotRequired[str]
    field_id: NotRequired[str]
    field_value: NotRequired[str]


class CreateForChargeItemItemPriceParams(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class CreateForChargeItemItemTierParams(TypedDict):
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class ImportInvoiceLineItemParams(TypedDict):
    id: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]
    subscription_id: NotRequired[str]
    description: Required[str]
    unit_amount: NotRequired[int]
    quantity: NotRequired[int]
    amount: NotRequired[int]
    unit_amount_in_decimal: NotRequired[str]
    quantity_in_decimal: NotRequired[str]
    amount_in_decimal: NotRequired[str]
    entity_type: NotRequired[LineItemEntityType]
    entity_id: NotRequired[str]
    item_level_discount1_entity_id: NotRequired[str]
    item_level_discount1_amount: NotRequired[int]
    item_level_discount2_entity_id: NotRequired[str]
    item_level_discount2_amount: NotRequired[int]
    tax1_name: NotRequired[str]
    tax1_amount: NotRequired[int]
    tax2_name: NotRequired[str]
    tax2_amount: NotRequired[int]
    tax3_name: NotRequired[str]
    tax3_amount: NotRequired[int]
    tax4_name: NotRequired[str]
    tax4_amount: NotRequired[int]
    tax5_name: NotRequired[str]
    tax5_amount: NotRequired[int]
    tax6_name: NotRequired[str]
    tax6_amount: NotRequired[int]
    tax7_name: NotRequired[str]
    tax7_amount: NotRequired[int]
    tax8_name: NotRequired[str]
    tax8_amount: NotRequired[int]
    tax9_name: NotRequired[str]
    tax9_amount: NotRequired[int]
    tax10_name: NotRequired[str]
    tax10_amount: NotRequired[int]


class ImportInvoicePaymentReferenceNumberParams(TypedDict):
    id: NotRequired[str]
    type: Required["payment_reference_number.Type"]
    number: Required[str]


class ImportInvoiceLineItemTierParams(TypedDict):
    line_item_id: Required[str]
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    quantity_used: NotRequired[int]
    unit_amount: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    quantity_used_in_decimal: NotRequired[str]
    unit_amount_in_decimal: NotRequired[str]


class ImportInvoiceDiscountParams(TypedDict):
    entity_type: Required[DiscountEntityType]
    entity_id: NotRequired[str]
    description: NotRequired[str]
    amount: Required[int]


class ImportInvoiceTaxParams(TypedDict):
    name: Required[str]
    rate: Required[float]
    amount: NotRequired[int]
    description: NotRequired[str]
    juris_type: NotRequired[enums.TaxJurisType]
    juris_name: NotRequired[str]
    juris_code: NotRequired[str]


class ImportInvoiceCreditNoteParams(TypedDict):
    id: NotRequired[str]


class ImportInvoicePaymentParams(TypedDict):
    amount: Required[int]
    payment_method: Required[enums.PaymentMethod]
    date: NotRequired[int]
    reference_number: NotRequired[str]


class ImportInvoiceNoteParams(TypedDict):
    entity_type: NotRequired[NoteEntityType]
    entity_id: NotRequired[str]
    note: NotRequired[str]


class ImportInvoiceBillingAddressParams(TypedDict):
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


class ImportInvoiceShippingAddressParams(TypedDict):
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


class ApplyPaymentsTransactionParams(TypedDict):
    id: NotRequired[str]
    amount: NotRequired[int]


class DeleteLineItemsLineItemParams(TypedDict):
    id: NotRequired[str]


class ApplyCreditsCreditNoteParams(TypedDict):
    id: NotRequired[str]


class ListEinvoiceParams(TypedDict):
    Status: NotRequired[Filters.EnumFilter]


class ListPaymentReferenceNumbersPaymentReferenceNumberParams(TypedDict):
    Number: NotRequired[Filters.StringFilter]


class AddChargeLineItemParams(TypedDict):
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class AddAddonChargeLineItemParams(TypedDict):
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class AddChargeItemItemPriceParams(TypedDict):
    item_price_id: Required[str]
    quantity: NotRequired[int]
    quantity_in_decimal: NotRequired[str]
    unit_price: NotRequired[int]
    unit_price_in_decimal: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]


class AddChargeItemItemTierParams(TypedDict):
    starting_unit: NotRequired[int]
    ending_unit: NotRequired[int]
    price: NotRequired[int]
    starting_unit_in_decimal: NotRequired[str]
    ending_unit_in_decimal: NotRequired[str]
    price_in_decimal: NotRequired[str]


class CloseNotesToRemoveParams(TypedDict):
    entity_type: NotRequired[enums.EntityType]
    entity_id: NotRequired[str]


class RecordPaymentTransactionParams(TypedDict):
    amount: NotRequired[int]
    payment_method: Required[enums.PaymentMethod]
    reference_number: NotRequired[str]
    custom_payment_method_id: NotRequired[str]
    id_at_gateway: NotRequired[str]
    status: NotRequired["transaction.Status"]
    date: NotRequired[int]
    error_code: NotRequired[str]
    error_text: NotRequired[str]


class RecordTaxWithheldTaxWithheldParams(TypedDict):
    amount: Required[int]
    reference_number: NotRequired[str]
    date: NotRequired[int]
    description: NotRequired[str]


class RemoveTaxWithheldTaxWithheldParams(TypedDict):
    id: Required[str]


class RefundCreditNoteParams(TypedDict):
    reason_code: NotRequired["credit_note.ReasonCode"]
    create_reason_code: NotRequired[str]


class RecordRefundTransactionParams(TypedDict):
    amount: NotRequired[int]
    payment_method: Required[enums.PaymentMethod]
    reference_number: NotRequired[str]
    custom_payment_method_id: NotRequired[str]
    date: Required[int]


class RecordRefundCreditNoteParams(TypedDict):
    reason_code: NotRequired["credit_note.ReasonCode"]
    create_reason_code: NotRequired[str]


class RemovePaymentTransactionParams(TypedDict):
    id: Required[str]


class RemoveCreditNoteCreditNoteParams(TypedDict):
    id: Required[str]


class UpdateDetailsBillingAddressParams(TypedDict):
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


class UpdateDetailsShippingAddressParams(TypedDict):
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


class UpdateDetailsStatementDescriptorParams(TypedDict):
    descriptor: NotRequired[str]
