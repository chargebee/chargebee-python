from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters


@dataclass
class EmailLog:
    env: environment.Environment

    class EmailLogsForCustomerParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        sent_on: NotRequired[Filters.TimestampFilter]
        business_entity_id: NotRequired[Filters.StringFilter]
        brand_id: NotRequired[Filters.StringFilter]

    def email_logs_for_customer(
        self, id, params: EmailLogsForCustomerParams = None, headers=None
    ) -> EmailLogsForCustomerResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("customers", id, "email_logs"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            EmailLogsForCustomerResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="emailLog",
            operation="emailLogsForCustomer",
        )
