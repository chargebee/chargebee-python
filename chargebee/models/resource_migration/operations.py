from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


@dataclass
class ResourceMigration:
    env: environment.Environment

    class Status(Enum):
        SCHEDULED = "scheduled"
        FAILED = "failed"
        SUCCEEDED = "succeeded"

        def __str__(self):
            return self.value

    class RetrieveLatestParams(TypedDict):
        from_site: Required[str]
        entity_type: Required[enums.EntityType]
        entity_id: Required[str]

    def retrieve_latest(
        self, params: RetrieveLatestParams, headers=None
    ) -> RetrieveLatestResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("resource_migrations", "retrieve_latest"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RetrieveLatestResponse,
            None,
            False,
            jsonKeys,
            options,
        )
