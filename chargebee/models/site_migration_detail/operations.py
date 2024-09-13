from .types import *
from .responses import *
from chargebee import request
from typing import cast, Any
from chargebee.filters import Filters


class SiteMigrationDetail:

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        entity_id_at_other_site: NotRequired[Filters.StringFilter]
        other_site_name: NotRequired[Filters.StringFilter]
        entity_id: NotRequired[Filters.StringFilter]
        entity_type: NotRequired[Filters.EnumFilter]
        status: NotRequired[Filters.EnumFilter]

    @staticmethod
    def list(params: ListParams = None, env=None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("site_migration_details"),
            cast(Dict[Any, Any], params),
            env,
            headers,
            ListResponse,
        )
