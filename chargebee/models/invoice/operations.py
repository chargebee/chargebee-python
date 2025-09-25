from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import (
    enums,
    credit_note,
    payment_reference_number,
    payment_intent,
    transaction,
    card,
)


@dataclass
class Invoice:
    env: environment.Environment

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

    class LineItemDiscountDiscountType(Enum):
        ITEM_LEVEL_COUPON = "item_level_coupon"
        DOCUMENT_LEVEL_COUPON = "document_level_coupon"
        PROMOTIONAL_CREDITS = "promotional_credits"
        PRORATED_CREDITS = "prorated_credits"
        ITEM_LEVEL_DISCOUNT = "item_level_discount"
        DOCUMENT_LEVEL_DISCOUNT = "document_level_discount"

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

    class DiscountDiscountType(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"

        def __str__(self):
            return self.value

    class AppliedCreditTaxApplication(Enum):
        PRE_TAX = "pre_tax"
        POST_TAX = "post_tax"

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
        metered: NotRequired[bool]
        is_percentage_pricing: NotRequired[bool]
        reference_line_item_id: NotRequired[str]
        description: Required[str]
        entity_description: NotRequired[str]
        entity_type: Required["Invoice.LineItemEntityType"]
        tax_exempt_reason: NotRequired[enums.TaxExemptReason]
        entity_id: NotRequired[str]
        customer_id: NotRequired[str]

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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class LineItemDiscount(TypedDict):
        line_item_id: Required[str]
        discount_type: Required["Invoice.LineItemDiscountDiscountType"]
        coupon_id: NotRequired[str]
        entity_id: NotRequired[str]
        discount_amount: Required[int]

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

    class LineItemCredit(TypedDict):
        cn_id: Required[str]
        applied_amount: Required[float]
        line_item_id: NotRequired[str]

    class LineItemAddress(TypedDict):
        line_item_id: NotRequired[str]
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

    class Discount(TypedDict):
        amount: Required[int]
        description: NotRequired[str]
        entity_type: Required["Invoice.DiscountEntityType"]
        discount_type: NotRequired["Invoice.DiscountDiscountType"]
        entity_id: NotRequired[str]
        coupon_set_code: NotRequired[str]

    class Tax(TypedDict):
        name: Required[str]
        amount: Required[int]
        description: NotRequired[str]

    class TaxOrigin(TypedDict):
        country: NotRequired[str]
        registration_number: NotRequired[str]

    class LinkedPayment(TypedDict):
        txn_id: Required[str]
        applied_amount: Required[int]
        applied_at: Required[int]
        txn_status: NotRequired["transaction.Transaction.Status"]
        txn_date: NotRequired[int]
        txn_amount: NotRequired[int]

    class DunningAttempt(TypedDict):
        attempt: Required[int]
        transaction_id: NotRequired[str]
        dunning_type: Required[enums.DunningType]
        created_at: NotRequired[int]
        txn_status: NotRequired["transaction.Transaction.Status"]
        txn_amount: NotRequired[int]

    class AppliedCredit(TypedDict):
        cn_id: Required[str]
        applied_amount: Required[int]
        applied_at: Required[int]
        cn_reason_code: NotRequired["credit_note.CreditNote.ReasonCode"]
        cn_create_reason_code: NotRequired[str]
        cn_date: NotRequired[int]
        cn_status: Required["credit_note.CreditNote.Status"]
        tax_application: NotRequired["Invoice.AppliedCreditTaxApplication"]

    class AdjustmentCreditNote(TypedDict):
        cn_id: Required[str]
        cn_reason_code: NotRequired["credit_note.CreditNote.ReasonCode"]
        cn_create_reason_code: NotRequired[str]
        cn_date: NotRequired[int]
        cn_total: NotRequired[int]
        cn_status: Required["credit_note.CreditNote.Status"]

    class IssuedCreditNote(TypedDict):
        cn_id: Required[str]
        cn_reason_code: NotRequired["credit_note.CreditNote.ReasonCode"]
        cn_create_reason_code: NotRequired[str]
        cn_date: NotRequired[int]
        cn_total: NotRequired[int]
        cn_status: Required["credit_note.CreditNote.Status"]

    class LinkedOrder(TypedDict):
        id: Required[str]
        document_number: NotRequired[str]
        status: NotRequired["Invoice.LinkedOrderStatus"]
        order_type: NotRequired["Invoice.LinkedOrderOrderType"]
        reference_id: NotRequired[str]
        fulfillment_status: NotRequired[str]
        batch_id: NotRequired[str]
        created_at: Required[int]

    class Note(TypedDict):
        note: Required[str]
        entity_id: NotRequired[str]
        entity_type: NotRequired["Invoice.NoteEntityType"]

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

    class StatementDescriptor(TypedDict):
        id: Required[str]
        descriptor: NotRequired[str]

    class Einvoice(TypedDict):
        id: Required[str]
        reference_number: NotRequired[str]
        status: Required["Invoice.EinvoiceStatus"]
        message: NotRequired[str]

    class SiteDetailsAtCreation(TypedDict):
        timezone: NotRequired[str]
        organization_address: NotRequired[Dict[Any, Any]]

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
        preferred_scheme: NotRequired["card.Card.PreferredScheme"]
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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        quantity: NotRequired[int]
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
        preferred_scheme: NotRequired["card.Card.PreferredScheme"]
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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        entity_type: NotRequired["Invoice.LineItemEntityType"]
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
        created_at: NotRequired[int]

    class ImportInvoicePaymentReferenceNumberParams(TypedDict):
        id: NotRequired[str]
        type: Required["payment_reference_number.PaymentReferenceNumber.Type"]
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
        entity_type: Required["Invoice.DiscountEntityType"]
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
        id: NotRequired[str]
        amount: Required[int]
        payment_method: Required[enums.PaymentMethod]
        date: NotRequired[int]
        reference_number: NotRequired[str]

    class ImportInvoiceNoteParams(TypedDict):
        entity_type: NotRequired["Invoice.NoteEntityType"]
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

    class ImportInvoiceLineItemAddressParams(TypedDict):
        line_item_id: NotRequired[str]
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
        status: NotRequired[Filters.EnumFilter]

    class RetrieveLineItemParams(TypedDict):
        subscription_id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]

    class ListPaymentReferenceNumbersPaymentReferenceNumberParams(TypedDict):
        number: NotRequired[Filters.StringFilter]

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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class CloseNotesToRemoveParams(TypedDict):
        entity_type: NotRequired[enums.EntityType]
        entity_id: NotRequired[str]

    class RecordPaymentTransactionParams(TypedDict):
        amount: NotRequired[int]
        payment_method: Required[enums.PaymentMethod]
        reference_number: NotRequired[str]
        custom_payment_method_id: NotRequired[str]
        id_at_gateway: NotRequired[str]
        status: NotRequired["transaction.Transaction.Status"]
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
        reason_code: NotRequired["credit_note.CreditNote.ReasonCode"]
        create_reason_code: NotRequired[str]

    class RecordRefundTransactionParams(TypedDict):
        amount: NotRequired[int]
        payment_method: Required[enums.PaymentMethod]
        reference_number: NotRequired[str]
        custom_payment_method_id: NotRequired[str]
        date: Required[int]

    class RecordRefundCreditNoteParams(TypedDict):
        reason_code: NotRequired["credit_note.CreditNote.ReasonCode"]
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

    class CreateParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        currency_code: NotRequired[str]
        addons: NotRequired[List["Invoice.CreateAddonParams"]]
        invoice_date: NotRequired[int]
        charges: NotRequired[List["Invoice.CreateChargeParams"]]
        tax_providers_fields: NotRequired[List["Invoice.CreateTaxProvidersFieldParams"]]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[List["Invoice.CreateNotesToRemoveParams"]]
        po_number: NotRequired[str]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        shipping_address: NotRequired["Invoice.CreateShippingAddressParams"]
        statement_descriptor: NotRequired["Invoice.CreateStatementDescriptorParams"]
        card: NotRequired["Invoice.CreateCardParams"]
        bank_account: NotRequired["Invoice.CreateBankAccountParams"]
        token_id: NotRequired[str]
        payment_method: NotRequired["Invoice.CreatePaymentMethodParams"]
        payment_intent: NotRequired["Invoice.CreatePaymentIntentParams"]
        replace_primary_payment_source: NotRequired[bool]
        retain_payment_source: NotRequired[bool]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class CreateForChargeItemsAndChargesParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        currency_code: NotRequired[str]
        item_prices: NotRequired[
            List["Invoice.CreateForChargeItemsAndChargesItemPriceParams"]
        ]
        item_tiers: NotRequired[
            List["Invoice.CreateForChargeItemsAndChargesItemTierParams"]
        ]
        charges: NotRequired[List["Invoice.CreateForChargeItemsAndChargesChargeParams"]]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[
            List["Invoice.CreateForChargeItemsAndChargesNotesToRemoveParams"]
        ]
        po_number: NotRequired[str]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        tax_providers_fields: NotRequired[
            List["Invoice.CreateForChargeItemsAndChargesTaxProvidersFieldParams"]
        ]
        discounts: Required[
            List["Invoice.CreateForChargeItemsAndChargesDiscountParams"]
        ]
        invoice_date: NotRequired[int]
        shipping_address: NotRequired[
            "Invoice.CreateForChargeItemsAndChargesShippingAddressParams"
        ]
        statement_descriptor: NotRequired[
            "Invoice.CreateForChargeItemsAndChargesStatementDescriptorParams"
        ]
        card: NotRequired["Invoice.CreateForChargeItemsAndChargesCardParams"]
        bank_account: NotRequired[
            "Invoice.CreateForChargeItemsAndChargesBankAccountParams"
        ]
        token_id: NotRequired[str]
        payment_method: NotRequired[
            "Invoice.CreateForChargeItemsAndChargesPaymentMethodParams"
        ]
        payment_intent: NotRequired[
            "Invoice.CreateForChargeItemsAndChargesPaymentIntentParams"
        ]
        replace_primary_payment_source: NotRequired[bool]
        retain_payment_source: NotRequired[bool]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class ChargeParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        currency_code: NotRequired[str]
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        description: Required[str]
        date_from: NotRequired[int]
        date_to: NotRequired[int]
        coupon_ids: NotRequired[List[str]]
        coupon: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        po_number: NotRequired[str]
        invoice_date: NotRequired[int]
        tax_providers_fields: NotRequired[List["Invoice.ChargeTaxProvidersFieldParams"]]
        payment_source_id: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class ChargeAddonParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        addon_id: Required[str]
        addon_quantity: NotRequired[int]
        addon_unit_price: NotRequired[int]
        addon_quantity_in_decimal: NotRequired[str]
        addon_unit_price_in_decimal: NotRequired[str]
        date_from: NotRequired[int]
        date_to: NotRequired[int]
        coupon_ids: NotRequired[List[str]]
        coupon: NotRequired[str]
        po_number: NotRequired[str]
        invoice_date: NotRequired[int]
        payment_source_id: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class CreateForChargeItemParams(TypedDict):
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        item_price: Required["Invoice.CreateForChargeItemItemPriceParams"]
        item_tiers: NotRequired[List["Invoice.CreateForChargeItemItemTierParams"]]
        po_number: NotRequired[str]
        coupon: NotRequired[str]
        payment_source_id: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        invoice_date: NotRequired[int]

    class StopDunningParams(TypedDict):
        comment: NotRequired[str]

    class PauseDunningParams(TypedDict):
        expected_payment_date: Required[int]
        comment: NotRequired[str]

    class ResumeDunningParams(TypedDict):
        comment: NotRequired[str]

    class ImportInvoiceParams(TypedDict):
        id: Required[str]
        currency_code: NotRequired[str]
        customer_id: NotRequired[str]
        subscription_id: NotRequired[str]
        po_number: NotRequired[str]
        price_type: NotRequired[enums.PriceType]
        tax_override_reason: NotRequired[enums.TaxOverrideReason]
        vat_number: NotRequired[str]
        vat_number_prefix: NotRequired[str]
        date: Required[int]
        total: Required[int]
        round_off: NotRequired[int]
        status: NotRequired["Invoice.Status"]
        voided_at: NotRequired[int]
        void_reason_code: NotRequired[str]
        is_written_off: NotRequired[bool]
        write_off_amount: NotRequired[int]
        write_off_date: NotRequired[int]
        due_date: NotRequired[int]
        net_term_days: NotRequired[int]
        has_advance_charges: NotRequired[bool]
        use_for_proration: NotRequired[bool]
        line_items: Required[List["Invoice.ImportInvoiceLineItemParams"]]
        payment_reference_numbers: Required[
            List["Invoice.ImportInvoicePaymentReferenceNumberParams"]
        ]
        line_item_tiers: Required[List["Invoice.ImportInvoiceLineItemTierParams"]]
        discounts: Required[List["Invoice.ImportInvoiceDiscountParams"]]
        taxes: Required[List["Invoice.ImportInvoiceTaxParams"]]
        credit_note: NotRequired["Invoice.ImportInvoiceCreditNoteParams"]
        payments: Required[List["Invoice.ImportInvoicePaymentParams"]]
        notes: NotRequired[List["Invoice.ImportInvoiceNoteParams"]]
        billing_address: NotRequired["Invoice.ImportInvoiceBillingAddressParams"]
        shipping_address: NotRequired["Invoice.ImportInvoiceShippingAddressParams"]
        line_item_addresses: NotRequired[
            List["Invoice.ImportInvoiceLineItemAddressParams"]
        ]

    class ApplyPaymentsParams(TypedDict):
        transactions: NotRequired[List["Invoice.ApplyPaymentsTransactionParams"]]
        comment: NotRequired[str]

    class DeleteLineItemsParams(TypedDict):
        line_items: NotRequired[List["Invoice.DeleteLineItemsLineItemParams"]]

    class ApplyCreditsParams(TypedDict):
        credit_notes: NotRequired[List["Invoice.ApplyCreditsCreditNoteParams"]]
        comment: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        einvoice: NotRequired["Invoice.ListEinvoiceParams"]
        paid_on_after: NotRequired[int]
        include_deleted: NotRequired[bool]
        id: NotRequired[Filters.StringFilter]
        subscription_id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        recurring: NotRequired[Filters.BooleanFilter]
        status: NotRequired[Filters.EnumFilter]
        price_type: NotRequired[Filters.EnumFilter]
        date: NotRequired[Filters.TimestampFilter]
        paid_at: NotRequired[Filters.TimestampFilter]
        total: NotRequired[Filters.NumberFilter]
        amount_paid: NotRequired[Filters.NumberFilter]
        amount_adjusted: NotRequired[Filters.NumberFilter]
        credits_applied: NotRequired[Filters.NumberFilter]
        amount_due: NotRequired[Filters.NumberFilter]
        dunning_status: NotRequired[Filters.EnumFilter]
        payment_owner: NotRequired[Filters.StringFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        channel: NotRequired[Filters.EnumFilter]
        voided_at: NotRequired[Filters.TimestampFilter]
        void_reason_code: NotRequired[Filters.StringFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class InvoicesForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class InvoicesForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class RetrieveParams(TypedDict):
        line_item: NotRequired["Invoice.RetrieveLineItemParams"]

    class PdfParams(TypedDict):
        disposition_type: NotRequired[enums.DispositionType]

    class ListPaymentReferenceNumbersParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        payment_reference_number: NotRequired[
            "Invoice.ListPaymentReferenceNumbersPaymentReferenceNumberParams"
        ]
        id: NotRequired[Filters.StringFilter]

    class AddChargeParams(TypedDict):
        amount: Required[int]
        description: Required[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        avalara_tax_code: NotRequired[str]
        hsn_code: NotRequired[str]
        taxjar_product_code: NotRequired[str]
        line_item: NotRequired["Invoice.AddChargeLineItemParams"]
        comment: NotRequired[str]
        subscription_id: NotRequired[str]

    class AddAddonChargeParams(TypedDict):
        addon_id: Required[str]
        addon_quantity: NotRequired[int]
        addon_unit_price: NotRequired[int]
        addon_quantity_in_decimal: NotRequired[str]
        addon_unit_price_in_decimal: NotRequired[str]
        line_item: NotRequired["Invoice.AddAddonChargeLineItemParams"]
        comment: NotRequired[str]
        subscription_id: NotRequired[str]

    class AddChargeItemParams(TypedDict):
        item_price: Required["Invoice.AddChargeItemItemPriceParams"]
        item_tiers: NotRequired[List["Invoice.AddChargeItemItemTierParams"]]
        comment: NotRequired[str]
        subscription_id: NotRequired[str]

    class CloseParams(TypedDict):
        comment: NotRequired[str]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[List["Invoice.CloseNotesToRemoveParams"]]
        invoice_date: NotRequired[int]

    class CollectPaymentParams(TypedDict):
        amount: NotRequired[int]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        comment: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]

    class RecordPaymentParams(TypedDict):
        transaction: Required["Invoice.RecordPaymentTransactionParams"]
        comment: NotRequired[str]

    class RecordTaxWithheldParams(TypedDict):
        tax_withheld: Required["Invoice.RecordTaxWithheldTaxWithheldParams"]

    class RemoveTaxWithheldParams(TypedDict):
        tax_withheld: Required["Invoice.RemoveTaxWithheldTaxWithheldParams"]

    class RefundParams(TypedDict):
        refund_amount: NotRequired[int]
        credit_note: NotRequired["Invoice.RefundCreditNoteParams"]
        comment: NotRequired[str]
        customer_notes: NotRequired[str]

    class RecordRefundParams(TypedDict):
        transaction: Required["Invoice.RecordRefundTransactionParams"]
        credit_note: NotRequired["Invoice.RecordRefundCreditNoteParams"]
        comment: NotRequired[str]
        customer_notes: NotRequired[str]

    class RemovePaymentParams(TypedDict):
        transaction: Required["Invoice.RemovePaymentTransactionParams"]

    class RemoveCreditNoteParams(TypedDict):
        credit_note: Required["Invoice.RemoveCreditNoteCreditNoteParams"]

    class VoidInvoiceParams(TypedDict):
        comment: NotRequired[str]
        void_reason_code: NotRequired[str]

    class WriteOffParams(TypedDict):
        comment: NotRequired[str]

    class DeleteParams(TypedDict):
        comment: NotRequired[str]

    class UpdateDetailsParams(TypedDict):
        billing_address: NotRequired["Invoice.UpdateDetailsBillingAddressParams"]
        shipping_address: NotRequired["Invoice.UpdateDetailsShippingAddressParams"]
        statement_descriptor: NotRequired[
            "Invoice.UpdateDetailsStatementDescriptorParams"
        ]
        vat_number: NotRequired[str]
        vat_number_prefix: NotRequired[str]
        po_number: NotRequired[str]
        comment: NotRequired[str]

    class ApplyPaymentScheduleSchemeParams(TypedDict):
        scheme_id: Required[str]
        amount: NotRequired[int]

    def create(self, params: CreateParams = None, headers=None) -> CreateResponse:
        jsonKeys = {
            "additional_information": 1,
            "billing_address": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_for_charge_items_and_charges(
        self, params: CreateForChargeItemsAndChargesParams, headers=None
    ) -> CreateForChargeItemsAndChargesResponse:
        jsonKeys = {
            "additional_information": 1,
            "billing_address": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", "create_for_charge_items_and_charges"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForChargeItemsAndChargesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def charge(self, params: ChargeParams, headers=None) -> ChargeResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", "charge"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ChargeResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def charge_addon(
        self, params: ChargeAddonParams, headers=None
    ) -> ChargeAddonResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", "charge_addon"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ChargeAddonResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_for_charge_item(
        self, params: CreateForChargeItemParams, headers=None
    ) -> CreateForChargeItemResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", "create_for_charge_item"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForChargeItemResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def stop_dunning(
        self, id, params: StopDunningParams = None, headers=None
    ) -> StopDunningResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "stop_dunning"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            StopDunningResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def pause_dunning(
        self, id, params: PauseDunningParams, headers=None
    ) -> PauseDunningResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "pause_dunning"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PauseDunningResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def resume_dunning(
        self, id, params: ResumeDunningParams = None, headers=None
    ) -> ResumeDunningResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "resume_dunning"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ResumeDunningResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def import_invoice(
        self, params: ImportInvoiceParams, headers=None
    ) -> ImportInvoiceResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", "import_invoice"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportInvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def apply_payments(
        self, id, params: ApplyPaymentsParams = None, headers=None
    ) -> ApplyPaymentsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "apply_payments"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ApplyPaymentsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def sync_usages(self, id, headers=None) -> SyncUsagesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "sync_usages"),
            self.env,
            None,
            headers,
            SyncUsagesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete_line_items(
        self, id, params: DeleteLineItemsParams = None, headers=None
    ) -> DeleteLineItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "delete_line_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteLineItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def apply_credits(
        self, id, params: ApplyCreditsParams = None, headers=None
    ) -> ApplyCreditsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "apply_credits"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ApplyCreditsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("invoices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def invoices_for_customer(
        self, id, params: InvoicesForCustomerParams = None, headers=None
    ) -> InvoicesForCustomerResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "invoices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            InvoicesForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def invoices_for_subscription(
        self, id, params: InvoicesForSubscriptionParams = None, headers=None
    ) -> InvoicesForSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "invoices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            InvoicesForSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(
        self, id, params: RetrieveParams = None, headers=None
    ) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("invoices", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def pdf(self, id, params: PdfParams = None, headers=None) -> PdfResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "pdf"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PdfResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def download_einvoice(self, id, headers=None) -> DownloadEinvoiceResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("invoices", id, "download_einvoice"),
            self.env,
            None,
            headers,
            DownloadEinvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list_payment_reference_numbers(
        self, params: ListPaymentReferenceNumbersParams = None, headers=None
    ) -> ListPaymentReferenceNumbersResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("invoices", "payment_reference_numbers"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListPaymentReferenceNumbersResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def add_charge(
        self, id, params: AddChargeParams, headers=None
    ) -> AddChargeResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "add_charge"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddChargeResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def add_addon_charge(
        self, id, params: AddAddonChargeParams, headers=None
    ) -> AddAddonChargeResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "add_addon_charge"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddAddonChargeResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def add_charge_item(
        self, id, params: AddChargeItemParams, headers=None
    ) -> AddChargeItemResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "add_charge_item"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddChargeItemResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def close(self, id, params: CloseParams = None, headers=None) -> CloseResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "close"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CloseResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def collect_payment(
        self, id, params: CollectPaymentParams = None, headers=None
    ) -> CollectPaymentResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "collect_payment"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CollectPaymentResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def record_payment(
        self, id, params: RecordPaymentParams, headers=None
    ) -> RecordPaymentResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "record_payment"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RecordPaymentResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def record_tax_withheld(
        self, id, params: RecordTaxWithheldParams, headers=None
    ) -> RecordTaxWithheldResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "record_tax_withheld"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RecordTaxWithheldResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_tax_withheld(
        self, id, params: RemoveTaxWithheldParams, headers=None
    ) -> RemoveTaxWithheldResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "remove_tax_withheld"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RemoveTaxWithheldResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def refund(self, id, params: RefundParams = None, headers=None) -> RefundResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "refund"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RefundResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def record_refund(
        self, id, params: RecordRefundParams, headers=None
    ) -> RecordRefundResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "record_refund"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RecordRefundResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_payment(
        self, id, params: RemovePaymentParams, headers=None
    ) -> RemovePaymentResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "remove_payment"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RemovePaymentResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_credit_note(
        self, id, params: RemoveCreditNoteParams, headers=None
    ) -> RemoveCreditNoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "remove_credit_note"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RemoveCreditNoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def void_invoice(
        self, id, params: VoidInvoiceParams = None, headers=None
    ) -> VoidInvoiceResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "void"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            VoidInvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def write_off(
        self, id, params: WriteOffParams = None, headers=None
    ) -> WriteOffResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "write_off"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            WriteOffResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, params: DeleteParams = None, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "delete"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_details(
        self, id, params: UpdateDetailsParams = None, headers=None
    ) -> UpdateDetailsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "update_details"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateDetailsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def apply_payment_schedule_scheme(
        self, id, params: ApplyPaymentScheduleSchemeParams, headers=None
    ) -> ApplyPaymentScheduleSchemeResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "apply_payment_schedule_scheme"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ApplyPaymentScheduleSchemeResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def payment_schedules(self, id, headers=None) -> PaymentSchedulesResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("invoices", id, "payment_schedules"),
            self.env,
            None,
            headers,
            PaymentSchedulesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def resend_einvoice(self, id, headers=None) -> ResendEinvoiceResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "resend_einvoice"),
            self.env,
            None,
            headers,
            ResendEinvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def send_einvoice(self, id, headers=None) -> SendEinvoiceResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("invoices", id, "send_einvoice"),
            self.env,
            None,
            headers,
            SendEinvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )
