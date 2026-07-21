from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import column_definition, feature


@dataclass
class Meter:
    env: environment.Environment

    class Type(Enum):
        SIMPLE = "simple"
        COMPOUND = "compound"

        def __str__(self):
            return self.value

    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DELETED = "deleted"

        def __str__(self):
            return self.value

    class ColumnDefinitionDataType(Enum):
        NUMBER = "number"
        STRING = "string"

        def __str__(self):
            return self.value

    class FeatureStatus(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DRAFT = "draft"

        def __str__(self):
            return self.value

    class FeatureType(Enum):
        SWITCH = "switch"
        CUSTOM = "custom"
        QUANTITY = "quantity"
        RANGE = "range"

        def __str__(self):
            return self.value

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        name: NotRequired[Filters.StringFilter]
        sort_by: NotRequired[Filters.SortFilter]

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("meters"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="meter",
            operation="list",
        )
