from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums


@dataclass
class UnbilledCharge:

    env: environment.Environment

    class EntityType(Enum):
        ADHOC = "adhoc"
        PLAN_ITEM_PRICE = "plan_item_price"
        ADDON_ITEM_PRICE = "addon_item_price"
        CHARGE_ITEM_PRICE = "charge_item_price"
        PLAN_SETUP = "plan_setup"
        PLAN = "plan"
        ADDON = "addon"

        def __str__(self):
            return self.value

    class Tier(TypedDict):
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

    class CreateUnbilledChargeAddonParams(TypedDict):
        id: NotRequired[str]
        quantity: NotRequired[int]
        unit_price: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        unit_price_in_decimal: NotRequired[str]
        date_from: NotRequired[int]
        date_to: NotRequired[int]

    class CreateUnbilledChargeChargeParams(TypedDict):
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

    class CreateUnbilledChargeTaxProvidersFieldParams(TypedDict):
        provider_name: NotRequired[str]
        field_id: NotRequired[str]
        field_value: NotRequired[str]

    class CreateItemPriceParams(TypedDict):
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]
        quantity_in_decimal: NotRequired[str]
        unit_price: NotRequired[int]
        unit_price_in_decimal: NotRequired[str]
        date_from: NotRequired[int]
        date_to: NotRequired[int]

    class CreateItemTierParams(TypedDict):
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]
        pricing_type: NotRequired[enums.PricingType]
        package_size: NotRequired[int]

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

    class CreateUnbilledChargeParams(TypedDict):
        subscription_id: Required[str]
        currency_code: NotRequired[str]
        addons: NotRequired[List["UnbilledCharge.CreateUnbilledChargeAddonParams"]]
        charges: NotRequired[List["UnbilledCharge.CreateUnbilledChargeChargeParams"]]
        tax_providers_fields: NotRequired[
            List["UnbilledCharge.CreateUnbilledChargeTaxProvidersFieldParams"]
        ]

    class CreateParams(TypedDict):
        subscription_id: Required[str]
        currency_code: NotRequired[str]
        item_prices: NotRequired[List["UnbilledCharge.CreateItemPriceParams"]]
        item_tiers: NotRequired[List["UnbilledCharge.CreateItemTierParams"]]
        charges: NotRequired[List["UnbilledCharge.CreateChargeParams"]]
        tax_providers_fields: NotRequired[
            List["UnbilledCharge.CreateTaxProvidersFieldParams"]
        ]

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

    def create_unbilled_charge(
        self, params: CreateUnbilledChargeParams, headers=None
    ) -> CreateUnbilledChargeResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("unbilled_charges", "create"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateUnbilledChargeResponse,
            None,
            False,
            jsonKeys,
        )

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("unbilled_charges"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
        )

    def invoice_unbilled_charges(
        self, params: InvoiceUnbilledChargesParams = None, headers=None
    ) -> InvoiceUnbilledChargesResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("unbilled_charges", "invoice_unbilled_charges"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            InvoiceUnbilledChargesResponse,
            None,
            False,
            jsonKeys,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("unbilled_charges", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        return request.send_list_request(
            "get",
            request.uri_path("unbilled_charges"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
        )

    def invoice_now_estimate(
        self, params: InvoiceNowEstimateParams = None, headers=None
    ) -> InvoiceNowEstimateResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("unbilled_charges", "invoice_now_estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            InvoiceNowEstimateResponse,
            None,
            False,
            jsonKeys,
        )
