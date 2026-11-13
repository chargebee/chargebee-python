from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters


@dataclass
class OrganizationDetail:
    env: environment.Environment

    class CreateParams(TypedDict):
        organization_name: Required[str]
        email: NotRequired[str]
        address_line1: Required[str]
        address_line2: NotRequired[str]
        address_line3: NotRequired[str]
        city: Required[str]
        state_code: NotRequired[str]
        state: Required[str]
        zip: Required[str]
        country_code: NotRequired[str]
        phone: Required[str]
        fax: NotRequired[str]
        website: NotRequired[str]
        is_vat_number_present: NotRequired[bool]
        vat_number: NotRequired[str]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        business_entity_id: NotRequired[Filters.StringFilter]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("organization_details"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="organizationDetail",
            operation="create",
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("organization_details", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="organizationDetail",
            operation="retrieve",
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("organization_details"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="organizationDetail",
            operation="list",
        )
