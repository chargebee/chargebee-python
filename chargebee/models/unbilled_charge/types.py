from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


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


class UnbilledCharges(TypedDict):
    id: NotRequired[str]
    customer_id: NotRequired[str]
    subscription_id: NotRequired[str]
    date_from: NotRequired[int]
    date_to: NotRequired[int]
    unit_amount: NotRequired[int]
    pricing_model: NotRequired[enums.PricingModel]
    quantity: NotRequired[int]
    amount: NotRequired[int]
    currency_code: Required[str]
    discount_amount: NotRequired[int]
    description: NotRequired[str]
    entity_type: Required[EntityType]
    entity_id: NotRequired[str]
    is_voided: Required[bool]
    voided_at: NotRequired[int]
    unit_amount_in_decimal: NotRequired[str]
    quantity_in_decimal: NotRequired[str]
    amount_in_decimal: NotRequired[str]
    updated_at: Required[int]
    tiers: NotRequired[List[Tier]]
    is_advance_charge: NotRequired[bool]
    business_entity_id: NotRequired[str]
    deleted: Required[bool]


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
