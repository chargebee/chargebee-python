from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums, contract_term


@dataclass
class HostedPage:
    env: environment.Environment

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
        ACCEPT_QUOTE = "accept_quote"
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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        quantity: NotRequired[int]
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
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        invoice_notes: NotRequired[str]
        po_number: NotRequired[str]
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
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]

    class CheckoutNewForItemsItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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

    class CheckoutExistingForItemsItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
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

    class CheckoutNewParams(TypedDict):
        subscription: Required["HostedPage.CheckoutNewSubscriptionParams"]
        customer: NotRequired["HostedPage.CheckoutNewCustomerParams"]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List["HostedPage.CheckoutNewAddonParams"]]
        event_based_addons: NotRequired[
            List["HostedPage.CheckoutNewEventBasedAddonParams"]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        card: NotRequired["HostedPage.CheckoutNewCardParams"]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]
        allow_offline_payment_methods: NotRequired[bool]
        billing_address: NotRequired["HostedPage.CheckoutNewBillingAddressParams"]
        shipping_address: NotRequired["HostedPage.CheckoutNewShippingAddressParams"]
        contract_term: NotRequired["HostedPage.CheckoutNewContractTermParams"]

    class CheckoutOneTimeParams(TypedDict):
        customer: NotRequired["HostedPage.CheckoutOneTimeCustomerParams"]
        addons: NotRequired[List["HostedPage.CheckoutOneTimeAddonParams"]]
        currency_code: NotRequired[str]
        charges: NotRequired[List["HostedPage.CheckoutOneTimeChargeParams"]]
        invoice_note: NotRequired[str]
        invoice: NotRequired["HostedPage.CheckoutOneTimeInvoiceParams"]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        card: NotRequired["HostedPage.CheckoutOneTimeCardParams"]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]
        billing_address: NotRequired["HostedPage.CheckoutOneTimeBillingAddressParams"]
        shipping_address: NotRequired["HostedPage.CheckoutOneTimeShippingAddressParams"]

    class CheckoutOneTimeForItemsParams(TypedDict):
        business_entity_id: NotRequired[str]
        layout: NotRequired[enums.Layout]
        customer: NotRequired["HostedPage.CheckoutOneTimeForItemsCustomerParams"]
        item_prices: NotRequired[
            List["HostedPage.CheckoutOneTimeForItemsItemPriceParams"]
        ]
        item_tiers: NotRequired[
            List["HostedPage.CheckoutOneTimeForItemsItemTierParams"]
        ]
        charges: NotRequired[List["HostedPage.CheckoutOneTimeForItemsChargeParams"]]
        discounts: Required[List["HostedPage.CheckoutOneTimeForItemsDiscountParams"]]
        invoice_note: NotRequired[str]
        invoice: NotRequired["HostedPage.CheckoutOneTimeForItemsInvoiceParams"]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        currency_code: NotRequired[str]
        card: NotRequired["HostedPage.CheckoutOneTimeForItemsCardParams"]
        entity_identifiers: NotRequired[
            List["HostedPage.CheckoutOneTimeForItemsEntityIdentifierParams"]
        ]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        billing_address: NotRequired[
            "HostedPage.CheckoutOneTimeForItemsBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "HostedPage.CheckoutOneTimeForItemsShippingAddressParams"
        ]

    class CheckoutNewForItemsParams(TypedDict):
        subscription: NotRequired["HostedPage.CheckoutNewForItemsSubscriptionParams"]
        layout: NotRequired[enums.Layout]
        customer: NotRequired["HostedPage.CheckoutNewForItemsCustomerParams"]
        business_entity_id: NotRequired[str]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List["HostedPage.CheckoutNewForItemsSubscriptionItemParams"]
        ]
        discounts: Required[List["HostedPage.CheckoutNewForItemsDiscountParams"]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[List["HostedPage.CheckoutNewForItemsItemTierParams"]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        card: NotRequired["HostedPage.CheckoutNewForItemsCardParams"]
        entity_identifiers: NotRequired[
            List["HostedPage.CheckoutNewForItemsEntityIdentifierParams"]
        ]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        allow_offline_payment_methods: NotRequired[bool]
        billing_address: NotRequired[
            "HostedPage.CheckoutNewForItemsBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "HostedPage.CheckoutNewForItemsShippingAddressParams"
        ]
        contract_term: NotRequired["HostedPage.CheckoutNewForItemsContractTermParams"]

    class CheckoutExistingParams(TypedDict):
        subscription: Required["HostedPage.CheckoutExistingSubscriptionParams"]
        addons: NotRequired[List["HostedPage.CheckoutExistingAddonParams"]]
        event_based_addons: NotRequired[
            List["HostedPage.CheckoutExistingEventBasedAddonParams"]
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
        reactivate: NotRequired[bool]
        force_term_reset: NotRequired[bool]
        customer: NotRequired["HostedPage.CheckoutExistingCustomerParams"]
        card: NotRequired["HostedPage.CheckoutExistingCardParams"]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]
        allow_offline_payment_methods: NotRequired[bool]
        contract_term: NotRequired["HostedPage.CheckoutExistingContractTermParams"]

    class CheckoutExistingForItemsParams(TypedDict):
        layout: NotRequired[enums.Layout]
        subscription: Required["HostedPage.CheckoutExistingForItemsSubscriptionParams"]
        subscription_items: Required[
            List["HostedPage.CheckoutExistingForItemsSubscriptionItemParams"]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        discounts: Required[List["HostedPage.CheckoutExistingForItemsDiscountParams"]]
        item_tiers: NotRequired[
            List["HostedPage.CheckoutExistingForItemsItemTierParams"]
        ]
        invoice_date: NotRequired[int]
        billing_cycles: NotRequired[int]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        replace_coupon_list: NotRequired[bool]
        reactivate: NotRequired[bool]
        force_term_reset: NotRequired[bool]
        change_option: NotRequired[enums.ChangeOption]
        changes_scheduled_at: NotRequired[int]
        customer: NotRequired["HostedPage.CheckoutExistingForItemsCustomerParams"]
        entity_identifiers: NotRequired[
            List["HostedPage.CheckoutExistingForItemsEntityIdentifierParams"]
        ]
        card: NotRequired["HostedPage.CheckoutExistingForItemsCardParams"]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        allow_offline_payment_methods: NotRequired[bool]
        contract_term: NotRequired[
            "HostedPage.CheckoutExistingForItemsContractTermParams"
        ]

    class UpdateCardParams(TypedDict):
        customer: Required["HostedPage.UpdateCardCustomerParams"]
        card: NotRequired["HostedPage.UpdateCardCardParams"]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]

    class UpdatePaymentMethodParams(TypedDict):
        customer: Required["HostedPage.UpdatePaymentMethodCustomerParams"]
        card: NotRequired["HostedPage.UpdatePaymentMethodCardParams"]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]

    class ManagePaymentSourcesParams(TypedDict):
        customer: Required["HostedPage.ManagePaymentSourcesCustomerParams"]
        redirect_url: NotRequired[str]
        card: NotRequired["HostedPage.ManagePaymentSourcesCardParams"]

    class CollectNowParams(TypedDict):
        customer: Required["HostedPage.CollectNowCustomerParams"]
        redirect_url: NotRequired[str]
        card: NotRequired["HostedPage.CollectNowCardParams"]
        currency_code: NotRequired[str]

    class AcceptQuoteParams(TypedDict):
        quote: Required["HostedPage.AcceptQuoteQuoteParams"]
        redirect_url: NotRequired[str]
        layout: NotRequired[enums.Layout]

    class ExtendSubscriptionParams(TypedDict):
        subscription: Required["HostedPage.ExtendSubscriptionSubscriptionParams"]
        expiry: NotRequired[int]
        billing_cycle: NotRequired[int]

    class CheckoutGiftParams(TypedDict):
        gifter: NotRequired["HostedPage.CheckoutGiftGifterParams"]
        redirect_url: NotRequired[str]
        subscription: Required["HostedPage.CheckoutGiftSubscriptionParams"]
        addons: NotRequired[List["HostedPage.CheckoutGiftAddonParams"]]
        coupon_ids: NotRequired[List[str]]

    class CheckoutGiftForItemsParams(TypedDict):
        business_entity_id: NotRequired[str]
        gifter: NotRequired["HostedPage.CheckoutGiftForItemsGifterParams"]
        redirect_url: NotRequired[str]
        subscription_items: NotRequired[
            List["HostedPage.CheckoutGiftForItemsSubscriptionItemParams"]
        ]
        coupon_ids: NotRequired[List[str]]

    class ClaimGiftParams(TypedDict):
        gift: Required["HostedPage.ClaimGiftGiftParams"]
        redirect_url: NotRequired[str]
        customer: NotRequired["HostedPage.ClaimGiftCustomerParams"]

    class RetrieveAgreementPdfParams(TypedDict):
        payment_source_id: Required[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        type: NotRequired[Filters.EnumFilter]
        state: NotRequired[Filters.EnumFilter]
        updated_at: NotRequired[Filters.TimestampFilter]

    class PreCancelParams(TypedDict):
        subscription: Required["HostedPage.PreCancelSubscriptionParams"]
        pass_thru_content: NotRequired[str]
        cancel_url: NotRequired[str]
        redirect_url: NotRequired[str]

    class EventsParams(TypedDict):
        event_name: Required[enums.EventName]
        occurred_at: NotRequired[int]
        event_data: Required[Dict[Any, Any]]

    class ViewVoucherParams(TypedDict):
        payment_voucher: Required["HostedPage.ViewVoucherPaymentVoucherParams"]
        customer: NotRequired["HostedPage.ViewVoucherCustomerParams"]

    def checkout_new(
        self, params: CheckoutNewParams, headers=None
    ) -> CheckoutNewResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_new"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CheckoutNewResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def checkout_one_time(
        self, params: CheckoutOneTimeParams = None, headers=None
    ) -> CheckoutOneTimeResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_one_time"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CheckoutOneTimeResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def checkout_one_time_for_items(
        self, params: CheckoutOneTimeForItemsParams, headers=None
    ) -> CheckoutOneTimeForItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_one_time_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CheckoutOneTimeForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def checkout_new_for_items(
        self, params: CheckoutNewForItemsParams, headers=None
    ) -> CheckoutNewForItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_new_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CheckoutNewForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def checkout_existing(
        self, params: CheckoutExistingParams, headers=None
    ) -> CheckoutExistingResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_existing"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CheckoutExistingResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def checkout_existing_for_items(
        self, params: CheckoutExistingForItemsParams, headers=None
    ) -> CheckoutExistingForItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_existing_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CheckoutExistingForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_card(self, params: UpdateCardParams, headers=None) -> UpdateCardResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "update_card"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateCardResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def update_payment_method(
        self, params: UpdatePaymentMethodParams, headers=None
    ) -> UpdatePaymentMethodResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "update_payment_method"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdatePaymentMethodResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def manage_payment_sources(
        self, params: ManagePaymentSourcesParams, headers=None
    ) -> ManagePaymentSourcesResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "manage_payment_sources"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ManagePaymentSourcesResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def collect_now(self, params: CollectNowParams, headers=None) -> CollectNowResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "collect_now"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CollectNowResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def accept_quote(
        self, params: AcceptQuoteParams, headers=None
    ) -> AcceptQuoteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "accept_quote"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AcceptQuoteResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def extend_subscription(
        self, params: ExtendSubscriptionParams, headers=None
    ) -> ExtendSubscriptionResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "extend_subscription"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ExtendSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def checkout_gift(
        self, params: CheckoutGiftParams, headers=None
    ) -> CheckoutGiftResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_gift"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CheckoutGiftResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def checkout_gift_for_items(
        self, params: CheckoutGiftForItemsParams = None, headers=None
    ) -> CheckoutGiftForItemsResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_gift_for_items"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CheckoutGiftForItemsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def claim_gift(self, params: ClaimGiftParams, headers=None) -> ClaimGiftResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "claim_gift"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ClaimGiftResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def retrieve_agreement_pdf(
        self, params: RetrieveAgreementPdfParams, headers=None
    ) -> RetrieveAgreementPdfResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "retrieve_agreement_pdf"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveAgreementPdfResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def acknowledge(self, id, headers=None) -> AcknowledgeResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", id, "acknowledge"),
            self.env,
            None,
            headers,
            AcknowledgeResponse,
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
            request.uri_path("hosted_pages", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
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
            request.uri_path("hosted_pages"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def pre_cancel(self, params: PreCancelParams, headers=None) -> PreCancelResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "pre_cancel"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            PreCancelResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def events(self, params: EventsParams, headers=None) -> EventsResponse:
        jsonKeys = {
            "event_data": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "events"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EventsResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def view_voucher(
        self, params: ViewVoucherParams, headers=None
    ) -> ViewVoucherResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("hosted_pages", "view_voucher"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ViewVoucherResponse,
            None,
            False,
            jsonKeys,
            options,
        )
