from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class Subscription:

    class CreateParams(TypedDict):
        id: NotRequired[str]
        customer: NotRequired[CreateCustomerParams]
        entity_identifiers: NotRequired[List[CreateEntityIdentifierParams]]
        tax_providers_fields: NotRequired[List[CreateTaxProvidersFieldParams]]
        plan_id: Required[str]
        plan_quantity: NotRequired[int]
        plan_quantity_in_decimal: NotRequired[str]
        plan_unit_price: NotRequired[int]
        plan_unit_price_in_decimal: NotRequired[str]
        setup_fee: NotRequired[int]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List[CreateAddonParams]]
        event_based_addons: NotRequired[List[CreateEventBasedAddonParams]]
        mandatory_addons_to_remove: NotRequired[List[str]]
        start_date: NotRequired[int]
        coupon: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        offline_payment_method: NotRequired[enums.OfflinePaymentMethod]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        card: NotRequired[CreateCardParams]
        bank_account: NotRequired[CreateBankAccountParams]
        token_id: NotRequired[str]
        payment_method: NotRequired[CreatePaymentMethodParams]
        payment_intent: NotRequired[CreatePaymentIntentParams]
        billing_address: NotRequired[CreateBillingAddressParams]
        shipping_address: NotRequired[CreateShippingAddressParams]
        statement_descriptor: NotRequired[CreateStatementDescriptorParams]
        affiliate_token: NotRequired[str]
        created_from_ip: NotRequired[str]
        invoice_notes: NotRequired[str]
        invoice_date: NotRequired[int]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        contract_term: NotRequired[CreateContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        trial_end_action: NotRequired[enums.TrialEndAction]
        client_profile_id: NotRequired[str]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        coupons: NotRequired[List[CreateCouponParams]]

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
        addons: NotRequired[List[CreateForCustomerAddonParams]]
        event_based_addons: NotRequired[List[CreateForCustomerEventBasedAddonParams]]
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
        shipping_address: NotRequired[CreateForCustomerShippingAddressParams]
        statement_descriptor: NotRequired[CreateForCustomerStatementDescriptorParams]
        invoice_notes: NotRequired[str]
        invoice_date: NotRequired[int]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        replace_primary_payment_source: NotRequired[bool]
        payment_intent: NotRequired[CreateForCustomerPaymentIntentParams]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        contract_term: NotRequired[CreateForCustomerContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        trial_end_action: NotRequired[enums.TrialEndAction]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        coupons: NotRequired[List[CreateForCustomerCouponParams]]

    class CreateWithItemsParams(TypedDict):
        id: NotRequired[str]
        business_entity_id: NotRequired[str]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        subscription_items: Required[List[CreateWithItemsSubscriptionItemParams]]
        setup_fee: NotRequired[int]
        discounts: Required[List[CreateWithItemsDiscountParams]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[List[CreateWithItemsItemTierParams]]
        net_term_days: NotRequired[int]
        start_date: NotRequired[int]
        coupon: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        payment_source_id: NotRequired[str]
        override_relationship: NotRequired[bool]
        shipping_address: NotRequired[CreateWithItemsShippingAddressParams]
        statement_descriptor: NotRequired[CreateWithItemsStatementDescriptorParams]
        invoice_notes: NotRequired[str]
        invoice_date: NotRequired[int]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        replace_primary_payment_source: NotRequired[bool]
        payment_intent: NotRequired[CreateWithItemsPaymentIntentParams]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        contract_term: NotRequired[CreateWithItemsContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        create_pending_invoices: NotRequired[bool]
        auto_close_invoices: NotRequired[bool]
        first_invoice_pending: NotRequired[bool]
        trial_end_action: NotRequired[enums.TrialEndAction]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        coupons: NotRequired[List[CreateWithItemsCouponParams]]

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

    class ListDiscountsParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    class RemoveScheduledCancellationParams(TypedDict):
        billing_cycles: NotRequired[int]

    class RemoveCouponsParams(TypedDict):
        coupon_ids: NotRequired[List[str]]

    class UpdateParams(TypedDict):
        plan_id: NotRequired[str]
        plan_quantity: NotRequired[int]
        plan_unit_price: NotRequired[int]
        setup_fee: NotRequired[int]
        addons: NotRequired[List[UpdateAddonParams]]
        event_based_addons: NotRequired[List[UpdateEventBasedAddonParams]]
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
        card: NotRequired[UpdateCardParams]
        token_id: NotRequired[str]
        payment_method: NotRequired[UpdatePaymentMethodParams]
        payment_intent: NotRequired[UpdatePaymentIntentParams]
        billing_address: NotRequired[UpdateBillingAddressParams]
        shipping_address: NotRequired[UpdateShippingAddressParams]
        statement_descriptor: NotRequired[UpdateStatementDescriptorParams]
        customer: NotRequired[UpdateCustomerParams]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        override_relationship: NotRequired[bool]
        changes_scheduled_at: NotRequired[int]
        change_option: NotRequired[enums.ChangeOption]
        contract_term: NotRequired[UpdateContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        trial_end_action: NotRequired[enums.TrialEndAction]
        coupons: NotRequired[List[UpdateCouponParams]]

    class UpdateForItemsParams(TypedDict):
        subscription_items: Required[List[UpdateForItemsSubscriptionItemParams]]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        setup_fee: NotRequired[int]
        discounts: Required[List[UpdateForItemsDiscountParams]]
        item_tiers: NotRequired[List[UpdateForItemsItemTierParams]]
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
        card: NotRequired[UpdateForItemsCardParams]
        token_id: NotRequired[str]
        payment_method: NotRequired[UpdateForItemsPaymentMethodParams]
        payment_intent: NotRequired[UpdateForItemsPaymentIntentParams]
        billing_address: NotRequired[UpdateForItemsBillingAddressParams]
        shipping_address: NotRequired[UpdateForItemsShippingAddressParams]
        statement_descriptor: NotRequired[UpdateForItemsStatementDescriptorParams]
        customer: NotRequired[UpdateForItemsCustomerParams]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        invoice_immediately: NotRequired[bool]
        override_relationship: NotRequired[bool]
        changes_scheduled_at: NotRequired[int]
        change_option: NotRequired[enums.ChangeOption]
        contract_term: NotRequired[UpdateForItemsContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        free_period: NotRequired[int]
        free_period_unit: NotRequired[enums.FreePeriodUnit]
        create_pending_invoices: NotRequired[bool]
        auto_close_invoices: NotRequired[bool]
        trial_end_action: NotRequired[enums.TrialEndAction]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        coupons: NotRequired[List[UpdateForItemsCouponParams]]
        invoice_usages: NotRequired[bool]

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
        contract_term: NotRequired[ReactivateContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        statement_descriptor: NotRequired[ReactivateStatementDescriptorParams]
        payment_intent: NotRequired[ReactivatePaymentIntentParams]

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
            List[ChargeFutureRenewalsSpecificDatesScheduleParams]
        ]
        fixed_interval_schedule: NotRequired[
            ChargeFutureRenewalsFixedIntervalScheduleParams
        ]
        invoice_immediately: NotRequired[bool]
        schedule_type: NotRequired[enums.ScheduleType]

    class EditAdvanceInvoiceScheduleParams(TypedDict):
        terms_to_charge: NotRequired[int]
        schedule_type: NotRequired[enums.ScheduleType]
        specific_dates_schedule: NotRequired[
            List[EditAdvanceInvoiceScheduleSpecificDatesScheduleParams]
        ]
        fixed_interval_schedule: NotRequired[
            EditAdvanceInvoiceScheduleFixedIntervalScheduleParams
        ]

    class RemoveAdvanceInvoiceScheduleParams(TypedDict):
        specific_dates_schedule: NotRequired[
            List[RemoveAdvanceInvoiceScheduleSpecificDatesScheduleParams]
        ]

    class RegenerateInvoiceParams(TypedDict):
        date_from: NotRequired[int]
        date_to: NotRequired[int]
        prorate: NotRequired[bool]
        invoice_immediately: NotRequired[bool]

    class ImportSubscriptionParams(TypedDict):
        id: NotRequired[str]
        customer: NotRequired[ImportSubscriptionCustomerParams]
        client_profile_id: NotRequired[str]
        plan_id: Required[str]
        plan_quantity: NotRequired[int]
        plan_quantity_in_decimal: NotRequired[str]
        plan_unit_price: NotRequired[int]
        plan_unit_price_in_decimal: NotRequired[str]
        setup_fee: NotRequired[int]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List[ImportSubscriptionAddonParams]]
        event_based_addons: NotRequired[List[ImportSubscriptionEventBasedAddonParams]]
        charged_event_based_addons: NotRequired[
            List[ImportSubscriptionChargedEventBasedAddonParams]
        ]
        start_date: NotRequired[int]
        auto_collection: NotRequired[enums.AutoCollection]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        contract_term: NotRequired[ImportSubscriptionContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        status: Required[Status]
        current_term_end: NotRequired[int]
        current_term_start: NotRequired[int]
        trial_start: NotRequired[int]
        cancelled_at: NotRequired[int]
        started_at: NotRequired[int]
        activated_at: NotRequired[int]
        pause_date: NotRequired[int]
        resume_date: NotRequired[int]
        create_current_term_invoice: NotRequired[bool]
        card: NotRequired[ImportSubscriptionCardParams]
        payment_method: NotRequired[ImportSubscriptionPaymentMethodParams]
        billing_address: NotRequired[ImportSubscriptionBillingAddressParams]
        shipping_address: NotRequired[ImportSubscriptionShippingAddressParams]
        affiliate_token: NotRequired[str]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        transaction: NotRequired[ImportSubscriptionTransactionParams]
        coupons: NotRequired[List[ImportSubscriptionCouponParams]]

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
        addons: NotRequired[List[ImportForCustomerAddonParams]]
        event_based_addons: NotRequired[List[ImportForCustomerEventBasedAddonParams]]
        charged_event_based_addons: NotRequired[
            List[ImportForCustomerChargedEventBasedAddonParams]
        ]
        start_date: NotRequired[int]
        auto_collection: NotRequired[enums.AutoCollection]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        payment_source_id: NotRequired[str]
        status: Required[Status]
        current_term_end: NotRequired[int]
        current_term_start: NotRequired[int]
        trial_start: NotRequired[int]
        cancelled_at: NotRequired[int]
        started_at: NotRequired[int]
        activated_at: NotRequired[int]
        pause_date: NotRequired[int]
        resume_date: NotRequired[int]
        contract_term: NotRequired[ImportForCustomerContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        create_current_term_invoice: NotRequired[bool]
        transaction: NotRequired[ImportForCustomerTransactionParams]
        shipping_address: NotRequired[ImportForCustomerShippingAddressParams]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        coupons: NotRequired[List[ImportForCustomerCouponParams]]

    class ImportContractTermParams(TypedDict):
        contract_term: NotRequired[ImportContractTermContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]

    class ImportUnbilledChargesParams(TypedDict):
        unbilled_charges: Required[List[ImportUnbilledChargesUnbilledChargeParams]]
        discounts: Required[List[ImportUnbilledChargesDiscountParams]]
        tiers: Required[List[ImportUnbilledChargesTierParams]]

    class ImportForItemsParams(TypedDict):
        id: NotRequired[str]
        trial_end: NotRequired[int]
        billing_cycles: NotRequired[int]
        subscription_items: Required[List[ImportForItemsSubscriptionItemParams]]
        setup_fee: NotRequired[int]
        discounts: Required[List[ImportForItemsDiscountParams]]
        charged_items: NotRequired[List[ImportForItemsChargedItemParams]]
        item_tiers: NotRequired[List[ImportForItemsItemTierParams]]
        net_term_days: NotRequired[int]
        start_date: NotRequired[int]
        auto_collection: NotRequired[enums.AutoCollection]
        po_number: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        payment_source_id: NotRequired[str]
        status: Required[Status]
        current_term_end: NotRequired[int]
        current_term_start: NotRequired[int]
        trial_start: NotRequired[int]
        cancelled_at: NotRequired[int]
        started_at: NotRequired[int]
        activated_at: NotRequired[int]
        pause_date: NotRequired[int]
        resume_date: NotRequired[int]
        contract_term: NotRequired[ImportForItemsContractTermParams]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        create_current_term_invoice: NotRequired[bool]
        transaction: NotRequired[ImportForItemsTransactionParams]
        shipping_address: NotRequired[ImportForItemsShippingAddressParams]
        invoice_notes: NotRequired[str]
        meta_data: NotRequired[Dict[Any, Any]]
        cancel_reason_code: NotRequired[str]
        create_pending_invoices: NotRequired[bool]
        auto_close_invoices: NotRequired[bool]
        coupons: NotRequired[List[ImportForItemsCouponParams]]

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
        event_based_addons: NotRequired[List[CancelEventBasedAddonParams]]
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
        subscription_items: NotRequired[List[CancelForItemsSubscriptionItemParams]]
        cancel_reason_code: NotRequired[str]

    class ResumeParams(TypedDict):
        resume_option: NotRequired[enums.ResumeOption]
        resume_date: NotRequired[int]
        charges_handling: NotRequired[enums.ChargesHandling]
        unpaid_invoices_handling: NotRequired[enums.UnpaidInvoicesHandling]
        payment_initiator: NotRequired[enums.PaymentInitiator]
        payment_intent: NotRequired[ResumePaymentIntentParams]

    class MoveParams(TypedDict):
        to_customer_id: Required[str]
        copy_payment_source: NotRequired[bool]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def create_for_customer(
        id, params: CreateForCustomerParams, env=None, headers=None
    ) -> CreateForCustomerResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "subscriptions"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForCustomerResponse,
        )

    @staticmethod
    def create_with_items(
        id, params: CreateWithItemsParams, env=None, headers=None
    ) -> CreateWithItemsResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "subscription_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateWithItemsResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("subscriptions"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def subscriptions_for_customer(
        id, params: SubscriptionsForCustomerParams = None, env=None, headers=None
    ) -> SubscriptionsForCustomerResponse:
        return request.send(
            "get",
            request.uri_path("customers", id, "subscriptions"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            SubscriptionsForCustomerResponse,
        )

    @staticmethod
    def contract_terms_for_subscription(
        id, params: ContractTermsForSubscriptionParams = None, env=None, headers=None
    ) -> ContractTermsForSubscriptionResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "contract_terms"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ContractTermsForSubscriptionResponse,
        )

    @staticmethod
    def list_discounts(
        id, params: ListDiscountsParams = None, env=None, headers=None
    ) -> ListDiscountsResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "discounts"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListDiscountsResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def retrieve_with_scheduled_changes(
        id, env=None, headers=None
    ) -> RetrieveWithScheduledChangesResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "retrieve_with_scheduled_changes"),
            None,
            env,
            headers,
            RetrieveWithScheduledChangesResponse,
        )

    @staticmethod
    def remove_scheduled_changes(
        id, env=None, headers=None
    ) -> RemoveScheduledChangesResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_scheduled_changes"),
            None,
            env,
            headers,
            RemoveScheduledChangesResponse,
        )

    @staticmethod
    def remove_scheduled_cancellation(
        id, params: RemoveScheduledCancellationParams = None, env=None, headers=None
    ) -> RemoveScheduledCancellationResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_scheduled_cancellation"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RemoveScheduledCancellationResponse,
        )

    @staticmethod
    def remove_coupons(
        id, params: RemoveCouponsParams = None, env=None, headers=None
    ) -> RemoveCouponsResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_coupons"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RemoveCouponsResponse,
        )

    @staticmethod
    def update(
        id, params: UpdateParams = None, env=None, headers=None
    ) -> UpdateResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateResponse,
        )

    @staticmethod
    def update_for_items(
        id, params: UpdateForItemsParams, env=None, headers=None
    ) -> UpdateForItemsResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "update_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateForItemsResponse,
        )

    @staticmethod
    def change_term_end(
        id, params: ChangeTermEndParams, env=None, headers=None
    ) -> ChangeTermEndResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "change_term_end"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ChangeTermEndResponse,
        )

    @staticmethod
    def reactivate(
        id, params: ReactivateParams = None, env=None, headers=None
    ) -> ReactivateResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "reactivate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ReactivateResponse,
        )

    @staticmethod
    def add_charge_at_term_end(
        id, params: AddChargeAtTermEndParams, env=None, headers=None
    ) -> AddChargeAtTermEndResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "add_charge_at_term_end"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AddChargeAtTermEndResponse,
        )

    @staticmethod
    def charge_addon_at_term_end(
        id, params: ChargeAddonAtTermEndParams, env=None, headers=None
    ) -> ChargeAddonAtTermEndResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "charge_addon_at_term_end"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ChargeAddonAtTermEndResponse,
        )

    @staticmethod
    def charge_future_renewals(
        id, params: ChargeFutureRenewalsParams = None, env=None, headers=None
    ) -> ChargeFutureRenewalsResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "charge_future_renewals"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ChargeFutureRenewalsResponse,
        )

    @staticmethod
    def edit_advance_invoice_schedule(
        id, params: EditAdvanceInvoiceScheduleParams = None, env=None, headers=None
    ) -> EditAdvanceInvoiceScheduleResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "edit_advance_invoice_schedule"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EditAdvanceInvoiceScheduleResponse,
        )

    @staticmethod
    def retrieve_advance_invoice_schedule(
        id, env=None, headers=None
    ) -> RetrieveAdvanceInvoiceScheduleResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "retrieve_advance_invoice_schedule"),
            None,
            env,
            headers,
            RetrieveAdvanceInvoiceScheduleResponse,
        )

    @staticmethod
    def remove_advance_invoice_schedule(
        id, params: RemoveAdvanceInvoiceScheduleParams = None, env=None, headers=None
    ) -> RemoveAdvanceInvoiceScheduleResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_advance_invoice_schedule"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RemoveAdvanceInvoiceScheduleResponse,
        )

    @staticmethod
    def regenerate_invoice(
        id, params: RegenerateInvoiceParams = None, env=None, headers=None
    ) -> RegenerateInvoiceResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "regenerate_invoice"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RegenerateInvoiceResponse,
        )

    @staticmethod
    def import_subscription(
        params: ImportSubscriptionParams, env=None, headers=None
    ) -> ImportSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", "import_subscription"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportSubscriptionResponse,
        )

    @staticmethod
    def import_for_customer(
        id, params: ImportForCustomerParams, env=None, headers=None
    ) -> ImportForCustomerResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "import_subscription"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportForCustomerResponse,
        )

    @staticmethod
    def import_contract_term(
        id, params: ImportContractTermParams = None, env=None, headers=None
    ) -> ImportContractTermResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "import_contract_term"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportContractTermResponse,
        )

    @staticmethod
    def import_unbilled_charges(
        id, params: ImportUnbilledChargesParams, env=None, headers=None
    ) -> ImportUnbilledChargesResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "import_unbilled_charges"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportUnbilledChargesResponse,
        )

    @staticmethod
    def import_for_items(
        id, params: ImportForItemsParams, env=None, headers=None
    ) -> ImportForItemsResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "import_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ImportForItemsResponse,
        )

    @staticmethod
    def override_billing_profile(
        id, params: OverrideBillingProfileParams = None, env=None, headers=None
    ) -> OverrideBillingProfileResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "override_billing_profile"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            OverrideBillingProfileResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def pause(id, params: PauseParams = None, env=None, headers=None) -> PauseResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "pause"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PauseResponse,
        )

    @staticmethod
    def cancel(
        id, params: CancelParams = None, env=None, headers=None
    ) -> CancelResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "cancel"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CancelResponse,
        )

    @staticmethod
    def cancel_for_items(
        id, params: CancelForItemsParams = None, env=None, headers=None
    ) -> CancelForItemsResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "cancel_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CancelForItemsResponse,
        )

    @staticmethod
    def resume(
        id, params: ResumeParams = None, env=None, headers=None
    ) -> ResumeResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "resume"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ResumeResponse,
        )

    @staticmethod
    def remove_scheduled_pause(
        id, env=None, headers=None
    ) -> RemoveScheduledPauseResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_scheduled_pause"),
            None,
            env,
            headers,
            RemoveScheduledPauseResponse,
        )

    @staticmethod
    def remove_scheduled_resumption(
        id, env=None, headers=None
    ) -> RemoveScheduledResumptionResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "remove_scheduled_resumption"),
            None,
            env,
            headers,
            RemoveScheduledResumptionResponse,
        )

    @staticmethod
    def move(id, params: MoveParams, env=None, headers=None) -> MoveResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "move"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            MoveResponse,
        )
