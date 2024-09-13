from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class Estimate:

    class CreateSubscriptionParams(TypedDict):
        subscription: Required[CreateSubscriptionSubscriptionParams]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List[CreateSubscriptionAddonParams]]
        event_based_addons: NotRequired[List[CreateSubscriptionEventBasedAddonParams]]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        billing_address: NotRequired[CreateSubscriptionBillingAddressParams]
        shipping_address: NotRequired[CreateSubscriptionShippingAddressParams]
        customer: NotRequired[CreateSubscriptionCustomerParams]
        invoice_immediately: NotRequired[bool]
        invoice_date: NotRequired[int]
        contract_term: NotRequired[CreateSubscriptionContractTermParams]
        tax_providers_fields: NotRequired[
            List[CreateSubscriptionTaxProvidersFieldParams]
        ]
        client_profile_id: NotRequired[str]

    class CreateSubItemEstimateParams(TypedDict):
        subscription: NotRequired[CreateSubItemEstimateSubscriptionParams]
        billing_cycles: NotRequired[int]
        subscription_items: Required[List[CreateSubItemEstimateSubscriptionItemParams]]
        discounts: Required[List[CreateSubItemEstimateDiscountParams]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[List[CreateSubItemEstimateItemTierParams]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        billing_address: NotRequired[CreateSubItemEstimateBillingAddressParams]
        shipping_address: NotRequired[CreateSubItemEstimateShippingAddressParams]
        customer: NotRequired[CreateSubItemEstimateCustomerParams]
        invoice_immediately: NotRequired[bool]
        invoice_date: NotRequired[int]
        client_profile_id: NotRequired[str]
        contract_term: NotRequired[CreateSubItemEstimateContractTermParams]
        tax_providers_fields: NotRequired[
            List[CreateSubItemEstimateTaxProvidersFieldParams]
        ]

    class CreateSubForCustomerEstimateParams(TypedDict):
        use_existing_balances: NotRequired[bool]
        subscription: NotRequired[CreateSubForCustomerEstimateSubscriptionParams]
        invoice_immediately: NotRequired[bool]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List[CreateSubForCustomerEstimateAddonParams]]
        event_based_addons: NotRequired[
            List[CreateSubForCustomerEstimateEventBasedAddonParams]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[CreateSubForCustomerEstimateShippingAddressParams]
        invoice_date: NotRequired[int]
        coupon_ids: NotRequired[List[str]]
        contract_term: NotRequired[CreateSubForCustomerEstimateContractTermParams]

    class CreateSubItemForCustomerEstimateParams(TypedDict):
        use_existing_balances: NotRequired[bool]
        subscription: NotRequired[CreateSubItemForCustomerEstimateSubscriptionParams]
        invoice_immediately: NotRequired[bool]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List[CreateSubItemForCustomerEstimateSubscriptionItemParams]
        ]
        discounts: Required[List[CreateSubItemForCustomerEstimateDiscountParams]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[List[CreateSubItemForCustomerEstimateItemTierParams]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            CreateSubItemForCustomerEstimateShippingAddressParams
        ]
        billing_address: NotRequired[
            CreateSubItemForCustomerEstimateBillingAddressParams
        ]
        invoice_date: NotRequired[int]
        coupon_ids: NotRequired[List[str]]
        contract_term: NotRequired[CreateSubItemForCustomerEstimateContractTermParams]

    class UpdateSubscriptionParams(TypedDict):
        subscription: Required[UpdateSubscriptionSubscriptionParams]
        changes_scheduled_at: NotRequired[int]
        change_option: NotRequired[enums.ChangeOption]
        addons: NotRequired[List[UpdateSubscriptionAddonParams]]
        event_based_addons: NotRequired[List[UpdateSubscriptionEventBasedAddonParams]]
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
        billing_address: NotRequired[UpdateSubscriptionBillingAddressParams]
        shipping_address: NotRequired[UpdateSubscriptionShippingAddressParams]
        customer: NotRequired[UpdateSubscriptionCustomerParams]
        invoice_immediately: NotRequired[bool]

    class UpdateSubscriptionForItemsParams(TypedDict):
        subscription: Required[UpdateSubscriptionForItemsSubscriptionParams]
        changes_scheduled_at: NotRequired[int]
        change_option: NotRequired[enums.ChangeOption]
        subscription_items: Required[
            List[UpdateSubscriptionForItemsSubscriptionItemParams]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        discounts: Required[List[UpdateSubscriptionForItemsDiscountParams]]
        item_tiers: NotRequired[List[UpdateSubscriptionForItemsItemTierParams]]
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
        billing_address: NotRequired[UpdateSubscriptionForItemsBillingAddressParams]
        shipping_address: NotRequired[UpdateSubscriptionForItemsShippingAddressParams]
        customer: NotRequired[UpdateSubscriptionForItemsCustomerParams]
        invoice_immediately: NotRequired[bool]
        invoice_usages: NotRequired[bool]

    class RenewalEstimateParams(TypedDict):
        include_delayed_charges: NotRequired[bool]
        use_existing_balances: NotRequired[bool]
        ignore_scheduled_cancellation: NotRequired[bool]
        ignore_scheduled_changes: NotRequired[bool]

    class AdvanceInvoiceEstimateParams(TypedDict):
        terms_to_charge: NotRequired[int]
        specific_dates_schedule: NotRequired[
            List[AdvanceInvoiceEstimateSpecificDatesScheduleParams]
        ]
        fixed_interval_schedule: NotRequired[
            AdvanceInvoiceEstimateFixedIntervalScheduleParams
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
        event_based_addons: NotRequired[List[CancelSubscriptionEventBasedAddonParams]]
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
            List[CancelSubscriptionForItemsSubscriptionItemParams]
        ]
        cancel_reason_code: NotRequired[str]

    class PauseSubscriptionParams(TypedDict):
        pause_option: NotRequired[enums.PauseOption]
        subscription: NotRequired[PauseSubscriptionSubscriptionParams]
        unbilled_charges_handling: NotRequired[enums.UnbilledChargesHandling]

    class ResumeSubscriptionParams(TypedDict):
        resume_option: NotRequired[enums.ResumeOption]
        subscription: NotRequired[ResumeSubscriptionSubscriptionParams]
        charges_handling: NotRequired[enums.ChargesHandling]

    class GiftSubscriptionParams(TypedDict):
        gift: NotRequired[GiftSubscriptionGiftParams]
        gifter: Required[GiftSubscriptionGifterParams]
        gift_receiver: Required[GiftSubscriptionGiftReceiverParams]
        coupon_ids: NotRequired[List[str]]
        payment_intent: NotRequired[GiftSubscriptionPaymentIntentParams]
        shipping_address: NotRequired[GiftSubscriptionShippingAddressParams]
        subscription: Required[GiftSubscriptionSubscriptionParams]
        addons: NotRequired[List[GiftSubscriptionAddonParams]]

    class GiftSubscriptionForItemsParams(TypedDict):
        gift: NotRequired[GiftSubscriptionForItemsGiftParams]
        gifter: Required[GiftSubscriptionForItemsGifterParams]
        gift_receiver: Required[GiftSubscriptionForItemsGiftReceiverParams]
        coupon_ids: NotRequired[List[str]]
        payment_intent: NotRequired[GiftSubscriptionForItemsPaymentIntentParams]
        shipping_address: NotRequired[GiftSubscriptionForItemsShippingAddressParams]
        subscription_items: NotRequired[
            List[GiftSubscriptionForItemsSubscriptionItemParams]
        ]

    class CreateInvoiceParams(TypedDict):
        invoice: NotRequired[CreateInvoiceInvoiceParams]
        currency_code: NotRequired[str]
        addons: NotRequired[List[CreateInvoiceAddonParams]]
        charges: NotRequired[List[CreateInvoiceChargeParams]]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[List[CreateInvoiceNotesToRemoveParams]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        invoice_date: NotRequired[int]
        shipping_address: NotRequired[CreateInvoiceShippingAddressParams]
        tax_providers_fields: NotRequired[List[CreateInvoiceTaxProvidersFieldParams]]

    class CreateInvoiceForItemsParams(TypedDict):
        invoice: NotRequired[CreateInvoiceForItemsInvoiceParams]
        currency_code: NotRequired[str]
        item_prices: NotRequired[List[CreateInvoiceForItemsItemPriceParams]]
        item_tiers: NotRequired[List[CreateInvoiceForItemsItemTierParams]]
        charges: NotRequired[List[CreateInvoiceForItemsChargeParams]]
        invoice_note: NotRequired[str]
        remove_general_note: NotRequired[bool]
        notes_to_remove: NotRequired[List[CreateInvoiceForItemsNotesToRemoveParams]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        authorization_transaction_id: NotRequired[str]
        payment_source_id: NotRequired[str]
        auto_collection: NotRequired[enums.AutoCollection]
        discounts: Required[List[CreateInvoiceForItemsDiscountParams]]
        shipping_address: NotRequired[CreateInvoiceForItemsShippingAddressParams]
        tax_providers_fields: NotRequired[
            List[CreateInvoiceForItemsTaxProvidersFieldParams]
        ]
        invoice_date: NotRequired[int]

    @staticmethod
    def create_subscription(
        params: CreateSubscriptionParams, env=None, headers=None
    ) -> CreateSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("estimates", "create_subscription"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateSubscriptionResponse,
        )

    @staticmethod
    def create_sub_item_estimate(
        params: CreateSubItemEstimateParams, env=None, headers=None
    ) -> CreateSubItemEstimateResponse:
        return request.send(
            "post",
            request.uri_path("estimates", "create_subscription_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateSubItemEstimateResponse,
        )

    @staticmethod
    def create_sub_for_customer_estimate(
        id, params: CreateSubForCustomerEstimateParams, env=None, headers=None
    ) -> CreateSubForCustomerEstimateResponse:
        return request.send(
            "get",
            request.uri_path("customers", id, "create_subscription_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateSubForCustomerEstimateResponse,
        )

    @staticmethod
    def create_sub_item_for_customer_estimate(
        id, params: CreateSubItemForCustomerEstimateParams, env=None, headers=None
    ) -> CreateSubItemForCustomerEstimateResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "create_subscription_for_items_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateSubItemForCustomerEstimateResponse,
        )

    @staticmethod
    def update_subscription(
        params: UpdateSubscriptionParams, env=None, headers=None
    ) -> UpdateSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("estimates", "update_subscription"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateSubscriptionResponse,
        )

    @staticmethod
    def update_subscription_for_items(
        params: UpdateSubscriptionForItemsParams, env=None, headers=None
    ) -> UpdateSubscriptionForItemsResponse:
        return request.send(
            "post",
            request.uri_path("estimates", "update_subscription_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateSubscriptionForItemsResponse,
        )

    @staticmethod
    def renewal_estimate(
        id, params: RenewalEstimateParams = None, env=None, headers=None
    ) -> RenewalEstimateResponse:
        return request.send(
            "get",
            request.uri_path("subscriptions", id, "renewal_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RenewalEstimateResponse,
        )

    @staticmethod
    def advance_invoice_estimate(
        id, params: AdvanceInvoiceEstimateParams = None, env=None, headers=None
    ) -> AdvanceInvoiceEstimateResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "advance_invoice_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AdvanceInvoiceEstimateResponse,
        )

    @staticmethod
    def regenerate_invoice_estimate(
        id, params: RegenerateInvoiceEstimateParams = None, env=None, headers=None
    ) -> RegenerateInvoiceEstimateResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "regenerate_invoice_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RegenerateInvoiceEstimateResponse,
        )

    @staticmethod
    def upcoming_invoices_estimate(
        id, env=None, headers=None
    ) -> UpcomingInvoicesEstimateResponse:
        return request.send(
            "get",
            request.uri_path("customers", id, "upcoming_invoices_estimate"),
            None,
            env,
            headers,
            UpcomingInvoicesEstimateResponse,
        )

    @staticmethod
    def change_term_end(
        id, params: ChangeTermEndParams, env=None, headers=None
    ) -> ChangeTermEndResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "change_term_end_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ChangeTermEndResponse,
        )

    @staticmethod
    def cancel_subscription(
        id, params: CancelSubscriptionParams = None, env=None, headers=None
    ) -> CancelSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "cancel_subscription_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CancelSubscriptionResponse,
        )

    @staticmethod
    def cancel_subscription_for_items(
        id, params: CancelSubscriptionForItemsParams = None, env=None, headers=None
    ) -> CancelSubscriptionForItemsResponse:
        return request.send(
            "post",
            request.uri_path(
                "subscriptions", id, "cancel_subscription_for_items_estimate"
            ),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CancelSubscriptionForItemsResponse,
        )

    @staticmethod
    def pause_subscription(
        id, params: PauseSubscriptionParams = None, env=None, headers=None
    ) -> PauseSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "pause_subscription_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PauseSubscriptionResponse,
        )

    @staticmethod
    def resume_subscription(
        id, params: ResumeSubscriptionParams = None, env=None, headers=None
    ) -> ResumeSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("subscriptions", id, "resume_subscription_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ResumeSubscriptionResponse,
        )

    @staticmethod
    def gift_subscription(
        params: GiftSubscriptionParams, env=None, headers=None
    ) -> GiftSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("estimates", "gift_subscription"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            GiftSubscriptionResponse,
        )

    @staticmethod
    def gift_subscription_for_items(
        params: GiftSubscriptionForItemsParams, env=None, headers=None
    ) -> GiftSubscriptionForItemsResponse:
        return request.send(
            "post",
            request.uri_path("estimates", "gift_subscription_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            GiftSubscriptionForItemsResponse,
        )

    @staticmethod
    def create_invoice(
        params: CreateInvoiceParams = None, env=None, headers=None
    ) -> CreateInvoiceResponse:
        return request.send(
            "post",
            request.uri_path("estimates", "create_invoice"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateInvoiceResponse,
        )

    @staticmethod
    def create_invoice_for_items(
        params: CreateInvoiceForItemsParams, env=None, headers=None
    ) -> CreateInvoiceForItemsResponse:
        return request.send(
            "post",
            request.uri_path("estimates", "create_invoice_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateInvoiceForItemsResponse,
        )
