from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any


class Purchase:

    class CreateParams(TypedDict):
        purchase_items: Required[List[CreatePurchaseItemParams]]
        item_tiers: Required[List[CreateItemTierParams]]
        shipping_addresses: NotRequired[List[CreateShippingAddressParams]]
        discounts: NotRequired[List[CreateDiscountParams]]
        subscription_info: Required[List[CreateSubscriptionInfoParams]]
        contract_terms: Required[List[CreateContractTermParams]]
        invoice_info: NotRequired[CreateInvoiceInfoParams]
        statement_descriptor: NotRequired[CreateStatementDescriptorParams]
        installment_info: NotRequired[CreateInstallmentInfoParams]
        customer_id: Required[str]
        payment_source_id: NotRequired[str]

    class EstimateParams(TypedDict):
        purchase_items: Required[List[EstimatePurchaseItemParams]]
        item_tiers: Required[List[EstimateItemTierParams]]
        shipping_addresses: NotRequired[List[EstimateShippingAddressParams]]
        discounts: NotRequired[List[EstimateDiscountParams]]
        subscription_info: Required[List[EstimateSubscriptionInfoParams]]
        contract_terms: Required[List[EstimateContractTermParams]]
        customer: NotRequired[EstimateCustomerParams]
        billing_address: NotRequired[EstimateBillingAddressParams]
        client_profile_id: NotRequired[str]
        customer_id: NotRequired[str]

    @staticmethod
    def create(params: CreateParams, env=None, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("purchases"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            CreateResponse,
        )

    @staticmethod
    def estimate(params: EstimateParams, env=None, headers=None) -> EstimateResponse:
        return request.send(
            "post",
            request.uri_path("purchases", "estimate"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EstimateResponse,
        )
