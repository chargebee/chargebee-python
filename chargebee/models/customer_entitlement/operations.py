from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


@dataclass
class CustomerEntitlement:
    env: environment.Environment

    class EntitlementsForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        consolidate_entitlements: NotRequired[bool]

    def entitlements_for_customer(
        self, id, params: EntitlementsForCustomerParams = None, headers=None
    ) -> EntitlementsForCustomerResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "customer_entitlements"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EntitlementsForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
        )
