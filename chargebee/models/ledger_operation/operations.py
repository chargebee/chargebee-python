from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class LedgerOperation:
    env: environment.Environment

    class UnitType(Enum):
        CREDIT_UNIT = "credit_unit"

        def __str__(self):
            return self.value

    class Type(Enum):
        ALLOCATION = "allocation"
        CAPTURE = "capture"
        AUTHORIZE = "authorize"
        RELEASE_AUTHORIZATION = "release_authorization"
        CAPTURE_AUTHORIZATION = "capture_authorization"
        EXPIRY = "expiry"
        VOID = "void"
        ROLLOVER = "rollover"
        ADJUSTMENT = "adjustment"

        def __str__(self):
            return self.value

    class ListLedgerOperationsParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        subscription_id: Required[Filters.StringFilter]
        unit_id: NotRequired[Filters.StringFilter]
        created_at: NotRequired[Filters.TimestampFilter]
        type: NotRequired[Filters.EnumFilter]
        sort_by: NotRequired[Filters.SortFilter]

    class CaptureParams(TypedDict):
        id: NotRequired[str]
        subscription_id: Required[str]
        unit_id: Required[str]
        amount: Required[str]
        ledger_operation_timestamp: Required[int]
        metadata: NotRequired[Dict[Any, Any]]

    class AuthorizeParams(TypedDict):
        id: NotRequired[str]
        subscription_id: Required[str]
        unit_id: Required[str]
        amount: Required[str]
        ledger_operation_timestamp: Required[int]
        auto_release_timestamp: NotRequired[int]
        metadata: NotRequired[Dict[Any, Any]]

    class CaptureAuthorizationParams(TypedDict):
        authorization_id: Required[str]
        id: NotRequired[str]
        amount: Required[str]
        ledger_operation_timestamp: Required[int]
        metadata: NotRequired[Dict[Any, Any]]

    class ReleaseAuthorizationParams(TypedDict):
        authorization_id: Required[str]
        id: NotRequired[str]
        ledger_operation_timestamp: Required[int]
        metadata: NotRequired[Dict[Any, Any]]

    class AllocateParams(TypedDict):
        subscription_id: Required[str]
        unit_id: Required[str]
        amount: Required[str]
        expires_at: Required[int]
        metadata: NotRequired[Dict[Any, Any]]

    def retrieve_ledger_operation(
        self, id, headers=None
    ) -> RetrieveLedgerOperationResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("ledger_operations", id),
            self.env,
            None,
            headers,
            RetrieveLedgerOperationResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="ledgerOperation",
            operation="retrieveLedgerOperation",
        )

    def list_ledger_operations(
        self, params: ListLedgerOperationsParams, headers=None
    ) -> ListLedgerOperationsResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("ledger_operations"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListLedgerOperationsResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="ledgerOperation",
            operation="listLedgerOperations",
        )

    def capture(self, params: CaptureParams, headers=None) -> CaptureResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("ledger_operations", "capture"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CaptureResponse,
            None,
            True,
            jsonKeys,
            options,
            resource="ledgerOperation",
            operation="capture",
        )

    def authorize(self, params: AuthorizeParams, headers=None) -> AuthorizeResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("ledger_operations", "authorize"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AuthorizeResponse,
            None,
            True,
            jsonKeys,
            options,
            resource="ledgerOperation",
            operation="authorize",
        )

    def capture_authorization(
        self, params: CaptureAuthorizationParams, headers=None
    ) -> CaptureAuthorizationResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("ledger_operations", "capture_authorization"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CaptureAuthorizationResponse,
            None,
            True,
            jsonKeys,
            options,
            resource="ledgerOperation",
            operation="captureAuthorization",
        )

    def release_authorization(
        self, params: ReleaseAuthorizationParams, headers=None
    ) -> ReleaseAuthorizationResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("ledger_operations", "release_authorization"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ReleaseAuthorizationResponse,
            None,
            True,
            jsonKeys,
            options,
            resource="ledgerOperation",
            operation="releaseAuthorization",
        )

    def allocate(self, params: AllocateParams, headers=None) -> AllocateResponse:
        jsonKeys = {
            "metadata": 0,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("ledger_operations", "allocate"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AllocateResponse,
            None,
            True,
            jsonKeys,
            options,
            resource="ledgerOperation",
            operation="allocate",
        )
