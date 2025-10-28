from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, contract_term


@dataclass
class Quote:
    env: environment.Environment

    class Status(Enum):
        OPEN = "open"
        ACCEPTED = "accepted"
        DECLINED = "declined"
        INVOICED = "invoiced"
        CLOSED = "closed"
        PENDING_APPROVAL = "pending_approval"
        APPROVAL_REJECTED = "approval_rejected"
        PROPOSED = "proposed"
        VOIDED = "voided"
        EXPIRED = "expired"

        def __str__(self):
            return self.value

    class OperationType(Enum):
        CREATE_SUBSCRIPTION_FOR_CUSTOMER = "create_subscription_for_customer"
        CHANGE_SUBSCRIPTION = "change_subscription"
        ONETIME_INVOICE = "onetime_invoice"
        RENEW_SUBSCRIPTION = "renew_subscription"

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
        entity_type: Required["Quote.LineItemEntityType"]
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
        discount_type: Required["Quote.LineItemDiscountDiscountType"]
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

    class Discount(TypedDict):
        amount: Required[int]
        description: NotRequired[str]
        line_item_id: NotRequired[str]
        entity_type: Required["Quote.DiscountEntityType"]
        discount_type: NotRequired["Quote.DiscountDiscountType"]
        entity_id: NotRequired[str]
        coupon_set_code: NotRequired[str]

    class Tax(TypedDict):
        name: Required[str]
        amount: Required[int]
        description: NotRequired[str]

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
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
        start_date: NotRequired[int]
        end_date: NotRequired[int]
        ramp_tier_id: NotRequired[str]

    class CreateSubItemsForCustomerQuoteDiscountParams(TypedDict):
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]
        start_date: NotRequired[int]
        end_date: NotRequired[int]

    class CreateSubItemsForCustomerQuoteItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]
        ramp_tier_id: NotRequired[str]

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class CreateSubItemsForCustomerQuoteBillingAddressParams(TypedDict):
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

    class CreateSubItemsForCustomerQuoteCouponParams(TypedDict):
        id: NotRequired[str]
        start_date: NotRequired[int]
        end_date: NotRequired[int]

    class EditCreateSubCustomerQuoteForItemsSubscriptionParams(TypedDict):
        id: NotRequired[str]
        po_number: NotRequired[str]
        trial_end: NotRequired[int]
        setup_fee: NotRequired[int]
        start_date: NotRequired[int]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
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
        start_date: NotRequired[int]
        end_date: NotRequired[int]
        ramp_tier_id: NotRequired[str]

    class EditCreateSubCustomerQuoteForItemsDiscountParams(TypedDict):
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]
        start_date: NotRequired[int]
        end_date: NotRequired[int]

    class EditCreateSubCustomerQuoteForItemsItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]
        ramp_tier_id: NotRequired[str]

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class EditCreateSubCustomerQuoteForItemsBillingAddressParams(TypedDict):
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

    class EditCreateSubCustomerQuoteForItemsCouponParams(TypedDict):
        id: NotRequired[str]
        start_date: NotRequired[int]
        end_date: NotRequired[int]

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
        start_date: NotRequired[int]
        end_date: NotRequired[int]
        ramp_tier_id: NotRequired[str]

    class UpdateSubscriptionQuoteForItemsDiscountParams(TypedDict):
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]
        operation_type: Required[enums.OperationType]
        id: NotRequired[str]
        start_date: NotRequired[int]
        end_date: NotRequired[int]

    class UpdateSubscriptionQuoteForItemsItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]
        ramp_tier_id: NotRequired[str]

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class UpdateSubscriptionQuoteForItemsCouponParams(TypedDict):
        id: NotRequired[str]
        start_date: NotRequired[int]
        end_date: NotRequired[int]

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
        start_date: NotRequired[int]
        end_date: NotRequired[int]
        ramp_tier_id: NotRequired[str]

    class EditUpdateSubscriptionQuoteForItemsSubscriptionParams(TypedDict):
        setup_fee: NotRequired[int]
        start_date: NotRequired[int]
        trial_end: NotRequired[int]
        coupon: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        contract_term_billing_cycle_on_renewal: NotRequired[int]

    class EditUpdateSubscriptionQuoteForItemsDiscountParams(TypedDict):
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]
        operation_type: Required[enums.OperationType]
        id: NotRequired[str]
        start_date: NotRequired[int]
        end_date: NotRequired[int]

    class EditUpdateSubscriptionQuoteForItemsItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]
        ramp_tier_id: NotRequired[str]

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class EditUpdateSubscriptionQuoteForItemsCouponParams(TypedDict):
        id: NotRequired[str]
        start_date: NotRequired[int]
        end_date: NotRequired[int]

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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class CreateForChargeItemsAndChargesChargeParams(TypedDict):
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        description: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        service_period: NotRequired[int]

    class CreateForChargeItemsAndChargesBillingAddressParams(TypedDict):
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
        quantity: NotRequired[int]
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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class EditForChargeItemsAndChargesChargeParams(TypedDict):
        amount: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        description: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        service_period: NotRequired[int]

    class EditForChargeItemsAndChargesBillingAddressParams(TypedDict):
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
        quantity: NotRequired[int]
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

    class CreateSubForCustomerQuoteParams(TypedDict):
        name: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: Required["Quote.CreateSubForCustomerQuoteSubscriptionParams"]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List["Quote.CreateSubForCustomerQuoteAddonParams"]]
        event_based_addons: NotRequired[
            List["Quote.CreateSubForCustomerQuoteEventBasedAddonParams"]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            "Quote.CreateSubForCustomerQuoteShippingAddressParams"
        ]
        contract_term: NotRequired["Quote.CreateSubForCustomerQuoteContractTermParams"]
        coupon_ids: NotRequired[List[str]]

    class EditCreateSubForCustomerQuoteParams(TypedDict):
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: Required["Quote.EditCreateSubForCustomerQuoteSubscriptionParams"]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List["Quote.EditCreateSubForCustomerQuoteAddonParams"]]
        event_based_addons: NotRequired[
            List["Quote.EditCreateSubForCustomerQuoteEventBasedAddonParams"]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            "Quote.EditCreateSubForCustomerQuoteShippingAddressParams"
        ]
        contract_term: NotRequired[
            "Quote.EditCreateSubForCustomerQuoteContractTermParams"
        ]
        coupon_ids: NotRequired[List[str]]

    class UpdateSubscriptionQuoteParams(TypedDict):
        name: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: Required["Quote.UpdateSubscriptionQuoteSubscriptionParams"]
        addons: NotRequired[List["Quote.UpdateSubscriptionQuoteAddonParams"]]
        event_based_addons: NotRequired[
            List["Quote.UpdateSubscriptionQuoteEventBasedAddonParams"]
        ]
        replace_addon_list: NotRequired[bool]
        mandatory_addons_to_remove: NotRequired[List[str]]
        billing_cycles: NotRequired[int]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        replace_coupon_list: NotRequired[bool]
        change_option: NotRequired[enums.ChangeOption]
        changes_scheduled_at: NotRequired[int]
        force_term_reset: NotRequired[bool]
        reactivate: NotRequired[bool]
        billing_address: NotRequired[
            "Quote.UpdateSubscriptionQuoteBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "Quote.UpdateSubscriptionQuoteShippingAddressParams"
        ]
        customer: NotRequired["Quote.UpdateSubscriptionQuoteCustomerParams"]
        contract_term: NotRequired["Quote.UpdateSubscriptionQuoteContractTermParams"]

    class EditUpdateSubscriptionQuoteParams(TypedDict):
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: NotRequired["Quote.EditUpdateSubscriptionQuoteSubscriptionParams"]
        addons: NotRequired[List["Quote.EditUpdateSubscriptionQuoteAddonParams"]]
        event_based_addons: NotRequired[
            List["Quote.EditUpdateSubscriptionQuoteEventBasedAddonParams"]
        ]
        replace_addon_list: NotRequired[bool]
        mandatory_addons_to_remove: NotRequired[List[str]]
        billing_cycles: NotRequired[int]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        replace_coupon_list: NotRequired[bool]
        change_option: NotRequired[enums.ChangeOption]
        changes_scheduled_at: NotRequired[int]
        force_term_reset: NotRequired[bool]
        reactivate: NotRequired[bool]
        billing_address: NotRequired[
            "Quote.EditUpdateSubscriptionQuoteBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "Quote.EditUpdateSubscriptionQuoteShippingAddressParams"
        ]
        customer: NotRequired["Quote.EditUpdateSubscriptionQuoteCustomerParams"]
        contract_term: NotRequired[
            "Quote.EditUpdateSubscriptionQuoteContractTermParams"
        ]

    class CreateForOnetimeChargesParams(TypedDict):
        name: NotRequired[str]
        customer_id: Required[str]
        po_number: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        currency_code: NotRequired[str]
        addons: NotRequired[List["Quote.CreateForOnetimeChargesAddonParams"]]
        charges: NotRequired[List["Quote.CreateForOnetimeChargesChargeParams"]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        shipping_address: NotRequired[
            "Quote.CreateForOnetimeChargesShippingAddressParams"
        ]
        tax_providers_fields: NotRequired[
            List["Quote.CreateForOnetimeChargesTaxProvidersFieldParams"]
        ]

    class EditOneTimeQuoteParams(TypedDict):
        po_number: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        currency_code: NotRequired[str]
        addons: NotRequired[List["Quote.EditOneTimeQuoteAddonParams"]]
        charges: NotRequired[List["Quote.EditOneTimeQuoteChargeParams"]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        shipping_address: NotRequired["Quote.EditOneTimeQuoteShippingAddressParams"]
        tax_providers_fields: NotRequired[
            List["Quote.EditOneTimeQuoteTaxProvidersFieldParams"]
        ]

    class CreateSubItemsForCustomerQuoteParams(TypedDict):
        name: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: NotRequired[
            "Quote.CreateSubItemsForCustomerQuoteSubscriptionParams"
        ]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List["Quote.CreateSubItemsForCustomerQuoteSubscriptionItemParams"]
        ]
        discounts: Required[List["Quote.CreateSubItemsForCustomerQuoteDiscountParams"]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[
            List["Quote.CreateSubItemsForCustomerQuoteItemTierParams"]
        ]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            "Quote.CreateSubItemsForCustomerQuoteShippingAddressParams"
        ]
        contract_term: NotRequired[
            "Quote.CreateSubItemsForCustomerQuoteContractTermParams"
        ]
        coupon_ids: NotRequired[List[str]]
        billing_start_option: NotRequired[enums.BillingStartOption]
        billing_address: NotRequired[
            "Quote.CreateSubItemsForCustomerQuoteBillingAddressParams"
        ]
        net_term_days: NotRequired[int]
        coupons: NotRequired[List["Quote.CreateSubItemsForCustomerQuoteCouponParams"]]

    class EditCreateSubCustomerQuoteForItemsParams(TypedDict):
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: NotRequired[
            "Quote.EditCreateSubCustomerQuoteForItemsSubscriptionParams"
        ]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List["Quote.EditCreateSubCustomerQuoteForItemsSubscriptionItemParams"]
        ]
        discounts: Required[
            List["Quote.EditCreateSubCustomerQuoteForItemsDiscountParams"]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[
            List["Quote.EditCreateSubCustomerQuoteForItemsItemTierParams"]
        ]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            "Quote.EditCreateSubCustomerQuoteForItemsShippingAddressParams"
        ]
        contract_term: NotRequired[
            "Quote.EditCreateSubCustomerQuoteForItemsContractTermParams"
        ]
        coupon_ids: NotRequired[List[str]]
        billing_start_option: NotRequired[enums.BillingStartOption]
        billing_address: NotRequired[
            "Quote.EditCreateSubCustomerQuoteForItemsBillingAddressParams"
        ]
        net_term_days: NotRequired[int]
        coupons: NotRequired[
            List["Quote.EditCreateSubCustomerQuoteForItemsCouponParams"]
        ]

    class UpdateSubscriptionQuoteForItemsParams(TypedDict):
        name: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: Required[
            "Quote.UpdateSubscriptionQuoteForItemsSubscriptionParams"
        ]
        subscription_items: Required[
            List["Quote.UpdateSubscriptionQuoteForItemsSubscriptionItemParams"]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        discounts: Required[List["Quote.UpdateSubscriptionQuoteForItemsDiscountParams"]]
        item_tiers: NotRequired[
            List["Quote.UpdateSubscriptionQuoteForItemsItemTierParams"]
        ]
        billing_cycles: NotRequired[int]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        replace_coupon_list: NotRequired[bool]
        change_option: NotRequired[enums.ChangeOption]
        changes_scheduled_at: NotRequired[int]
        force_term_reset: NotRequired[bool]
        reactivate: NotRequired[bool]
        billing_address: NotRequired[
            "Quote.UpdateSubscriptionQuoteForItemsBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "Quote.UpdateSubscriptionQuoteForItemsShippingAddressParams"
        ]
        customer: NotRequired["Quote.UpdateSubscriptionQuoteForItemsCustomerParams"]
        contract_term: NotRequired[
            "Quote.UpdateSubscriptionQuoteForItemsContractTermParams"
        ]
        net_term_days: NotRequired[int]
        coupons: NotRequired[List["Quote.UpdateSubscriptionQuoteForItemsCouponParams"]]

    class EditUpdateSubscriptionQuoteForItemsParams(TypedDict):
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription_items: Required[
            List["Quote.EditUpdateSubscriptionQuoteForItemsSubscriptionItemParams"]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        subscription: NotRequired[
            "Quote.EditUpdateSubscriptionQuoteForItemsSubscriptionParams"
        ]
        discounts: Required[
            List["Quote.EditUpdateSubscriptionQuoteForItemsDiscountParams"]
        ]
        item_tiers: NotRequired[
            List["Quote.EditUpdateSubscriptionQuoteForItemsItemTierParams"]
        ]
        billing_cycles: NotRequired[int]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        replace_coupon_list: NotRequired[bool]
        change_option: NotRequired[enums.ChangeOption]
        changes_scheduled_at: NotRequired[int]
        force_term_reset: NotRequired[bool]
        reactivate: NotRequired[bool]
        billing_address: NotRequired[
            "Quote.EditUpdateSubscriptionQuoteForItemsBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "Quote.EditUpdateSubscriptionQuoteForItemsShippingAddressParams"
        ]
        customer: NotRequired["Quote.EditUpdateSubscriptionQuoteForItemsCustomerParams"]
        contract_term: NotRequired[
            "Quote.EditUpdateSubscriptionQuoteForItemsContractTermParams"
        ]
        net_term_days: NotRequired[int]
        coupons: NotRequired[
            List["Quote.EditUpdateSubscriptionQuoteForItemsCouponParams"]
        ]

    class CreateForChargeItemsAndChargesParams(TypedDict):
        name: NotRequired[str]
        customer_id: Required[str]
        po_number: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        currency_code: NotRequired[str]
        item_prices: NotRequired[
            List["Quote.CreateForChargeItemsAndChargesItemPriceParams"]
        ]
        item_tiers: NotRequired[
            List["Quote.CreateForChargeItemsAndChargesItemTierParams"]
        ]
        charges: NotRequired[List["Quote.CreateForChargeItemsAndChargesChargeParams"]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        billing_address: NotRequired[
            "Quote.CreateForChargeItemsAndChargesBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "Quote.CreateForChargeItemsAndChargesShippingAddressParams"
        ]
        discounts: Required[List["Quote.CreateForChargeItemsAndChargesDiscountParams"]]
        tax_providers_fields: NotRequired[
            List["Quote.CreateForChargeItemsAndChargesTaxProvidersFieldParams"]
        ]

    class EditForChargeItemsAndChargesParams(TypedDict):
        po_number: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        currency_code: NotRequired[str]
        item_prices: NotRequired[
            List["Quote.EditForChargeItemsAndChargesItemPriceParams"]
        ]
        item_tiers: NotRequired[
            List["Quote.EditForChargeItemsAndChargesItemTierParams"]
        ]
        charges: NotRequired[List["Quote.EditForChargeItemsAndChargesChargeParams"]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        billing_address: NotRequired[
            "Quote.EditForChargeItemsAndChargesBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "Quote.EditForChargeItemsAndChargesShippingAddressParams"
        ]
        discounts: Required[List["Quote.EditForChargeItemsAndChargesDiscountParams"]]
        tax_providers_fields: NotRequired[
            List["Quote.EditForChargeItemsAndChargesTaxProvidersFieldParams"]
        ]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_deleted: NotRequired[bool]
        id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        subscription_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        date: NotRequired[Filters.TimestampFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class QuoteLineGroupsForQuoteParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class ConvertParams(TypedDict):
        subscription: NotRequired["Quote.ConvertSubscriptionParams"]
        invoice_date: NotRequired[int]
        invoice_immediately: NotRequired[bool]
        create_pending_invoices: NotRequired[bool]
        first_invoice_pending: NotRequired[bool]

    class UpdateStatusParams(TypedDict):
        status: Required["Quote.Status"]
        comment: NotRequired[str]

    class ExtendExpiryDateParams(TypedDict):
        valid_till: Required[int]

    class DeleteParams(TypedDict):
        comment: NotRequired[str]

    class PdfParams(TypedDict):
        consolidated_view: NotRequired[bool]
        disposition_type: NotRequired[enums.DispositionType]

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("quotes", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_sub_for_customer_quote(
        self, id, params: CreateSubForCustomerQuoteParams, headers=None
    ) -> CreateSubForCustomerQuoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "create_subscription_quote"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateSubForCustomerQuoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def edit_create_sub_for_customer_quote(
        self, id, params: EditCreateSubForCustomerQuoteParams, headers=None
    ) -> EditCreateSubForCustomerQuoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_create_subscription_quote"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EditCreateSubForCustomerQuoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_subscription_quote(
        self, params: UpdateSubscriptionQuoteParams, headers=None
    ) -> UpdateSubscriptionQuoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", "update_subscription_quote"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateSubscriptionQuoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def edit_update_subscription_quote(
        self, id, params: EditUpdateSubscriptionQuoteParams = None, headers=None
    ) -> EditUpdateSubscriptionQuoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_update_subscription_quote"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EditUpdateSubscriptionQuoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_for_onetime_charges(
        self, params: CreateForOnetimeChargesParams, headers=None
    ) -> CreateForOnetimeChargesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", "create_for_onetime_charges"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForOnetimeChargesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def edit_one_time_quote(
        self, id, params: EditOneTimeQuoteParams = None, headers=None
    ) -> EditOneTimeQuoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_one_time_quote"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EditOneTimeQuoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_sub_items_for_customer_quote(
        self, id, params: CreateSubItemsForCustomerQuoteParams, headers=None
    ) -> CreateSubItemsForCustomerQuoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "create_subscription_quote_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateSubItemsForCustomerQuoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def edit_create_sub_customer_quote_for_items(
        self, id, params: EditCreateSubCustomerQuoteForItemsParams, headers=None
    ) -> EditCreateSubCustomerQuoteForItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_create_subscription_quote_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EditCreateSubCustomerQuoteForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_subscription_quote_for_items(
        self, params: UpdateSubscriptionQuoteForItemsParams, headers=None
    ) -> UpdateSubscriptionQuoteForItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", "update_subscription_quote_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateSubscriptionQuoteForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def edit_update_subscription_quote_for_items(
        self, id, params: EditUpdateSubscriptionQuoteForItemsParams, headers=None
    ) -> EditUpdateSubscriptionQuoteForItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_update_subscription_quote_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EditUpdateSubscriptionQuoteForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_for_charge_items_and_charges(
        self, params: CreateForChargeItemsAndChargesParams, headers=None
    ) -> CreateForChargeItemsAndChargesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", "create_for_charge_items_and_charges"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForChargeItemsAndChargesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def edit_for_charge_items_and_charges(
        self, id, params: EditForChargeItemsAndChargesParams, headers=None
    ) -> EditForChargeItemsAndChargesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_for_charge_items_and_charges"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EditForChargeItemsAndChargesResponse,
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
            request.uri_path("quotes"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def quote_line_groups_for_quote(
        self, id, params: QuoteLineGroupsForQuoteParams = None, headers=None
    ) -> QuoteLineGroupsForQuoteResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("quotes", id, "quote_line_groups"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            QuoteLineGroupsForQuoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def convert(
        self, id, params: ConvertParams = None, headers=None
    ) -> ConvertResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", id, "convert"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ConvertResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_status(
        self, id, params: UpdateStatusParams, headers=None
    ) -> UpdateStatusResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", id, "update_status"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateStatusResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def extend_expiry_date(
        self, id, params: ExtendExpiryDateParams, headers=None
    ) -> ExtendExpiryDateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("quotes", id, "extend_expiry_date"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ExtendExpiryDateResponse,
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
            request.uri_path("quotes", id, "delete"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            DeleteResponse,
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
            request.uri_path("quotes", id, "pdf"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PdfResponse,
            None,
            False,
            jsonKeys,
            options,
        )
