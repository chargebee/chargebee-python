from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, unbilled_charge, payment_intent, invoice, card


@dataclass
class Subscription:
    env: environment.Environment

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
        OFFER_QUANTITY = "offer_quantity"

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
        current_term_start: NotRequired[int]
        current_term_end: NotRequired[int]
        next_billing_at: NotRequired[int]
        amount_in_decimal: NotRequired[str]
        billing_period: NotRequired[int]
        billing_period_unit: NotRequired[enums.BillingPeriodUnit]
        free_quantity: NotRequired[int]
        free_quantity_in_decimal: NotRequired[str]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        service_period_days: NotRequired[int]
        charge_on_event: NotRequired[enums.ChargeOnEvent]
        charge_once: NotRequired[bool]
        charge_on_option: NotRequired[enums.ChargeOnOption]
        proration_type: NotRequired[enums.ProrationType]
        usage_accumulation_reset_frequency: NotRequired[
            enums.UsageAccumulationResetFrequency
        ]

    class ItemTier(TypedDict):
        item_price_id: Required[str]
        starting_unit: Required[int]
        ending_unit: NotRequired[int]
        price: Required[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]
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

    class ReferralInfo(TypedDict):
        referral_code: NotRequired[str]
        coupon_code: NotRequired[str]
        referrer_id: NotRequired[str]
        external_reference_id: NotRequired[str]
        reward_status: NotRequired["Subscription.ReferralInfoRewardStatus"]
        referral_system: NotRequired[enums.ReferralSystem]
        account_id: Required[str]
        campaign_id: Required[str]
        external_campaign_id: NotRequired[str]
        friend_offer_type: NotRequired[enums.FriendOfferType]
        referrer_reward_type: NotRequired[enums.ReferrerRewardType]
        notify_referral_system: NotRequired[enums.NotifyReferralSystem]
        destination_url: NotRequired[str]
        post_purchase_widget_enabled: Required[bool]

    class BillingOverride(TypedDict):
        max_excess_payment_usage: NotRequired[int]
        max_refundable_credits_usage: NotRequired[int]

    class ContractTerm(TypedDict):
        id: Required[str]
        status: Required["Subscription.ContractTermStatus"]
        contract_start: Required[int]
        contract_end: Required[int]
        billing_cycle: Required[int]
        action_at_term_end: Required["Subscription.ContractTermActionAtTermEnd"]
        total_contract_value: Required[int]
        total_contract_value_before_tax: Required[int]
        cancellation_cutoff_period: NotRequired[int]
        created_at: Required[int]
        subscription_id: Required[str]
        remaining_billing_cycles: NotRequired[int]

    class Discount(TypedDict):
        id: Required[str]
        invoice_name: NotRequired[str]
        type: Required["Subscription.DiscountType"]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        quantity: NotRequired[int]
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
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
        reference_id: NotRequired[str]
        gw_payment_method_id: NotRequired[str]
        additional_information: NotRequired[Dict[Any, Any]]

    class CreateForCustomerContractTermParams(TypedDict):
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
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
        usage_accumulation_reset_frequency: NotRequired[
            enums.UsageAccumulationResetFrequency
        ]

    class CreateWithItemsDiscountParams(TypedDict):
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]

    class CreateWithItemsItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
        reference_id: NotRequired[str]
        gw_payment_method_id: NotRequired[str]
        additional_information: NotRequired[Dict[Any, Any]]

    class CreateWithItemsContractTermParams(TypedDict):
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
        contract_start: NotRequired[int]
        cancellation_cutoff_period: NotRequired[int]

    class CreateWithItemsCouponParams(TypedDict):
        coupon_id: NotRequired[str]
        apply_till: NotRequired[int]

    class CreateWithItemsBillingOverrideParams(TypedDict):
        max_excess_payment_usage: NotRequired[int]
        max_refundable_credits_usage: NotRequired[int]

    class RemoveScheduledCancellationContractTermParams(TypedDict):
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
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
        usage_accumulation_reset_frequency: NotRequired[
            enums.UsageAccumulationResetFrequency
        ]

    class UpdateForItemsDiscountParams(TypedDict):
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

    class UpdateForItemsItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]
        contract_start: NotRequired[int]

    class UpdateForItemsCouponParams(TypedDict):
        coupon_id: NotRequired[str]
        apply_till: NotRequired[int]

    class UpdateForItemsBillingOverrideParams(TypedDict):
        max_excess_payment_usage: NotRequired[int]
        max_refundable_credits_usage: NotRequired[int]

    class ReactivateContractTermParams(TypedDict):
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class ReactivateStatementDescriptorParams(TypedDict):
        descriptor: NotRequired[str]

    class ReactivatePaymentIntentParams(TypedDict):
        id: NotRequired[str]
        gateway_account_id: NotRequired[str]
        gw_token: NotRequired[str]
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
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
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
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
        preferred_scheme: NotRequired["card.Card.PreferredScheme"]
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
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
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
        status: NotRequired["Subscription.ContractTermStatus"]
        total_amount_raised: NotRequired[int]
        total_amount_raised_before_tax: NotRequired[int]
        total_contract_value: NotRequired[int]
        total_contract_value_before_tax: NotRequired[int]
        billing_cycle: NotRequired[int]
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class ImportUnbilledChargesUnbilledChargeParams(TypedDict):
        id: NotRequired[str]
        date_from: Required[int]
        date_to: Required[int]
        entity_type: Required["unbilled_charge.UnbilledCharge.EntityType"]
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
        entity_type: NotRequired["invoice.Invoice.DiscountEntityType"]
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
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]

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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

    class ImportForItemsContractTermParams(TypedDict):
        id: NotRequired[str]
        created_at: NotRequired[int]
        contract_start: NotRequired[int]
        billing_cycle: NotRequired[int]
        total_amount_raised: NotRequired[int]
        total_amount_raised_before_tax: NotRequired[int]
        action_at_term_end: NotRequired["Subscription.ContractTermActionAtTermEnd"]
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
        payment_method_type: NotRequired[
            "payment_intent.PaymentIntent.PaymentMethodType"
        ]
        reference_id: NotRequired[str]
        gw_payment_method_id: NotRequired[str]
        additional_information: NotRequired[Dict[Any, Any]]

    class CreateParams(TypedDict):
        id: NotRequired[str]
        customer: NotRequired["Subscription.CreateCustomerParams"]
        entity_identifiers: NotRequired[
            List["Subscription.CreateEntityIdentifierParams"]
        ]
        tax_providers_fields: NotRequired[
            List["Subscription.CreateTaxProvidersFieldParams"]
        ]
        plan_id: Required[str]
        plan_quantity: NotRequired[int]
        plan_quantity_in_decimal: NotRequired[str]
        plan_unit_price: NotRequired[int]
        plan_unit_price_in_decimal: NotRequired[str]
        setup_fee: NotRequired[int]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List["Subscription.CreateAddonParams"]]
        event_based_addons: NotRequired[
            List["Subscription.CreateEventBasedAddonParams"]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        start_date: NotRequired[int]
        coupon: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        card: NotRequired["Subscription.CreateCardParams"]
        bank_account: NotRequired["Subscription.CreateBankAccountParams"]
        token_id: NotRequired[str]
        payment_method: NotRequired["Subscription.CreatePaymentMethodParams"]
        payment_intent: NotRequired["Subscription.CreatePaymentIntentParams"]
        billing_address: NotRequired["Subscription.CreateBillingAddressParams"]
        shipping_address: NotRequired["Subscription.CreateShippingAddressParams"]
        statement_descriptor: NotRequired[
            "Subscription.CreateStatementDescriptorParams"
        ]
        affiliate_token: NotRequired[str]
        created_from_ip: NotRequired[str]
        invoice_notes: NotRequired[str]
        invoice_date: NotRequired[int]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        contract_term: NotRequired["Subscription.CreateContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        trial_end_action: NotRequired[enums.TrialEndAction]
        client_profile_id: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        coupons: NotRequired[List["Subscription.CreateCouponParams"]]

    class CreateForCustomerParams(TypedDict):
        id: NotRequired[str]
        plan_id: Required[str]
        plan_quantity: NotRequired[int]
        plan_quantity_in_decimal: NotRequired[str]
        plan_unit_price: NotRequired[int]
        plan_unit_price_in_decimal: NotRequired[str]
        setup_fee: NotRequired[int]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List["Subscription.CreateForCustomerAddonParams"]]
        event_based_addons: NotRequired[
            List["Subscription.CreateForCustomerEventBasedAddonParams"]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        start_date: NotRequired[int]
        coupon: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        payment_source_id: NotRequired[str]
        override_relationship: NotRequired[bool]
        shipping_address: NotRequired[
            "Subscription.CreateForCustomerShippingAddressParams"
        ]
        statement_descriptor: NotRequired[
            "Subscription.CreateForCustomerStatementDescriptorParams"
        ]
        invoice_notes: NotRequired[str]
        invoice_date: NotRequired[int]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        replace_primary_payment_source: NotRequired[bool]
        payment_intent: NotRequired["Subscription.CreateForCustomerPaymentIntentParams"]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        contract_term: NotRequired["Subscription.CreateForCustomerContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        trial_end_action: NotRequired[enums.TrialEndAction]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        coupons: NotRequired[List["Subscription.CreateForCustomerCouponParams"]]

    class CreateWithItemsParams(TypedDict):
        id: NotRequired[str]
        business_entity_id: NotRequired[str]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List["Subscription.CreateWithItemsSubscriptionItemParams"]
        ]
        setup_fee: NotRequired[int]
        discounts: Required[List["Subscription.CreateWithItemsDiscountParams"]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[List["Subscription.CreateWithItemsItemTierParams"]]
        net_term_days: NotRequired[int]
        start_date: NotRequired[int]
        coupon: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        payment_source_id: NotRequired[str]
        override_relationship: NotRequired[bool]
        shipping_address: NotRequired[
            "Subscription.CreateWithItemsShippingAddressParams"
        ]
        statement_descriptor: NotRequired[
            "Subscription.CreateWithItemsStatementDescriptorParams"
        ]
        invoice_notes: NotRequired[str]
        invoice_date: NotRequired[int]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        replace_primary_payment_source: NotRequired[bool]
        payment_intent: NotRequired["Subscription.CreateWithItemsPaymentIntentParams"]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        contract_term: NotRequired["Subscription.CreateWithItemsContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        create_pending_invoices: NotRequired[bool]
        auto_close_invoices: NotRequired[bool]
        first_invoice_pending: NotRequired[bool]
        trial_end_action: NotRequired[enums.TrialEndAction]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        coupons: NotRequired[List["Subscription.CreateWithItemsCouponParams"]]
        billing_override: NotRequired[
            "Subscription.CreateWithItemsBillingOverrideParams"
        ]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_deleted: NotRequired[bool]
        id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]
        plan_id: NotRequired[Filters.StringFilter]
        item_id: NotRequired[Filters.StringFilter]
        item_price_id: NotRequired[Filters.StringFilter]
        status: NotRequired[Filters.EnumFilter]
        cancel_reason: NotRequired[Filters.EnumFilter]
        cancel_reason_code: NotRequired[Filters.StringFilter]
        remaining_billing_cycles: NotRequired[Filters.NumberFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        activated_at: NotRequired[Filters.TimestampFilter]
        next_billing_at: NotRequired[Filters.TimestampFilter]
        cancelled_at: NotRequired[Filters.TimestampFilter]
        has_scheduled_changes: NotRequired[Filters.BooleanFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        offline_payment_method: NotRequired[Filters.EnumFilter]
        auto_close_invoices: NotRequired[Filters.BooleanFilter]
        override_relationship: NotRequired[Filters.BooleanFilter]
        sort_by: NotRequired[Filters.SortFilter]
        business_entity_id: NotRequired[Filters.StringFilter]
        channel: NotRequired[Filters.EnumFilter]

    class SubscriptionsForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class ContractTermsForSubscriptionParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        sort_by: NotRequired[Filters.SortFilter]

    class ListDiscountsParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class RemoveScheduledCancellationParams(TypedDict):
        billing_cycles: NotRequired[int]
        contract_term: NotRequired[
            "Subscription.RemoveScheduledCancellationContractTermParams"
        ]
        contract_term_billing_cycle_on_renewal: NotRequired[int]

    class RemoveCouponsParams(TypedDict):
        coupon_ids: NotRequired[List[str]]

    class UpdateParams(TypedDict):
        plan_id: NotRequired[str]
        plan_quantity: NotRequired[int]
        plan_unit_price: NotRequired[int]
        setup_fee: NotRequired[int]
        addons: NotRequired[List["Subscription.UpdateAddonParams"]]
        event_based_addons: NotRequired[
            List["Subscription.UpdateEventBasedAddonParams"]
        ]
        replace_addon_list: NotRequired[bool]
        mandatory_addons_to_remove: NotRequired[List[str]]
        plan_quantity_in_decimal: NotRequired[str]
        plan_unit_price_in_decimal: NotRequired[str]
        invoice_date: NotRequired[int]
        start_date: NotRequired[int]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        coupon: NotRequired[str]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        auto_collection: NotRequired[enums.AutoCollection]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        replace_coupon_list: NotRequired[bool]
        prorate: NotRequired[bool]
        end_of_term: NotRequired[bool]
        force_term_reset: NotRequired[bool]
        reactivate: NotRequired[bool]
        card: NotRequired["Subscription.UpdateCardParams"]
        token_id: NotRequired[str]
        payment_method: NotRequired["Subscription.UpdatePaymentMethodParams"]
        payment_intent: NotRequired["Subscription.UpdatePaymentIntentParams"]
        billing_address: NotRequired["Subscription.UpdateBillingAddressParams"]
        shipping_address: NotRequired["Subscription.UpdateShippingAddressParams"]
        statement_descriptor: NotRequired[
            "Subscription.UpdateStatementDescriptorParams"
        ]
        customer: NotRequired["Subscription.UpdateCustomerParams"]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        override_relationship: NotRequired[bool]
        changes_scheduled_at: NotRequired[int]
        change_option: NotRequired[enums.ChangeOption]
        contract_term: NotRequired["Subscription.UpdateContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        trial_end_action: NotRequired[enums.TrialEndAction]
        coupons: NotRequired[List["Subscription.UpdateCouponParams"]]

    class UpdateForItemsParams(TypedDict):
        subscription_items: Required[
            List["Subscription.UpdateForItemsSubscriptionItemParams"]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        setup_fee: NotRequired[int]
        discounts: Required[List["Subscription.UpdateForItemsDiscountParams"]]
        item_tiers: NotRequired[List["Subscription.UpdateForItemsItemTierParams"]]
        net_term_days: NotRequired[int]
        invoice_date: NotRequired[int]
        start_date: NotRequired[int]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        coupon: NotRequired[str]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        auto_collection: NotRequired[enums.AutoCollection]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        replace_coupon_list: NotRequired[bool]
        prorate: NotRequired[bool]
        end_of_term: NotRequired[bool]
        force_term_reset: NotRequired[bool]
        reactivate: NotRequired[bool]
        card: NotRequired["Subscription.UpdateForItemsCardParams"]
        token_id: NotRequired[str]
        payment_method: NotRequired["Subscription.UpdateForItemsPaymentMethodParams"]
        payment_intent: NotRequired["Subscription.UpdateForItemsPaymentIntentParams"]
        billing_address: NotRequired["Subscription.UpdateForItemsBillingAddressParams"]
        shipping_address: NotRequired[
            "Subscription.UpdateForItemsShippingAddressParams"
        ]
        statement_descriptor: NotRequired[
            "Subscription.UpdateForItemsStatementDescriptorParams"
        ]
        customer: NotRequired["Subscription.UpdateForItemsCustomerParams"]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        override_relationship: NotRequired[bool]
        changes_scheduled_at: NotRequired[int]
        change_option: NotRequired[enums.ChangeOption]
        contract_term: NotRequired["Subscription.UpdateForItemsContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        create_pending_invoices: NotRequired[bool]
        auto_close_invoices: NotRequired[bool]
        trial_end_action: NotRequired[enums.TrialEndAction]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        coupons: NotRequired[List["Subscription.UpdateForItemsCouponParams"]]
        invoice_usages: NotRequired[bool]
        billing_override: NotRequired[
            "Subscription.UpdateForItemsBillingOverrideParams"
        ]

    class ChangeTermEndParams(TypedDict):
        term_ends_at: Required[int]
        prorate: NotRequired[bool]
        invoice_immediately: NotRequired[bool]

    class ReactivateParams(TypedDict):
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        trial_period_days: NotRequired[int]
        reactivate_from: NotRequired[int]
        invoice_immediately: NotRequired[bool]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        terms_to_charge: NotRequired[int]
        invoice_date: NotRequired[int]
        contract_term: NotRequired["Subscription.ReactivateContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        statement_descriptor: NotRequired[
            "Subscription.ReactivateStatementDescriptorParams"
        ]
        payment_intent: NotRequired["Subscription.ReactivatePaymentIntentParams"]

    class AddChargeAtTermEndParams(TypedDict):
        amount: NotRequired[int]
        description: Required[str]
        amount_in_decimal: NotRequired[str]
        avalara_sale_type: NotRequired[enums.AvalaraSaleType]
        avalara_transaction_type: NotRequired[int]
        avalara_service_type: NotRequired[int]
        date_from: NotRequired[int]
        date_to: NotRequired[int]

    class ChargeAddonAtTermEndParams(TypedDict):
        addon_id: Required[str]
        addon_quantity: NotRequired[int]
        addon_unit_price: NotRequired[int]
        addon_quantity_in_decimal: NotRequired[str]
        addon_unit_price_in_decimal: NotRequired[str]
        date_from: NotRequired[int]
        date_to: NotRequired[int]

    class ChargeFutureRenewalsParams(TypedDict):
        terms_to_charge: NotRequired[int]
        specific_dates_schedule: NotRequired[
            List["Subscription.ChargeFutureRenewalsSpecificDatesScheduleParams"]
        ]
        fixed_interval_schedule: NotRequired[
            "Subscription.ChargeFutureRenewalsFixedIntervalScheduleParams"
        ]
        invoice_immediately: NotRequired[bool]
        schedule_type: NotRequired[enums.ScheduleType]

    class EditAdvanceInvoiceScheduleParams(TypedDict):
        terms_to_charge: NotRequired[int]
        schedule_type: NotRequired[enums.ScheduleType]
        specific_dates_schedule: NotRequired[
            List["Subscription.EditAdvanceInvoiceScheduleSpecificDatesScheduleParams"]
        ]
        fixed_interval_schedule: NotRequired[
            "Subscription.EditAdvanceInvoiceScheduleFixedIntervalScheduleParams"
        ]

    class RemoveAdvanceInvoiceScheduleParams(TypedDict):
        specific_dates_schedule: NotRequired[
            List["Subscription.RemoveAdvanceInvoiceScheduleSpecificDatesScheduleParams"]
        ]

    class RegenerateInvoiceParams(TypedDict):
        date_from: NotRequired[int]
        date_to: NotRequired[int]
        prorate: NotRequired[bool]
        invoice_immediately: NotRequired[bool]

    class ImportSubscriptionParams(TypedDict):
        id: NotRequired[str]
        customer: NotRequired["Subscription.ImportSubscriptionCustomerParams"]
        client_profile_id: NotRequired[str]
        plan_id: Required[str]
        plan_quantity: NotRequired[int]
        plan_quantity_in_decimal: NotRequired[str]
        plan_unit_price: NotRequired[int]
        plan_unit_price_in_decimal: NotRequired[str]
        setup_fee: NotRequired[int]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List["Subscription.ImportSubscriptionAddonParams"]]
        event_based_addons: NotRequired[
            List["Subscription.ImportSubscriptionEventBasedAddonParams"]
        ]
        charged_event_based_addons: NotRequired[
            List["Subscription.ImportSubscriptionChargedEventBasedAddonParams"]
        ]
        start_date: NotRequired[int]
        auto_collection: NotRequired[enums.AutoCollection]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        contract_term: NotRequired["Subscription.ImportSubscriptionContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        status: Required["Subscription.Status"]
        current_term_end: NotRequired[int]
        current_term_start: NotRequired[int]
        trial_start: NotRequired[int]
        cancelled_at: NotRequired[int]
        started_at: NotRequired[int]
        activated_at: NotRequired[int]
        pause_date: NotRequired[int]
        resume_date: NotRequired[int]
        create_current_term_invoice: NotRequired[bool]
        card: NotRequired["Subscription.ImportSubscriptionCardParams"]
        payment_method: NotRequired[
            "Subscription.ImportSubscriptionPaymentMethodParams"
        ]
        billing_address: NotRequired[
            "Subscription.ImportSubscriptionBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "Subscription.ImportSubscriptionShippingAddressParams"
        ]
        affiliate_token: NotRequired[str]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        transaction: NotRequired["Subscription.ImportSubscriptionTransactionParams"]
        coupons: NotRequired[List["Subscription.ImportSubscriptionCouponParams"]]

    class ImportForCustomerParams(TypedDict):
        id: NotRequired[str]
        plan_id: Required[str]
        plan_quantity: NotRequired[int]
        plan_quantity_in_decimal: NotRequired[str]
        plan_unit_price: NotRequired[int]
        plan_unit_price_in_decimal: NotRequired[str]
        setup_fee: NotRequired[int]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List["Subscription.ImportForCustomerAddonParams"]]
        event_based_addons: NotRequired[
            List["Subscription.ImportForCustomerEventBasedAddonParams"]
        ]
        charged_event_based_addons: NotRequired[
            List["Subscription.ImportForCustomerChargedEventBasedAddonParams"]
        ]
        start_date: NotRequired[int]
        auto_collection: NotRequired[enums.AutoCollection]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        payment_source_id: NotRequired[str]
        status: Required["Subscription.Status"]
        current_term_end: NotRequired[int]
        current_term_start: NotRequired[int]
        trial_start: NotRequired[int]
        cancelled_at: NotRequired[int]
        started_at: NotRequired[int]
        activated_at: NotRequired[int]
        pause_date: NotRequired[int]
        resume_date: NotRequired[int]
        contract_term: NotRequired["Subscription.ImportForCustomerContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        create_current_term_invoice: NotRequired[bool]
        transaction: NotRequired["Subscription.ImportForCustomerTransactionParams"]
        shipping_address: NotRequired[
            "Subscription.ImportForCustomerShippingAddressParams"
        ]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        coupons: NotRequired[List["Subscription.ImportForCustomerCouponParams"]]

    class ImportContractTermParams(TypedDict):
        contract_term: NotRequired["Subscription.ImportContractTermContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]

    class ImportUnbilledChargesParams(TypedDict):
        unbilled_charges: Required[
            List["Subscription.ImportUnbilledChargesUnbilledChargeParams"]
        ]
        discounts: Required[List["Subscription.ImportUnbilledChargesDiscountParams"]]
        tiers: Required[List["Subscription.ImportUnbilledChargesTierParams"]]

    class ImportForItemsParams(TypedDict):
        exhausted_coupon_ids: NotRequired[List[str]]
        id: NotRequired[str]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List["Subscription.ImportForItemsSubscriptionItemParams"]
        ]
        setup_fee: NotRequired[int]
        discounts: Required[List["Subscription.ImportForItemsDiscountParams"]]
        charged_items: NotRequired[List["Subscription.ImportForItemsChargedItemParams"]]
        item_tiers: NotRequired[List["Subscription.ImportForItemsItemTierParams"]]
        net_term_days: NotRequired[int]
        start_date: NotRequired[int]
        auto_collection: NotRequired[enums.AutoCollection]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        payment_source_id: NotRequired[str]
        status: Required["Subscription.Status"]
        current_term_end: NotRequired[int]
        current_term_start: NotRequired[int]
        trial_start: NotRequired[int]
        cancelled_at: NotRequired[int]
        started_at: NotRequired[int]
        activated_at: NotRequired[int]
        pause_date: NotRequired[int]
        resume_date: NotRequired[int]
        contract_term: NotRequired["Subscription.ImportForItemsContractTermParams"]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        create_current_term_invoice: NotRequired[bool]
        transaction: NotRequired["Subscription.ImportForItemsTransactionParams"]
        shipping_address: NotRequired[
            "Subscription.ImportForItemsShippingAddressParams"
        ]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        cancel_reason_code: NotRequired[str]
        create_pending_invoices: NotRequired[bool]
        auto_close_invoices: NotRequired[bool]
        coupons: NotRequired[List["Subscription.ImportForItemsCouponParams"]]

    class OverrideBillingProfileParams(TypedDict):
        payment_source_id: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]

    class PauseParams(TypedDict):
        pause_option: NotRequired[enums.PauseOption]
        pause_date: NotRequired[int]
        unbilled_charges_handling: NotRequired[enums.UnbilledChargesHandling]
        invoice_dunning_handling: NotRequired[enums.InvoiceDunningHandling]
        skip_billing_cycles: NotRequired[int]
        resume_date: NotRequired[int]

    class CancelParams(TypedDict):
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
            List["Subscription.CancelEventBasedAddonParams"]
        ]
        cancel_reason_code: NotRequired[str]

    class CancelForItemsParams(TypedDict):
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
            List["Subscription.CancelForItemsSubscriptionItemParams"]
        ]
        cancel_reason_code: NotRequired[str]

    class ResumeParams(TypedDict):
        resume_option: NotRequired[enums.ResumeOption]
        resume_date: NotRequired[int]
        charges_handling: NotRequired[enums.ChargesHandling]
        unpaid_invoices_handling: NotRequired[enums.UnpaidInvoicesHandling]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        payment_intent: NotRequired["Subscription.ResumePaymentIntentParams"]

    class MoveParams(TypedDict):
        to_customer_id: Required[str]
        copy_payment_source: NotRequired[bool]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "meta_data": 0,
            "exemption_details": 1,
            "additional_information": 1,
            "billing_address": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_for_customer(
        self, id, params: CreateForCustomerParams, headers=None
    ) -> CreateForCustomerResponse:
        jsonKeys = {
            "meta_data": 0,
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "subscriptions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_with_items(
        self, id, params: CreateWithItemsParams, headers=None
    ) -> CreateWithItemsResponse:
        jsonKeys = {
            "meta_data": 0,
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "subscription_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateWithItemsResponse,
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
            request.uri_path("subscriptions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def subscriptions_for_customer(
        self, id, params: SubscriptionsForCustomerParams = None, headers=None
    ) -> SubscriptionsForCustomerResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "subscriptions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            SubscriptionsForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def contract_terms_for_subscription(
        self, id, params: ContractTermsForSubscriptionParams = None, headers=None
    ) -> ContractTermsForSubscriptionResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "contract_terms"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ContractTermsForSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def list_discounts(
        self, id, params: ListDiscountsParams = None, headers=None
    ) -> ListDiscountsResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "discounts"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListDiscountsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve_with_scheduled_changes(
        self, id, headers=None
    ) -> RetrieveWithScheduledChangesResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "retrieve_with_scheduled_changes"),
            self.env,
            None,
            headers,
            RetrieveWithScheduledChangesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_scheduled_changes(
        self, id, headers=None
    ) -> RemoveScheduledChangesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_scheduled_changes"),
            self.env,
            None,
            headers,
            RemoveScheduledChangesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_scheduled_cancellation(
        self, id, params: RemoveScheduledCancellationParams = None, headers=None
    ) -> RemoveScheduledCancellationResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_scheduled_cancellation"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RemoveScheduledCancellationResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_coupons(
        self, id, params: RemoveCouponsParams = None, headers=None
    ) -> RemoveCouponsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_coupons"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RemoveCouponsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {
            "meta_data": 0,
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_for_items(
        self, id, params: UpdateForItemsParams, headers=None
    ) -> UpdateForItemsResponse:
        jsonKeys = {
            "meta_data": 0,
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "update_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def change_term_end(
        self, id, params: ChangeTermEndParams, headers=None
    ) -> ChangeTermEndResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "change_term_end"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ChangeTermEndResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def reactivate(
        self, id, params: ReactivateParams = None, headers=None
    ) -> ReactivateResponse:
        jsonKeys = {
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "reactivate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ReactivateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def add_charge_at_term_end(
        self, id, params: AddChargeAtTermEndParams, headers=None
    ) -> AddChargeAtTermEndResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "add_charge_at_term_end"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddChargeAtTermEndResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def charge_addon_at_term_end(
        self, id, params: ChargeAddonAtTermEndParams, headers=None
    ) -> ChargeAddonAtTermEndResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "charge_addon_at_term_end"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ChargeAddonAtTermEndResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def charge_future_renewals(
        self, id, params: ChargeFutureRenewalsParams = None, headers=None
    ) -> ChargeFutureRenewalsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "charge_future_renewals"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ChargeFutureRenewalsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def edit_advance_invoice_schedule(
        self, id, params: EditAdvanceInvoiceScheduleParams = None, headers=None
    ) -> EditAdvanceInvoiceScheduleResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "edit_advance_invoice_schedule"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EditAdvanceInvoiceScheduleResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve_advance_invoice_schedule(
        self, id, headers=None
    ) -> RetrieveAdvanceInvoiceScheduleResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "retrieve_advance_invoice_schedule"),
            self.env,
            None,
            headers,
            RetrieveAdvanceInvoiceScheduleResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_advance_invoice_schedule(
        self, id, params: RemoveAdvanceInvoiceScheduleParams = None, headers=None
    ) -> RemoveAdvanceInvoiceScheduleResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_advance_invoice_schedule"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RemoveAdvanceInvoiceScheduleResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def regenerate_invoice(
        self, id, params: RegenerateInvoiceParams = None, headers=None
    ) -> RegenerateInvoiceResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "regenerate_invoice"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RegenerateInvoiceResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def import_subscription(
        self, params: ImportSubscriptionParams, headers=None
    ) -> ImportSubscriptionResponse:
        jsonKeys = {
            "meta_data": 0,
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", "import_subscription"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def import_for_customer(
        self, id, params: ImportForCustomerParams, headers=None
    ) -> ImportForCustomerResponse:
        jsonKeys = {
            "meta_data": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "import_subscription"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def import_contract_term(
        self, id, params: ImportContractTermParams = None, headers=None
    ) -> ImportContractTermResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "import_contract_term"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportContractTermResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def import_unbilled_charges(
        self, id, params: ImportUnbilledChargesParams, headers=None
    ) -> ImportUnbilledChargesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "import_unbilled_charges"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportUnbilledChargesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def import_for_items(
        self, id, params: ImportForItemsParams, headers=None
    ) -> ImportForItemsResponse:
        jsonKeys = {
            "meta_data": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("customers", id, "import_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ImportForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def override_billing_profile(
        self, id, params: OverrideBillingProfileParams = None, headers=None
    ) -> OverrideBillingProfileResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "override_billing_profile"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            OverrideBillingProfileResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def pause(self, id, params: PauseParams = None, headers=None) -> PauseResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "pause"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PauseResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def cancel(self, id, params: CancelParams = None, headers=None) -> CancelResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "cancel"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CancelResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def cancel_for_items(
        self, id, params: CancelForItemsParams = None, headers=None
    ) -> CancelForItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "cancel_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CancelForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def resume(self, id, params: ResumeParams = None, headers=None) -> ResumeResponse:
        jsonKeys = {
            "additional_information": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "resume"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ResumeResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_scheduled_pause(self, id, headers=None) -> RemoveScheduledPauseResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_scheduled_pause"),
            self.env,
            None,
            headers,
            RemoveScheduledPauseResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def remove_scheduled_resumption(
        self, id, headers=None
    ) -> RemoveScheduledResumptionResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_scheduled_resumption"),
            self.env,
            None,
            headers,
            RemoveScheduledResumptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def move(self, id, params: MoveParams, headers=None) -> MoveResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "move"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            MoveResponse,
            None,
            False,
            jsonKeys,
            options,
        )
