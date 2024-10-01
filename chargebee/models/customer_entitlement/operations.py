from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


class CustomerEntitlement:

    class EntitlementsForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]

    @staticmethod
    def entitlements_for_customer(
        id, params: EntitlementsForCustomerParams = None, env=None, headers=None
    ) -> EntitlementsForCustomerResponse:
        return request.send(
            "get",
            request.uri_path("customers", id, "customer_entitlements"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            EntitlementsForCustomerResponse,
        )
