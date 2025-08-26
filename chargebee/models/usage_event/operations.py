from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


@dataclass
class UsageEvent:
    env: environment.Environment

    class BatchIngestEventParams(TypedDict):
        deduplication_id: Required[str]
        subscription_id: Required[str]
        usage_timestamp: Required[int]
        properties: Required[Dict[Any, Any]]

    class CreateParams(TypedDict):
        deduplication_id: Required[str]
        subscription_id: Required[str]
        usage_timestamp: Required[int]
        properties: Required[Dict[Any, Any]]

    class BatchIngestParams(TypedDict):
        events: Required[List["UsageEvent.BatchIngestEventParams"]]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "properties": 0,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("usage_events"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            "ingest",
            True,
            jsonKeys,
            options,
        )

    def batch_ingest(
        self, params: BatchIngestParams, headers=None
    ) -> BatchIngestResponse:
        jsonKeys = {
            "properties": 1,
        }
        options = {}
        return request.send(
            "post",
            request.uri_path("batch", "usage_events"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            BatchIngestResponse,
            "ingest",
            True,
            jsonKeys,
            options,
        )
