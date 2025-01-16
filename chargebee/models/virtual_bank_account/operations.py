from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class VirtualBankAccount:

    env: environment.Environment

    class Scheme(Enum):
        ACH_CREDIT = "ach_credit"
        SEPA_CREDIT = "sepa_credit"
        US_AUTOMATED_BANK_TRANSFER = "us_automated_bank_transfer"
        GB_AUTOMATED_BANK_TRANSFER = "gb_automated_bank_transfer"
        EU_AUTOMATED_BANK_TRANSFER = "eu_automated_bank_transfer"
        JP_AUTOMATED_BANK_TRANSFER = "jp_automated_bank_transfer"
        MX_AUTOMATED_BANK_TRANSFER = "mx_automated_bank_transfer"

        def __str__(self):
            return self.value

    class CreateUsingPermanentTokenParams(TypedDict):
        customer_id: Required[str]
        reference_id: Required[str]
        scheme: NotRequired["VirtualBankAccount.Scheme"]

    class CreateParams(TypedDict):
        customer_id: Required[str]
        email: NotRequired[str]
        scheme: NotRequired["VirtualBankAccount.Scheme"]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        customer_id: NotRequired[Filters.StringFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        created_at: NotRequired[Filters.TimestampFilter]

    def create_using_permanent_token(
        self, params: CreateUsingPermanentTokenParams, headers=None
    ) -> CreateUsingPermanentTokenResponse:
        return request.send(
            "post",
            request.uri_path("virtual_bank_accounts", "create_using_permanent_token"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateUsingPermanentTokenResponse,
        )

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        return request.send(
            "post",
            request.uri_path("virtual_bank_accounts"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        return request.send(
            "get",
            request.uri_path("virtual_bank_accounts", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        return request.send_list_request(
            "get",
            request.uri_path("virtual_bank_accounts"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        return request.send(
            "post",
            request.uri_path("virtual_bank_accounts", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
        )

    def delete_local(self, id, headers=None) -> DeleteLocalResponse:
        return request.send(
            "post",
            request.uri_path("virtual_bank_accounts", id, "delete_local"),
            self.env,
            None,
            headers,
            DeleteLocalResponse,
        )
