from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class Quote:

    class CreateSubForCustomerQuoteParams(TypedDict):
        name: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: Required[CreateSubForCustomerQuoteSubscriptionParams]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List[CreateSubForCustomerQuoteAddonParams]]
        event_based_addons: NotRequired[
            List[CreateSubForCustomerQuoteEventBasedAddonParams]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[CreateSubForCustomerQuoteShippingAddressParams]
        contract_term: NotRequired[CreateSubForCustomerQuoteContractTermParams]
        coupon_ids: NotRequired[List[str]]

    class EditCreateSubForCustomerQuoteParams(TypedDict):
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: Required[EditCreateSubForCustomerQuoteSubscriptionParams]
        billing_cycles: NotRequired[int]
        addons: NotRequired[List[EditCreateSubForCustomerQuoteAddonParams]]
        event_based_addons: NotRequired[
            List[EditCreateSubForCustomerQuoteEventBasedAddonParams]
        ]
        mandatory_addons_to_remove: NotRequired[List[str]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            EditCreateSubForCustomerQuoteShippingAddressParams
        ]
        contract_term: NotRequired[EditCreateSubForCustomerQuoteContractTermParams]
        coupon_ids: NotRequired[List[str]]

    class UpdateSubscriptionQuoteParams(TypedDict):
        name: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: Required[UpdateSubscriptionQuoteSubscriptionParams]
        addons: NotRequired[List[UpdateSubscriptionQuoteAddonParams]]
        event_based_addons: NotRequired[
            List[UpdateSubscriptionQuoteEventBasedAddonParams]
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
        billing_address: NotRequired[UpdateSubscriptionQuoteBillingAddressParams]
        shipping_address: NotRequired[UpdateSubscriptionQuoteShippingAddressParams]
        customer: NotRequired[UpdateSubscriptionQuoteCustomerParams]
        contract_term: NotRequired[UpdateSubscriptionQuoteContractTermParams]

    class EditUpdateSubscriptionQuoteParams(TypedDict):
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: NotRequired[EditUpdateSubscriptionQuoteSubscriptionParams]
        addons: NotRequired[List[EditUpdateSubscriptionQuoteAddonParams]]
        event_based_addons: NotRequired[
            List[EditUpdateSubscriptionQuoteEventBasedAddonParams]
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
        billing_address: NotRequired[EditUpdateSubscriptionQuoteBillingAddressParams]
        shipping_address: NotRequired[EditUpdateSubscriptionQuoteShippingAddressParams]
        customer: NotRequired[EditUpdateSubscriptionQuoteCustomerParams]
        contract_term: NotRequired[EditUpdateSubscriptionQuoteContractTermParams]

    class CreateForOnetimeChargesParams(TypedDict):
        name: NotRequired[str]
        customer_id: Required[str]
        po_number: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        currency_code: NotRequired[str]
        addons: NotRequired[List[CreateForOnetimeChargesAddonParams]]
        charges: NotRequired[List[CreateForOnetimeChargesChargeParams]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        shipping_address: NotRequired[CreateForOnetimeChargesShippingAddressParams]
        tax_providers_fields: NotRequired[
            List[CreateForOnetimeChargesTaxProvidersFieldParams]
        ]

    class EditOneTimeQuoteParams(TypedDict):
        po_number: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        currency_code: NotRequired[str]
        addons: NotRequired[List[EditOneTimeQuoteAddonParams]]
        charges: NotRequired[List[EditOneTimeQuoteChargeParams]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        shipping_address: NotRequired[EditOneTimeQuoteShippingAddressParams]
        tax_providers_fields: NotRequired[List[EditOneTimeQuoteTaxProvidersFieldParams]]

    class CreateSubItemsForCustomerQuoteParams(TypedDict):
        name: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: NotRequired[CreateSubItemsForCustomerQuoteSubscriptionParams]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List[CreateSubItemsForCustomerQuoteSubscriptionItemParams]
        ]
        discounts: Required[List[CreateSubItemsForCustomerQuoteDiscountParams]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[List[CreateSubItemsForCustomerQuoteItemTierParams]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            CreateSubItemsForCustomerQuoteShippingAddressParams
        ]
        contract_term: NotRequired[CreateSubItemsForCustomerQuoteContractTermParams]
        coupon_ids: NotRequired[List[str]]

    class EditCreateSubCustomerQuoteForItemsParams(TypedDict):
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: NotRequired[EditCreateSubCustomerQuoteForItemsSubscriptionParams]
        billing_cycles: NotRequired[int]
        subscription_items: Required[
            List[EditCreateSubCustomerQuoteForItemsSubscriptionItemParams]
        ]
        discounts: Required[List[EditCreateSubCustomerQuoteForItemsDiscountParams]]
        mandatory_items_to_remove: NotRequired[List[str]]
        item_tiers: NotRequired[List[EditCreateSubCustomerQuoteForItemsItemTierParams]]
        terms_to_charge: NotRequired[int]
        billing_alignment_mode: NotRequired[enums.BillingAlignmentMode]
        shipping_address: NotRequired[
            EditCreateSubCustomerQuoteForItemsShippingAddressParams
        ]
        contract_term: NotRequired[EditCreateSubCustomerQuoteForItemsContractTermParams]
        coupon_ids: NotRequired[List[str]]

    class UpdateSubscriptionQuoteForItemsParams(TypedDict):
        name: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription: Required[UpdateSubscriptionQuoteForItemsSubscriptionParams]
        subscription_items: Required[
            List[UpdateSubscriptionQuoteForItemsSubscriptionItemParams]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        discounts: Required[List[UpdateSubscriptionQuoteForItemsDiscountParams]]
        item_tiers: NotRequired[List[UpdateSubscriptionQuoteForItemsItemTierParams]]
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
            UpdateSubscriptionQuoteForItemsBillingAddressParams
        ]
        shipping_address: NotRequired[
            UpdateSubscriptionQuoteForItemsShippingAddressParams
        ]
        customer: NotRequired[UpdateSubscriptionQuoteForItemsCustomerParams]
        contract_term: NotRequired[UpdateSubscriptionQuoteForItemsContractTermParams]

    class EditUpdateSubscriptionQuoteForItemsParams(TypedDict):
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        subscription_items: Required[
            List[EditUpdateSubscriptionQuoteForItemsSubscriptionItemParams]
        ]
        mandatory_items_to_remove: NotRequired[List[str]]
        replace_items_list: NotRequired[bool]
        subscription: NotRequired[EditUpdateSubscriptionQuoteForItemsSubscriptionParams]
        discounts: Required[List[EditUpdateSubscriptionQuoteForItemsDiscountParams]]
        item_tiers: NotRequired[List[EditUpdateSubscriptionQuoteForItemsItemTierParams]]
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
            EditUpdateSubscriptionQuoteForItemsBillingAddressParams
        ]
        shipping_address: NotRequired[
            EditUpdateSubscriptionQuoteForItemsShippingAddressParams
        ]
        customer: NotRequired[EditUpdateSubscriptionQuoteForItemsCustomerParams]
        contract_term: NotRequired[
            EditUpdateSubscriptionQuoteForItemsContractTermParams
        ]

    class CreateForChargeItemsAndChargesParams(TypedDict):
        name: NotRequired[str]
        customer_id: Required[str]
        po_number: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        currency_code: NotRequired[str]
        item_prices: NotRequired[List[CreateForChargeItemsAndChargesItemPriceParams]]
        item_tiers: NotRequired[List[CreateForChargeItemsAndChargesItemTierParams]]
        charges: NotRequired[List[CreateForChargeItemsAndChargesChargeParams]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        shipping_address: NotRequired[
            CreateForChargeItemsAndChargesShippingAddressParams
        ]
        discounts: Required[List[CreateForChargeItemsAndChargesDiscountParams]]
        tax_providers_fields: NotRequired[
            List[CreateForChargeItemsAndChargesTaxProvidersFieldParams]
        ]

    class EditForChargeItemsAndChargesParams(TypedDict):
        po_number: NotRequired[str]
        notes: NotRequired[str]
        expires_at: NotRequired[int]
        currency_code: NotRequired[str]
        item_prices: NotRequired[List[EditForChargeItemsAndChargesItemPriceParams]]
        item_tiers: NotRequired[List[EditForChargeItemsAndChargesItemTierParams]]
        charges: NotRequired[List[EditForChargeItemsAndChargesChargeParams]]
        coupon: NotRequired[str]
        coupon_ids: NotRequired[List[str]]
        shipping_address: NotRequired[EditForChargeItemsAndChargesShippingAddressParams]
        discounts: Required[List[EditForChargeItemsAndChargesDiscountParams]]
        tax_providers_fields: NotRequired[
            List[EditForChargeItemsAndChargesTaxProvidersFieldParams]
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
        subscription: NotRequired[ConvertSubscriptionParams]
        invoice_date: NotRequired[int]
        create_pending_invoices: NotRequired[bool]
        first_invoice_pending: NotRequired[bool]

    class UpdateStatusParams(TypedDict):
        status: Required[Status]
        comment: NotRequired[str]

    class ExtendExpiryDateParams(TypedDict):
        valid_till: Required[int]

    class DeleteParams(TypedDict):
        comment: NotRequired[str]

    class PdfParams(TypedDict):
        consolidated_view: NotRequired[bool]
        disposition_type: NotRequired[enums.DispositionType]

    @staticmethod
    def retrieve(id, env=None, headers=None) -> RetrieveResponse:
        return request.send(
            "get", request.uri_path("quotes", id), None, env, headers, RetrieveResponse
        )

    @staticmethod
    def create_sub_for_customer_quote(
        id, params: CreateSubForCustomerQuoteParams, env=None, headers=None
    ) -> CreateSubForCustomerQuoteResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "create_subscription_quote"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateSubForCustomerQuoteResponse,
        )

    @staticmethod
    def edit_create_sub_for_customer_quote(
        id, params: EditCreateSubForCustomerQuoteParams, env=None, headers=None
    ) -> EditCreateSubForCustomerQuoteResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_create_subscription_quote"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EditCreateSubForCustomerQuoteResponse,
        )

    @staticmethod
    def update_subscription_quote(
        params: UpdateSubscriptionQuoteParams, env=None, headers=None
    ) -> UpdateSubscriptionQuoteResponse:
        return request.send(
            "post",
            request.uri_path("quotes", "update_subscription_quote"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateSubscriptionQuoteResponse,
        )

    @staticmethod
    def edit_update_subscription_quote(
        id, params: EditUpdateSubscriptionQuoteParams = None, env=None, headers=None
    ) -> EditUpdateSubscriptionQuoteResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_update_subscription_quote"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EditUpdateSubscriptionQuoteResponse,
        )

    @staticmethod
    def create_for_onetime_charges(
        params: CreateForOnetimeChargesParams, env=None, headers=None
    ) -> CreateForOnetimeChargesResponse:
        return request.send(
            "post",
            request.uri_path("quotes", "create_for_onetime_charges"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForOnetimeChargesResponse,
        )

    @staticmethod
    def edit_one_time_quote(
        id, params: EditOneTimeQuoteParams = None, env=None, headers=None
    ) -> EditOneTimeQuoteResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_one_time_quote"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EditOneTimeQuoteResponse,
        )

    @staticmethod
    def create_sub_items_for_customer_quote(
        id, params: CreateSubItemsForCustomerQuoteParams, env=None, headers=None
    ) -> CreateSubItemsForCustomerQuoteResponse:
        return request.send(
            "post",
            request.uri_path("customers", id, "create_subscription_quote_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateSubItemsForCustomerQuoteResponse,
        )

    @staticmethod
    def edit_create_sub_customer_quote_for_items(
        id, params: EditCreateSubCustomerQuoteForItemsParams, env=None, headers=None
    ) -> EditCreateSubCustomerQuoteForItemsResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_create_subscription_quote_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EditCreateSubCustomerQuoteForItemsResponse,
        )

    @staticmethod
    def update_subscription_quote_for_items(
        params: UpdateSubscriptionQuoteForItemsParams, env=None, headers=None
    ) -> UpdateSubscriptionQuoteForItemsResponse:
        return request.send(
            "post",
            request.uri_path("quotes", "update_subscription_quote_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateSubscriptionQuoteForItemsResponse,
        )

    @staticmethod
    def edit_update_subscription_quote_for_items(
        id, params: EditUpdateSubscriptionQuoteForItemsParams, env=None, headers=None
    ) -> EditUpdateSubscriptionQuoteForItemsResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_update_subscription_quote_for_items"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EditUpdateSubscriptionQuoteForItemsResponse,
        )

    @staticmethod
    def create_for_charge_items_and_charges(
        params: CreateForChargeItemsAndChargesParams, env=None, headers=None
    ) -> CreateForChargeItemsAndChargesResponse:
        return request.send(
            "post",
            request.uri_path("quotes", "create_for_charge_items_and_charges"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateForChargeItemsAndChargesResponse,
        )

    @staticmethod
    def edit_for_charge_items_and_charges(
        id, params: EditForChargeItemsAndChargesParams, env=None, headers=None
    ) -> EditForChargeItemsAndChargesResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "edit_for_charge_items_and_charges"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EditForChargeItemsAndChargesResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("quotes"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def quote_line_groups_for_quote(
        id, params: QuoteLineGroupsForQuoteParams = None, env=None, headers=None
    ) -> QuoteLineGroupsForQuoteResponse:
        return request.send(
            "get",
            request.uri_path("quotes", id, "quote_line_groups"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            QuoteLineGroupsForQuoteResponse,
        )

    @staticmethod
    def convert(
        id, params: ConvertParams = None, env=None, headers=None
    ) -> ConvertResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "convert"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ConvertResponse,
        )

    @staticmethod
    def update_status(
        id, params: UpdateStatusParams, env=None, headers=None
    ) -> UpdateStatusResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "update_status"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            UpdateStatusResponse,
        )

    @staticmethod
    def extend_expiry_date(
        id, params: ExtendExpiryDateParams, env=None, headers=None
    ) -> ExtendExpiryDateResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "extend_expiry_date"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ExtendExpiryDateResponse,
        )

    @staticmethod
    def delete(
        id, params: DeleteParams = None, env=None, headers=None
    ) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "delete"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def pdf(id, params: PdfParams = None, env=None, headers=None) -> PdfResponse:
        return request.send(
            "post",
            request.uri_path("quotes", id, "pdf"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            PdfResponse,
        )
