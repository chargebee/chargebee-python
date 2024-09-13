from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class HostedPage:

    class CheckoutNewParams(TypedDict):
        subscription: Required[CheckoutNewSubscriptionParams]
        customer: NotRequired[CheckoutNewCustomerParams]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List[CheckoutNewAddonParams]]
        event_based_addons: NotRequired[List[CheckoutNewEventBasedAddonParams]]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        card: NotRequired[CheckoutNewCardParams]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]
        allow_offline_payment_methods: NotRequired[bool]
        billing_address: NotRequired[CheckoutNewBillingAddressParams]
        shipping_address: NotRequired[CheckoutNewShippingAddressParams]
        contract_term: NotRequired[CheckoutNewContractTermParams]

    class CheckoutOneTimeParams(TypedDict):
        customer: NotRequired[CheckoutOneTimeCustomerParams]
        addons: NotRequired[List[CheckoutOneTimeAddonParams]]
        currency_code: NotRequired[str]
        charges: NotRequired[List[CheckoutOneTimeChargeParams]]
        invoice_note: NotRequired[str]
        invoice: NotRequired[CheckoutOneTimeInvoiceParams]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        card: NotRequired[CheckoutOneTimeCardParams]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]
        billing_address: NotRequired[CheckoutOneTimeBillingAddressParams]
        shipping_address: NotRequired[CheckoutOneTimeShippingAddressParams]

    class CheckoutOneTimeForItemsParams(TypedDict):
        business_entity_id: NotRequired[str]
        layout: NotRequired[enums.Layout]
        customer: NotRequired[CheckoutOneTimeForItemsCustomerParams]
        item_prices: NotRequired[List[CheckoutOneTimeForItemsItemPriceParams]]
        item_tiers: NotRequired[List[CheckoutOneTimeForItemsItemTierParams]]
        charges: NotRequired[List[CheckoutOneTimeForItemsChargeParams]]
        discounts: Required[List[CheckoutOneTimeForItemsDiscountParams]]
        invoice_note: NotRequired[str]
        invoice: NotRequired[CheckoutOneTimeForItemsInvoiceParams]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        currency_code: NotRequired[str]
        card: NotRequired[CheckoutOneTimeForItemsCardParams]
        entity_identifiers: NotRequired[
            List[CheckoutOneTimeForItemsEntityIdentifierParams]
        ]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        billing_address: NotRequired[CheckoutOneTimeForItemsBillingAddressParams]
        shipping_address: NotRequired[CheckoutOneTimeForItemsShippingAddressParams]

    class CheckoutNewForItemsParams(TypedDict):
        subscription: NotRequired[CheckoutNewForItemsSubscriptionParams]
        layout: NotRequired[enums.Layout]
        customer: NotRequired[CheckoutNewForItemsCustomerParams]
        business_entity_id: NotRequired[str]
        billing_cycles: NotRequired[int]
        subscription_items: Required[List[CheckoutNewForItemsSubscriptionItemParams]]
        discounts: Required[List[CheckoutNewForItemsDiscountParams]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[List[CheckoutNewForItemsItemTierParams]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        card: NotRequired[CheckoutNewForItemsCardParams]
        entity_identifiers: NotRequired[List[CheckoutNewForItemsEntityIdentifierParams]]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        allow_offline_payment_methods: NotRequired[bool]
        billing_address: NotRequired[CheckoutNewForItemsBillingAddressParams]
        shipping_address: NotRequired[CheckoutNewForItemsShippingAddressParams]
        contract_term: NotRequired[CheckoutNewForItemsContractTermParams]

    class CheckoutExistingParams(TypedDict):
        subscription: Required[CheckoutExistingSubscriptionParams]
        addons: NotRequired[List[CheckoutExistingAddonParams]]
        event_based_addons: NotRequired[List[CheckoutExistingEventBasedAddonParams]]
        replace_addon_list: NotRequired[bool]
        mandatory_addons_to_remove: NotRequired[List[str]]
        invoice_date: NotRequired[int]
        billing_cycles: NotRequired[int]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        reactivate: NotRequired[bool]
        force_term_reset: NotRequired[bool]
        customer: NotRequired[CheckoutExistingCustomerParams]
        card: NotRequired[CheckoutExistingCardParams]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]
        allow_offline_payment_methods: NotRequired[bool]
        contract_term: NotRequired[CheckoutExistingContractTermParams]

    class CheckoutExistingForItemsParams(TypedDict):
        layout: NotRequired[enums.Layout]
        subscription: Required[CheckoutExistingForItemsSubscriptionParams]
        subscription_items: Required[
            List[CheckoutExistingForItemsSubscriptionItemParams]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        discounts: Required[List[CheckoutExistingForItemsDiscountParams]]
        item_tiers: NotRequired[List[CheckoutExistingForItemsItemTierParams]]
        invoice_date: NotRequired[int]
        billing_cycles: NotRequired[int]
        terms_to_charge: NotRequired[int]
        reactivate_from: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        coupon_ids: NotRequired[List[str]]
        reactivate: NotRequired[bool]
        force_term_reset: NotRequired[bool]
        change_option: NotRequired[enums.ChangeOption]
        changes_scheduled_at: NotRequired[int]
        customer: NotRequired[CheckoutExistingForItemsCustomerParams]
        entity_identifiers: NotRequired[
            List[CheckoutExistingForItemsEntityIdentifierParams]
        ]
        card: NotRequired[CheckoutExistingForItemsCardParams]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        allow_offline_payment_methods: NotRequired[bool]
        contract_term: NotRequired[CheckoutExistingForItemsContractTermParams]

    class UpdateCardParams(TypedDict):
        customer: Required[UpdateCardCustomerParams]
        card: NotRequired[UpdateCardCardParams]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]

    class UpdatePaymentMethodParams(TypedDict):
        customer: Required[UpdatePaymentMethodCustomerParams]
        card: NotRequired[UpdatePaymentMethodCardParams]
        redirect_url: NotRequired[str]
        cancel_url: NotRequired[str]
        pass_thru_content: NotRequired[str]
        embed: NotRequired[bool]
        iframe_messaging: NotRequired[bool]

    class ManagePaymentSourcesParams(TypedDict):
        customer: Required[ManagePaymentSourcesCustomerParams]
        redirect_url: NotRequired[str]
        card: NotRequired[ManagePaymentSourcesCardParams]

    class CollectNowParams(TypedDict):
        customer: Required[CollectNowCustomerParams]
        redirect_url: NotRequired[str]
        card: NotRequired[CollectNowCardParams]
        currency_code: NotRequired[str]

    class AcceptQuoteParams(TypedDict):
        quote: Required[AcceptQuoteQuoteParams]
        redirect_url: NotRequired[str]
        layout: NotRequired[enums.Layout]

    class ExtendSubscriptionParams(TypedDict):
        subscription: Required[ExtendSubscriptionSubscriptionParams]
        expiry: NotRequired[int]
        billing_cycle: NotRequired[int]

    class CheckoutGiftParams(TypedDict):
        gifter: NotRequired[CheckoutGiftGifterParams]
        redirect_url: NotRequired[str]
        subscription: Required[CheckoutGiftSubscriptionParams]
        addons: NotRequired[List[CheckoutGiftAddonParams]]
        coupon_ids: NotRequired[List[str]]

    class CheckoutGiftForItemsParams(TypedDict):
        business_entity_id: NotRequired[str]
        gifter: NotRequired[CheckoutGiftForItemsGifterParams]
        redirect_url: NotRequired[str]
        subscription_items: NotRequired[
            List[CheckoutGiftForItemsSubscriptionItemParams]
        ]
        coupon_ids: NotRequired[List[str]]

    class ClaimGiftParams(TypedDict):
        gift: Required[ClaimGiftGiftParams]
        redirect_url: NotRequired[str]
        customer: NotRequired[ClaimGiftCustomerParams]

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
        subscription: Required[PreCancelSubscriptionParams]
        pass_thru_content: NotRequired[str]
        cancel_url: NotRequired[str]
        redirect_url: NotRequired[str]

    class EventsParams(TypedDict):
        event_name: Required[enums.EventName]
        occurred_at: NotRequired[int]
        event_data: Required[Dict[Any, Any]]

    class ViewVoucherParams(TypedDict):
        payment_voucher: Required[ViewVoucherPaymentVoucherParams]
        customer: NotRequired[ViewVoucherCustomerParams]

    @staticmethod
    def checkout_new(
        params: CheckoutNewParams, env=None, headers=None
    ) -> CheckoutNewResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_new"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CheckoutNewResponse,
        )

    @staticmethod
    def checkout_one_time(
        params: CheckoutOneTimeParams = None, env=None, headers=None
    ) -> CheckoutOneTimeResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_one_time"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CheckoutOneTimeResponse,
        )

    @staticmethod
    def checkout_one_time_for_items(
        params: CheckoutOneTimeForItemsParams, env=None, headers=None
    ) -> CheckoutOneTimeForItemsResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_one_time_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CheckoutOneTimeForItemsResponse,
        )

    @staticmethod
    def checkout_new_for_items(
        params: CheckoutNewForItemsParams, env=None, headers=None
    ) -> CheckoutNewForItemsResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_new_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CheckoutNewForItemsResponse,
        )

    @staticmethod
    def checkout_existing(
        params: CheckoutExistingParams, env=None, headers=None
    ) -> CheckoutExistingResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_existing"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CheckoutExistingResponse,
        )

    @staticmethod
    def checkout_existing_for_items(
        params: CheckoutExistingForItemsParams, env=None, headers=None
    ) -> CheckoutExistingForItemsResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_existing_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CheckoutExistingForItemsResponse,
        )

    @staticmethod
    def update_card(
        params: UpdateCardParams, env=None, headers=None
    ) -> UpdateCardResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "update_card"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateCardResponse,
        )

    @staticmethod
    def update_payment_method(
        params: UpdatePaymentMethodParams, env=None, headers=None
    ) -> UpdatePaymentMethodResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "update_payment_method"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdatePaymentMethodResponse,
        )

    @staticmethod
    def manage_payment_sources(
        params: ManagePaymentSourcesParams, env=None, headers=None
    ) -> ManagePaymentSourcesResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "manage_payment_sources"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ManagePaymentSourcesResponse,
        )

    @staticmethod
    def collect_now(
        params: CollectNowParams, env=None, headers=None
    ) -> CollectNowResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "collect_now"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CollectNowResponse,
        )

    @staticmethod
    def accept_quote(
        params: AcceptQuoteParams, env=None, headers=None
    ) -> AcceptQuoteResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "accept_quote"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            AcceptQuoteResponse,
        )

    @staticmethod
    def extend_subscription(
        params: ExtendSubscriptionParams, env=None, headers=None
    ) -> ExtendSubscriptionResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "extend_subscription"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ExtendSubscriptionResponse,
        )

    @staticmethod
    def checkout_gift(
        params: CheckoutGiftParams, env=None, headers=None
    ) -> CheckoutGiftResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_gift"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CheckoutGiftResponse,
        )

    @staticmethod
    def checkout_gift_for_items(
        params: CheckoutGiftForItemsParams = None, env=None, headers=None
    ) -> CheckoutGiftForItemsResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "checkout_gift_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CheckoutGiftForItemsResponse,
        )

    @staticmethod
    def claim_gift(
        params: ClaimGiftParams, env=None, headers=None
    ) -> ClaimGiftResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "claim_gift"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ClaimGiftResponse,
        )

    @staticmethod
    def retrieve_agreement_pdf(
        params: RetrieveAgreementPdfParams, env=None, headers=None
    ) -> RetrieveAgreementPdfResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "retrieve_agreement_pdf"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RetrieveAgreementPdfResponse,
        )

    @staticmethod
    def acknowledge(id, env=None, headers=None) -> AcknowledgeResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", id, "acknowledge"),
            None,
            env,
            headers,
            AcknowledgeResponse,
        )

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("hosted_pages", id),
            None,
            env,
            headers,
            RetrieveResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("hosted_pages"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def pre_cancel(
        params: PreCancelParams, env=None, headers=None
    ) -> PreCancelResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "pre_cancel"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PreCancelResponse,
        )

    @staticmethod
    def events(params: EventsParams, env=None, headers=None) -> EventsResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "events"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EventsResponse,
        )

    @staticmethod
    def view_voucher(
        params: ViewVoucherParams, env=None, headers=None
    ) -> ViewVoucherResponse:
        return request.send(
            "post",
            request.uri_path("hosted_pages", "view_voucher"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ViewVoucherResponse,
        )
