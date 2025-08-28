from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.models import enums, payment_intent, contract_term


@dataclass
class Purchase:
    env: environment.Environment

    class CreatePurchaseItemParams(TypedDict):
        index: Required[int]
        item_price_id: Required[str]
        quantity: NotRequired[int]
        unit_amount: NotRequired[int]
        unit_amount_in_decimal: NotRequired[str]
        quantity_in_decimal: NotRequired[str]

    class CreateItemTierParams(TypedDict):
        index: Required[int]
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]

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
        state: NotRequired[str]
        state_code: NotRequired[str]
        country: NotRequired[str]
        zip: NotRequired[str]
        validation_status: NotRequired[enums.ValidationStatus]

    class CreateDiscountParams(TypedDict):
        index: NotRequired[int]
        coupon_id: NotRequired[str]
        percentage: NotRequired[float]
        quantity: NotRequired[int]
        amount: NotRequired[int]
        included_in_mrr: NotRequired[bool]

    class CreateSubscriptionInfoParams(TypedDict):
        index: Required[int]
        subscription_id: NotRequired[str]
        billing_cycles: NotRequired[int]
        contract_term_billing_cycle_on_renewal: NotRequired[int]
        meta_data: NotRequired[Dict[Any, Any]]

    class CreateContractTermParams(TypedDict):
        index: Required[int]
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class CreateInvoiceInfoParams(TypedDict):
        po_number: NotRequired[str]
        notes: NotRequired[str]

    class CreatePaymentScheduleParams(TypedDict):
        scheme_id: NotRequired[str]
        amount: NotRequired[int]

    class CreateStatementDescriptorParams(TypedDict):
        descriptor: NotRequired[str]

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

    class EstimatePurchaseItemParams(TypedDict):
        index: Required[int]
        item_price_id: Required[str]
        quantity: NotRequired[int]
        unit_amount: NotRequired[int]
        unit_amount_in_decimal: NotRequired[str]
        quantity_in_decimal: NotRequired[str]

    class EstimateItemTierParams(TypedDict):
        index: Required[int]
        item_price_id: NotRequired[str]
        starting_unit: NotRequired[int]
        ending_unit: NotRequired[int]
        price: NotRequired[int]
        starting_unit_in_decimal: NotRequired[str]
        ending_unit_in_decimal: NotRequired[str]
        price_in_decimal: NotRequired[str]

    class EstimateShippingAddressParams(TypedDict):
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        email: NotRequired[str]
        company: NotRequired[str]
        phone: NotRequired[str]
        line1: NotRequired[str]
        line2: NotRequired[str]
        line3: NotRequired[str]
        city: NotRequired[str]
        state: NotRequired[str]
        state_code: NotRequired[str]
        country: NotRequired[str]
        zip: NotRequired[str]
        validation_status: NotRequired[enums.ValidationStatus]

    class EstimateDiscountParams(TypedDict):
        index: NotRequired[int]
        coupon_id: NotRequired[str]
        percentage: NotRequired[float]
        quantity: NotRequired[int]
        amount: NotRequired[int]
        included_in_mrr: NotRequired[bool]

    class EstimateSubscriptionInfoParams(TypedDict):
        index: Required[int]
        subscription_id: NotRequired[str]
        billing_cycles: NotRequired[int]
        contract_term_billing_cycle_on_renewal: NotRequired[int]

    class EstimateContractTermParams(TypedDict):
        index: Required[int]
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class EstimateCustomerParams(TypedDict):
        vat_number: NotRequired[str]
        vat_number_prefix: NotRequired[str]
        registered_for_gst: NotRequired[bool]
        taxability: NotRequired[enums.Taxability]
        entity_code: NotRequired[enums.EntityCode]
        exempt_number: NotRequired[str]
        exemption_details: NotRequired[List[Dict[Any, Any]]]
        customer_type: NotRequired[enums.CustomerType]

    class EstimateBillingAddressParams(TypedDict):
        line1: NotRequired[str]
        line2: NotRequired[str]
        line3: NotRequired[str]
        city: NotRequired[str]
        state_code: NotRequired[str]
        zip: NotRequired[str]
        country: NotRequired[str]
        validation_status: NotRequired[enums.ValidationStatus]

    class CreateParams(TypedDict):
        purchase_items: Required[List["Purchase.CreatePurchaseItemParams"]]
        item_tiers: Required[List["Purchase.CreateItemTierParams"]]
        shipping_addresses: NotRequired[List["Purchase.CreateShippingAddressParams"]]
        discounts: NotRequired[List["Purchase.CreateDiscountParams"]]
        subscription_info: Required[List["Purchase.CreateSubscriptionInfoParams"]]
        contract_terms: Required[List["Purchase.CreateContractTermParams"]]
        invoice_info: NotRequired["Purchase.CreateInvoiceInfoParams"]
        payment_schedule: NotRequired["Purchase.CreatePaymentScheduleParams"]
        statement_descriptor: NotRequired["Purchase.CreateStatementDescriptorParams"]
        customer_id: Required[str]
        payment_source_id: NotRequired[str]
        payment_intent: NotRequired["Purchase.CreatePaymentIntentParams"]
        replace_primary_payment_source: NotRequired[bool]

    class EstimateParams(TypedDict):
        purchase_items: Required[List["Purchase.EstimatePurchaseItemParams"]]
        item_tiers: Required[List["Purchase.EstimateItemTierParams"]]
        shipping_addresses: NotRequired[List["Purchase.EstimateShippingAddressParams"]]
        discounts: NotRequired[List["Purchase.EstimateDiscountParams"]]
        subscription_info: Required[List["Purchase.EstimateSubscriptionInfoParams"]]
        contract_terms: Required[List["Purchase.EstimateContractTermParams"]]
        customer: NotRequired["Purchase.EstimateCustomerParams"]
        billing_address: NotRequired["Purchase.EstimateBillingAddressParams"]
        client_profile_id: NotRequired[str]
        customer_id: NotRequired[str]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "additional_information": 1,
            "meta_data": 1,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("purchases"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def estimate(self, params: EstimateParams, headers=None) -> EstimateResponse:
        jsonKeys = {
            "exemption_details": 1,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("purchases", "estimate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EstimateResponse,
            None,
            False,
            jsonKeys,
            options,
        )
