from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class Einvoice:
    env: environment.Environment

    class EntityType(Enum):
        INVOICE = "invoice"
        CREDIT_NOTE = "credit_note"

        def __str__(self):
            return self.value

    class Status(Enum):
        SCHEDULED = "scheduled"
        SKIPPED = "skipped"
        IN_PROGRESS = "in_progress"
        SUCCESS = "success"
        FAILED = "failed"
        REGISTERED = "registered"
        ACCEPTED = "accepted"
        REJECTED = "rejected"
        MESSAGE_ACKNOWLEDGEMENT = "message_acknowledgement"
        IN_PROCESS = "in_process"
        UNDER_QUERY = "under_query"
        CONDITIONALLY_ACCEPTED = "conditionally_accepted"
        PAID = "paid"

        def __str__(self):
            return self.value

    class EinvoiceArtifactDirection(Enum):
        OUTBOUND = "outbound"
        INBOUND = "inbound"

        def __str__(self):
            return self.value

    class EinvoiceArtifactStatus(Enum):
        SCHEDULED = "scheduled"
        SKIPPED = "skipped"
        IN_PROGRESS = "in_progress"
        SUCCESS = "success"
        FAILED = "failed"
        REGISTERED = "registered"

        def __str__(self):
            return self.value

    class Artifact(TypedDict):
        artifact_type: Required[str]
        direction: Required["Einvoice.EinvoiceArtifactDirection"]
        status: Required["Einvoice.EinvoiceArtifactStatus"]
        code: NotRequired[str]
        external_artifact_id: NotRequired[str]
        created_at: Required[int]
        resource_version: NotRequired[int]
        updated_at: NotRequired[int]
        deleted: Required[bool]

    class ListEinvoicesParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        id: NotRequired[Filters.StringFilter]
        reference_id: NotRequired[Filters.StringFilter]
        updated_at: NotRequired[Filters.TimestampFilter]
        sort_by: NotRequired[Filters.SortFilter]
        invoice_id: NotRequired[str]
        credit_note_id: NotRequired[str]

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("einvoices", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="einvoice",
            operation="retrieve",
        )

    def list_einvoices(
        self, params: ListEinvoicesParams = None, headers=None
    ) -> ListEinvoicesResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("einvoices"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListEinvoicesResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="einvoice",
            operation="listEinvoices",
        )
