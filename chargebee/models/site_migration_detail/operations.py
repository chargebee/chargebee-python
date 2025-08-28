from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class SiteMigrationDetail:
    env: environment.Environment

    class Status(Enum):
        MOVED_IN = "moved_in"
        MOVED_OUT = "moved_out"
        MOVING_OUT = "moving_out"

        def __str__(self):
            return self.value

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        entity_id_at_other_site: NotRequired[Filters.StringFilter]
        other_site_name: NotRequired[Filters.StringFilter]
        entity_id: NotRequired[Filters.StringFilter]
        entity_type: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("site_migration_details"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )
