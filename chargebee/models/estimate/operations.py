from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import (
    enums,
    payment_intent,
    contract_term,
    subscription_estimate,
    invoice_estimate,
    payment_schedule_estimate,
    credit_note_estimate,
    unbilled_charge,
)


@dataclass
class Estimate:
    env: environment.Environment

    class PaymentScheduleEstimateEntityType(Enum):
        INVOICE = "invoice"

        def __str__(self):
            return self.value

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
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
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]

    class CreateSubItemEstimateItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class CreateSubItemForCustomerEstimateSubscriptionParams(TypedDict):
        id: NotRequired[str]
        trial_end: NotRequired[int]
        setup_fee: NotRequired[int]
        start_date: NotRequired[int]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
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
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]

    class CreateSubItemForCustomerEstimateItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        contract_start: NotRequired[int]
        cancellation_cutoff_period: NotRequired[int]

    class CreateSubItemForCustomerEstimateBillingOverrideParams(TypedDict):
        max_excess_payment_usage: NotRequired[int]
        max_refundable_credits_usage: NotRequired[int]

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

    class UpdateSubscriptionForItemsItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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

    class UpdateSubscriptionForItemsBillingOverrideParams(TypedDict):
        max_excess_payment_usage: NotRequired[int]
        max_refundable_credits_usage: NotRequired[int]

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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        unit_price: NotRequired[int]
        unit_price_in_decimal: NotRequired[str]

    class GiftSubscriptionForItemsItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]

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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        quantity: NotRequired[int]
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

    class CreateInvoiceForItemsBillingAddressParams(TypedDict):
        line1: NotRequired[str]
        line2: NotRequired[str]
        line3: NotRequired[str]
        city: NotRequired[str]
        state_code: NotRequired[str]
        zip: NotRequired[str]
        country: NotRequired[str]
        validation_status: NotRequired[enums.ValidationStatus]

    class CreateSubscriptionParams(TypedDict):
        subscription: Required["Estimate.CreateSubscriptionSubscriptionParams"]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List["Estimate.CreateSubscriptionAddonParams"]]
        event_based_addons: NotRequired[
            List["Estimate.CreateSubscriptionEventBasedAddonParams"]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        billing_address: NotRequired["Estimate.CreateSubscriptionBillingAddressParams"]
        shipping_address: NotRequired[
            "Estimate.CreateSubscriptionShippingAddressParams"
        ]
        customer: NotRequired["Estimate.CreateSubscriptionCustomerParams"]
        invoice_immediately: NotRequired[bool]
        invoice_date: NotRequired[int]
        contract_term: NotRequired["Estimate.CreateSubscriptionContractTermParams"]
        tax_providers_fields: NotRequired[
            List["Estimate.CreateSubscriptionTaxProvidersFieldParams"]
        ]
        client_profile_id: NotRequired[str]

    class CreateSubItemEstimateParams(TypedDict):
        subscription: NotRequired["Estimate.CreateSubItemEstimateSubscriptionParams"]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List["Estimate.CreateSubItemEstimateSubscriptionItemParams"]
        ]
        discounts: Required[List["Estimate.CreateSubItemEstimateDiscountParams"]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[List["Estimate.CreateSubItemEstimateItemTierParams"]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        billing_address: NotRequired[
            "Estimate.CreateSubItemEstimateBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "Estimate.CreateSubItemEstimateShippingAddressParams"
        ]
        customer: NotRequired["Estimate.CreateSubItemEstimateCustomerParams"]
        invoice_immediately: NotRequired[bool]
        invoice_date: NotRequired[int]
        client_profile_id: NotRequired[str]
        contract_term: NotRequired["Estimate.CreateSubItemEstimateContractTermParams"]
        tax_providers_fields: NotRequired[
            List["Estimate.CreateSubItemEstimateTaxProvidersFieldParams"]
        ]

    class CreateSubForCustomerEstimateParams(TypedDict):
        use_existing_balances: NotRequired[bool]
        subscription: NotRequired[
            "Estimate.CreateSubForCustomerEstimateSubscriptionParams"
        ]
        invoice_immediately: NotRequired[bool]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List["Estimate.CreateSubForCustomerEstimateAddonParams"]]
        event_based_addons: NotRequired[
            List["Estimate.CreateSubForCustomerEstimateEventBasedAddonParams"]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            "Estimate.CreateSubForCustomerEstimateShippingAddressParams"
        ]
        invoice_date: NotRequired[int]
        coupon_ids: NotRequired[List[str]]
        contract_term: NotRequired[
            "Estimate.CreateSubForCustomerEstimateContractTermParams"
        ]

    class CreateSubItemForCustomerEstimateParams(TypedDict):
        use_existing_balances: NotRequired[bool]
        subscription: NotRequired[
            "Estimate.CreateSubItemForCustomerEstimateSubscriptionParams"
        ]
        invoice_immediately: NotRequired[bool]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List["Estimate.CreateSubItemForCustomerEstimateSubscriptionItemParams"]
        ]
        discounts: Required[
            List["Estimate.CreateSubItemForCustomerEstimateDiscountParams"]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[
            List["Estimate.CreateSubItemForCustomerEstimateItemTierParams"]
        ]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            "Estimate.CreateSubItemForCustomerEstimateShippingAddressParams"
        ]
        billing_address: NotRequired[
            "Estimate.CreateSubItemForCustomerEstimateBillingAddressParams"
        ]
        invoice_date: NotRequired[int]
        coupon_ids: NotRequired[List[str]]
        contract_term: NotRequired[
            "Estimate.CreateSubItemForCustomerEstimateContractTermParams"
        ]
        billing_override: NotRequired[
            "Estimate.CreateSubItemForCustomerEstimateBillingOverrideParams"
        ]

    class UpdateSubscriptionParams(TypedDict):
        subscription: Required["Estimate.UpdateSubscriptionSubscriptionParams"]
        changes_scheduled_at: NotRequired[int]
        change_option: NotRequired[enums.ChangeOption]
        addons: NotRequired[List["Estimate.UpdateSubscriptionAddonParams"]]
        event_based_addons: NotRequired[
            List["Estimate.UpdateSubscriptionEventBasedAddonParams"]
        ]
        replace_addon_list: NotRequired[bool]
        mandatory_addons_to_remove: NotRequired[List[str]]
        invoice_date: NotRequired[int]
        billing_cycles: NotRequired[int]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        replace_coupon_list: NotRequired[bool]
        prorate: NotRequired[bool]
        end_of_term: NotRequired[bool]
        force_term_reset: NotRequired[bool]
        reactivate: NotRequired[bool]
        include_delayed_charges: NotRequired[bool]
        use_existing_balances: NotRequired[bool]
        billing_address: NotRequired["Estimate.UpdateSubscriptionBillingAddressParams"]
        shipping_address: NotRequired[
            "Estimate.UpdateSubscriptionShippingAddressParams"
        ]
        customer: NotRequired["Estimate.UpdateSubscriptionCustomerParams"]
        invoice_immediately: NotRequired[bool]

    class UpdateSubscriptionForItemsParams(TypedDict):
        subscription: Required["Estimate.UpdateSubscriptionForItemsSubscriptionParams"]
        changes_scheduled_at: NotRequired[int]
        change_option: NotRequired[enums.ChangeOption]
        subscription_items: Required[
            List["Estimate.UpdateSubscriptionForItemsSubscriptionItemParams"]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        discounts: Required[List["Estimate.UpdateSubscriptionForItemsDiscountParams"]]
        item_tiers: NotRequired[
            List["Estimate.UpdateSubscriptionForItemsItemTierParams"]
        ]
        invoice_date: NotRequired[int]
        billing_cycles: NotRequired[int]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        replace_coupon_list: NotRequired[bool]
        prorate: NotRequired[bool]
        end_of_term: NotRequired[bool]
        force_term_reset: NotRequired[bool]
        reactivate: NotRequired[bool]
        include_delayed_charges: NotRequired[bool]
        use_existing_balances: NotRequired[bool]
        billing_address: NotRequired[
            "Estimate.UpdateSubscriptionForItemsBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "Estimate.UpdateSubscriptionForItemsShippingAddressParams"
        ]
        customer: NotRequired["Estimate.UpdateSubscriptionForItemsCustomerParams"]
        invoice_immediately: NotRequired[bool]
        invoice_usages: NotRequired[bool]
        billing_override: NotRequired[
            "Estimate.UpdateSubscriptionForItemsBillingOverrideParams"
        ]

    class RenewalEstimateParams(TypedDict):
        include_delayed_charges: NotRequired[bool]
        use_existing_balances: NotRequired[bool]
        ignore_scheduled_cancellation: NotRequired[bool]
        ignore_scheduled_changes: NotRequired[bool]
        exclude_tax_type: NotRequired[enums.ExcludeTaxType]

    class AdvanceInvoiceEstimateParams(TypedDict):
        terms_to_charge: NotRequired[int]
        specific_dates_schedule: NotRequired[
            List["Estimate.AdvanceInvoiceEstimateSpecificDatesScheduleParams"]
        ]
        fixed_interval_schedule: NotRequired[
            "Estimate.AdvanceInvoiceEstimateFixedIntervalScheduleParams"
        ]
        invoice_immediately: NotRequired[bool]
        schedule_type: NotRequired[enums.ScheduleType]

    class RegenerateInvoiceEstimateParams(TypedDict):
        date_from: NotRequired[int]
        date_to: NotRequired[int]
        prorate: NotRequired[bool]
        invoice_immediately: NotRequired[bool]

    class ChangeTermEndParams(TypedDict):
        term_ends_at: Required[int]
        prorate: NotRequired[bool]
        invoice_immediately: NotRequired[bool]

    class CancelSubscriptionParams(TypedDict):
        cancel_option: NotRequired[enums.CancelOption]
        end_of_term: NotRequired[bool]
        cancel_at: NotRequired[int]
        credit_option_for_current_term_charges: NotRequired[
            enums.CreditOptionForCurrentTermCharges
        ]
        unbilled_charges_option: NotRequired[enums.UnbilledChargesOption]
        account_receivables_handling: NotRequired[enums.AccountReceivablesHandling]
        refundable_credits_handling: NotRequired[enums.RefundableCreditsHandling]
        contract_term_cancel_option: NotRequired[enums.ContractTermCancelOption]
        invoice_date: NotRequired[int]
        event_based_addons: NotRequired[
            List["Estimate.CancelSubscriptionEventBasedAddonParams"]
        ]
        cancel_reason_code: NotRequired[str]

    class CancelSubscriptionForItemsParams(TypedDict):
        cancel_option: NotRequired[enums.CancelOption]
        end_of_term: NotRequired[bool]
        cancel_at: NotRequired[int]
        credit_option_for_current_term_charges: NotRequired[
            enums.CreditOptionForCurrentTermCharges
        ]
        unbilled_charges_option: NotRequired[enums.UnbilledChargesOption]
        account_receivables_handling: NotRequired[enums.AccountReceivablesHandling]
        refundable_credits_handling: NotRequired[enums.RefundableCreditsHandling]
        contract_term_cancel_option: NotRequired[enums.ContractTermCancelOption]
        invoice_date: NotRequired[int]
        subscription_items: NotRequired[
            List["Estimate.CancelSubscriptionForItemsSubscriptionItemParams"]
        ]
        cancel_reason_code: NotRequired[str]

    class PauseSubscriptionParams(TypedDict):
        pause_option: NotRequired[enums.PauseOption]
        subscription: NotRequired["Estimate.PauseSubscriptionSubscriptionParams"]
        unbilled_charges_handling: NotRequired[enums.UnbilledChargesHandling]

    class ResumeSubscriptionParams(TypedDict):
        resume_option: NotRequired[enums.ResumeOption]
        subscription: NotRequired["Estimate.ResumeSubscriptionSubscriptionParams"]
        charges_handling: NotRequired[enums.ChargesHandling]

    class GiftSubscriptionParams(TypedDict):
        gift: NotRequired["Estimate.GiftSubscriptionGiftParams"]
        gifter: Required["Estimate.GiftSubscriptionGifterParams"]
        gift_receiver: Required["Estimate.GiftSubscriptionGiftReceiverParams"]
        coupon_ids: NotRequired[List[str]]
        payment_intent: NotRequired["Estimate.GiftSubscriptionPaymentIntentParams"]
        shipping_address: NotRequired["Estimate.GiftSubscriptionShippingAddressParams"]
        subscription: Required["Estimate.GiftSubscriptionSubscriptionParams"]
        addons: NotRequired[List["Estimate.GiftSubscriptionAddonParams"]]

    class GiftSubscriptionForItemsParams(TypedDict):
        gift: NotRequired["Estimate.GiftSubscriptionForItemsGiftParams"]
        gifter: Required["Estimate.GiftSubscriptionForItemsGifterParams"]
        gift_receiver: Required["Estimate.GiftSubscriptionForItemsGiftReceiverParams"]
        coupon_ids: NotRequired[List[str]]
        payment_intent: NotRequired[
            "Estimate.GiftSubscriptionForItemsPaymentIntentParams"
        ]
        shipping_address: NotRequired[
            "Estimate.GiftSubscriptionForItemsShippingAddressParams"
        ]
        subscription_items: NotRequired[
            List["Estimate.GiftSubscriptionForItemsSubscriptionItemParams"]
        ]
        item_tiers: NotRequired[List["Estimate.GiftSubscriptionForItemsItemTierParams"]]

    class CreateInvoiceParams(TypedDict):
        invoice: NotRequired["Estimate.CreateInvoiceInvoiceParams"]
        currency_code: NotRequired[str]
        addons: NotRequired[List["Estimate.CreateInvoiceAddonParams"]]
        charges: NotRequired[List["Estimate.CreateInvoiceChargeParams"]]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[List["Estimate.CreateInvoiceNotesToRemoveParams"]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        invoice_date: NotRequired[int]
        shipping_address: NotRequired["Estimate.CreateInvoiceShippingAddressParams"]
        tax_providers_fields: NotRequired[
            List["Estimate.CreateInvoiceTaxProvidersFieldParams"]
        ]

    class CreateInvoiceForItemsParams(TypedDict):
        invoice: NotRequired["Estimate.CreateInvoiceForItemsInvoiceParams"]
        currency_code: NotRequired[str]
        item_prices: NotRequired[List["Estimate.CreateInvoiceForItemsItemPriceParams"]]
        item_tiers: NotRequired[List["Estimate.CreateInvoiceForItemsItemTierParams"]]
        charges: NotRequired[List["Estimate.CreateInvoiceForItemsChargeParams"]]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[
            List["Estimate.CreateInvoiceForItemsNotesToRemoveParams"]
        ]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        discounts: Required[List["Estimate.CreateInvoiceForItemsDiscountParams"]]
        shipping_address: NotRequired[
            "Estimate.CreateInvoiceForItemsShippingAddressParams"
        ]
        tax_providers_fields: NotRequired[
            List["Estimate.CreateInvoiceForItemsTaxProvidersFieldParams"]
        ]
        invoice_date: NotRequired[int]
        billing_address: NotRequired[
            "Estimate.CreateInvoiceForItemsBillingAddressParams"
        ]

    class PaymentSchedulesParams(TypedDict):
        scheme_id: Required[str]
        amount: NotRequired[int]
        invoice_id: NotRequired[str]
        payment_schedule_start_date: NotRequired[int]

    def create_subscription(
        self, params: CreateSubscriptionParams, headers=None
    ) -> CreateSubscriptionResponse:
        jsonKeys = {
            "exemption_details": 1,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("estimates", "create_subscription"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_sub_item_estimate(
        self, params: CreateSubItemEstimateParams, headers=None
    ) -> CreateSubItemEstimateResponse:
        jsonKeys = {
            "exemption_details": 1,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("estimates", "create_subscription_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateSubItemEstimateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_sub_for_customer_estimate(
        self, id, params: CreateSubForCustomerEstimateParams, headers=None
    ) -> CreateSubForCustomerEstimateResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "create_subscription_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateSubForCustomerEstimateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_sub_item_for_customer_estimate(
        self, id, params: CreateSubItemForCustomerEstimateParams, headers=None
    ) -> CreateSubItemForCustomerEstimateResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("customers", id, "create_subscription_for_items_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateSubItemForCustomerEstimateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_subscription(
        self, params: UpdateSubscriptionParams, headers=None
    ) -> UpdateSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("estimates", "update_subscription"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_subscription_for_items(
        self, params: UpdateSubscriptionForItemsParams, headers=None
    ) -> UpdateSubscriptionForItemsResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("estimates", "update_subscription_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateSubscriptionForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def renewal_estimate(
        self, id, params: RenewalEstimateParams = None, headers=None
    ) -> RenewalEstimateResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "renewal_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RenewalEstimateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def advance_invoice_estimate(
        self, id, params: AdvanceInvoiceEstimateParams = None, headers=None
    ) -> AdvanceInvoiceEstimateResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "advance_invoice_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AdvanceInvoiceEstimateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def regenerate_invoice_estimate(
        self, id, params: RegenerateInvoiceEstimateParams = None, headers=None
    ) -> RegenerateInvoiceEstimateResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "regenerate_invoice_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RegenerateInvoiceEstimateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def upcoming_invoices_estimate(
        self, id, headers=None
    ) -> UpcomingInvoicesEstimateResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "upcoming_invoices_estimate"),
            self.env,
            None,
            headers,
            UpcomingInvoicesEstimateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def change_term_end(
        self, id, params: ChangeTermEndParams, headers=None
    ) -> ChangeTermEndResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "change_term_end_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ChangeTermEndResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def cancel_subscription(
        self, id, params: CancelSubscriptionParams = None, headers=None
    ) -> CancelSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "cancel_subscription_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CancelSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def cancel_subscription_for_items(
        self, id, params: CancelSubscriptionForItemsParams = None, headers=None
    ) -> CancelSubscriptionForItemsResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path(
                "subscriptions", id, "cancel_subscription_for_items_estimate"
            ),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CancelSubscriptionForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def pause_subscription(
        self, id, params: PauseSubscriptionParams = None, headers=None
    ) -> PauseSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "pause_subscription_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PauseSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def resume_subscription(
        self, id, params: ResumeSubscriptionParams = None, headers=None
    ) -> ResumeSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "resume_subscription_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ResumeSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def gift_subscription(
        self, params: GiftSubscriptionParams, headers=None
    ) -> GiftSubscriptionResponse:
        jsonKeys = {
            "additional_information": 1,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("estimates", "gift_subscription"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            GiftSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def gift_subscription_for_items(
        self, params: GiftSubscriptionForItemsParams, headers=None
    ) -> GiftSubscriptionForItemsResponse:
        jsonKeys = {
            "additional_information": 1,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("estimates", "gift_subscription_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            GiftSubscriptionForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_invoice(
        self, params: CreateInvoiceParams = None, headers=None
    ) -> CreateInvoiceResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("estimates", "create_invoice"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateInvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_invoice_for_items(
        self, params: CreateInvoiceForItemsParams, headers=None
    ) -> CreateInvoiceForItemsResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("estimates", "create_invoice_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateInvoiceForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def payment_schedules(
        self, params: PaymentSchedulesParams, headers=None
    ) -> PaymentSchedulesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("estimates", "payment_schedules"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PaymentSchedulesResponse,
            None,
            False,
            jsonKeys,
            options,
        )
