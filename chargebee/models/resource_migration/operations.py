from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import enums


class ResourceMigration:
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

    @staticmethod
    def retrieve_latest(
        params: RetrieveLatestParams, env=None, headers=None
    ) -> RetrieveLatestResponse:
        return request.send(
            "get",
            request.uri_path("resource_migrations", "retrieve_latest"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            RetrieveLatestResponse,
        )
