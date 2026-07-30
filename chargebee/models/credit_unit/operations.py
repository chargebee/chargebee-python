from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class CreditUnit:
    env: environment.Environment

    class Status(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"

        def __str__(self):
            return self.value

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        status: NotRequired[Filters.EnumFilter]
        id: NotRequired[Filters.StringFilter]

    class CreateParams(TypedDict):
        id: Required[str]
        name: Required[str]
        is_unlimited: Required[bool]
        overdraft_amount: NotRequired[str]
        external_name: NotRequired[str]

    class UpdateParams(TypedDict):
        name: NotRequired[str]
        external_name: NotRequired[str]

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("credit_units"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="creditUnit",
            operation="list",
        )

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_units"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="creditUnit",
            operation="create",
        )

    def update(self, id, params: UpdateParams = None, headers=None) -> UpdateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_units", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="creditUnit",
            operation="update",
        )

    def archive(self, id, headers=None) -> ArchiveResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_units", id, "archive_command"),
            self.env,
            None,
            headers,
            ArchiveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="creditUnit",
            operation="archive",
        )

    def reactivate(self, id, headers=None) -> ReactivateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("credit_units", id, "reactivate_command"),
            self.env,
            None,
            headers,
            ReactivateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="creditUnit",
            operation="reactivate",
        )
