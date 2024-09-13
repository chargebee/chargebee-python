from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class UnbilledCharge:

    class CreateUnbilledChargeParams(TypedDict):
        subscription_id: Required[str]
        currency_code: NotRequired[str]
        addons: NotRequired[List[CreateUnbilledChargeAddonParams]]
        charges: NotRequired[List[CreateUnbilledChargeChargeParams]]
        tax_providers_fields: NotRequired[
            List[CreateUnbilledChargeTaxProvidersFieldParams]
        ]

    class CreateParams(TypedDict):
        subscription_id: Required[str]
        currency_code: NotRequired[str]
        item_prices: NotRequired[List[CreateItemPriceParams]]
        item_tiers: NotRequired[List[CreateItemTierParams]]
        charges: NotRequired[List[CreateChargeParams]]
        tax_providers_fields: NotRequired[List[CreateTaxProvidersFieldParams]]

    class InvoiceUnbilledChargesParams(TypedDict):
        subscription_id: NotRequired[str]
        customer_id: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        include_deleted: NotRequired[bool]
        is_voided: NotRequired[bool]
        subscription_id: NotRequired[Filters.StringFilter]
        customer_id: NotRequired[Filters.StringFilter]

    class InvoiceNowEstimateParams(TypedDict):
        subscription_id: NotRequired[str]
        customer_id: NotRequired[str]

    @staticmethod
    def create_unbilled_charge(
        params: CreateUnbilledChargeParams, env=None, headers=None
    ) -> CreateUnbilledChargeResponse:
        return request.send(
            "post",
            request.uri_path("unbilled_charges", "create"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateUnbilledChargeResponse,
        )

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("unbilled_charges"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def invoice_unbilled_charges(
        params: InvoiceUnbilledChargesParams = None, env=None, headers=None
    ) -> InvoiceUnbilledChargesResponse:
        return request.send(
            "post",
            request.uri_path("unbilled_charges", "invoice_unbilled_charges"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            InvoiceUnbilledChargesResponse,
        )

    @staticmethod
    def delete(id, env=None, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("unbilled_charges", id, "delete"),
            None,
            env,
            headers,
            DeleteResponse,
        )

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("unbilled_charges"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )

    @staticmethod
    def invoice_now_estimate(
        params: InvoiceNowEstimateParams = None, env=None, headers=None
    ) -> InvoiceNowEstimateResponse:
        return request.send(
            "post",
            request.uri_path("unbilled_charges", "invoice_now_estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            InvoiceNowEstimateResponse,
        )
