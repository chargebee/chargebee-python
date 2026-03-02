from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.models import enums, contract_term


@dataclass
class PricingPageSession:
    env: environment.Environment

    class CreateForNewSubscriptionPricingPageParams(TypedDict):
        id: Required[str]

    class CreateForNewSubscriptionSubscriptionParams(TypedDict):
        id: NotRequired[str]

    class CreateForNewSubscriptionCustomerParams(TypedDict):
        id: NotRequired[str]
        email: NotRequired[str]
        first_name: NotRequired[str]
        last_name: NotRequired[str]
        company: NotRequired[str]
        phone: NotRequired[str]
        locale: NotRequired[str]

    class CreateForNewSubscriptionDiscountParams(TypedDict):
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]
        label: NotRequired[str]

    class CreateForNewSubscriptionBillingAddressParams(TypedDict):
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

    class CreateForNewSubscriptionShippingAddressParams(TypedDict):
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

    class CreateForNewSubscriptionContractTermParams(TypedDict):
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class CreateForExistingSubscriptionPricingPageParams(TypedDict):
        id: NotRequired[str]

    class CreateForExistingSubscriptionSubscriptionParams(TypedDict):
        id: Required[str]

    class CreateForExistingSubscriptionDiscountParams(TypedDict):
        apply_on: NotRequired[enums.ApplyOn]
        duration_type: Required[enums.DurationType]
        percentage: NotRequired[float]
        amount: NotRequired[int]
        period: NotRequired[int]
        period_unit: NotRequired[enums.PeriodUnit]
        included_in_mrr: NotRequired[bool]
        item_price_id: NotRequired[str]
        quantity: NotRequired[int]
        label: NotRequired[str]

    class CreateForExistingSubscriptionContractTermParams(TypedDict):
        action_at_term_end: NotRequired["contract_term.ContractTerm.ActionAtTermEnd"]
        cancellation_cutoff_period: NotRequired[int]

    class CreateForNewSubscriptionParams(TypedDict):
        redirect_url: NotRequired[str]
        pricing_page: Required[
            "PricingPageSession.CreateForNewSubscriptionPricingPageParams"
        ]
        subscription: NotRequired[
            "PricingPageSession.CreateForNewSubscriptionSubscriptionParams"
        ]
        business_entity_id: NotRequired[str]
        auto_select_local_currency: NotRequired[bool]
        custom: NotRequired[Dict[Any, Any]]
        customer: NotRequired[
            "PricingPageSession.CreateForNewSubscriptionCustomerParams"
        ]
        discounts: Required[
            List["PricingPageSession.CreateForNewSubscriptionDiscountParams"]
        ]
        billing_address: NotRequired[
            "PricingPageSession.CreateForNewSubscriptionBillingAddressParams"
        ]
        shipping_address: NotRequired[
            "PricingPageSession.CreateForNewSubscriptionShippingAddressParams"
        ]
        contract_term: NotRequired[
            "PricingPageSession.CreateForNewSubscriptionContractTermParams"
        ]

    class CreateForExistingSubscriptionParams(TypedDict):
        redirect_url: NotRequired[str]
        pricing_page: NotRequired[
            "PricingPageSession.CreateForExistingSubscriptionPricingPageParams"
        ]
        subscription: Required[
            "PricingPageSession.CreateForExistingSubscriptionSubscriptionParams"
        ]
        custom: NotRequired[Dict[Any, Any]]
        discounts: Required[
            List["PricingPageSession.CreateForExistingSubscriptionDiscountParams"]
        ]
        contract_term: NotRequired[
            "PricingPageSession.CreateForExistingSubscriptionContractTermParams"
        ]

    def create_for_new_subscription(
        self, params: CreateForNewSubscriptionParams, headers=None
    ) -> CreateForNewSubscriptionResponse:
        jsonKeys = {
            "custom": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("pricing_page_sessions", "create_for_new_subscription"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForNewSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )

    def create_for_existing_subscription(
        self, params: CreateForExistingSubscriptionParams, headers=None
    ) -> CreateForExistingSubscriptionResponse:
        jsonKeys = {
            "custom": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path(
                "pricing_page_sessions", "create_for_existing_subscription"
            ),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateForExistingSubscriptionResponse,
            None,
            False,
            jsonKeys,
            options,
        )
