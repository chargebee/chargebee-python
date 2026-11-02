from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class RetrySegment:
    env: environment.Environment

    class ConditionLogic(Enum):
        AND = "and"
        OR = "or"

        def __str__(self):
            return self.value

    class RetrieveParams(TypedDict):
        invoice_id: NotRequired[str]

    def retrieve(
        self, id, params: RetrieveParams = None, headers=None
    ) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("retry_segments", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="retrySegment",
            operation="retrieve",
        )
