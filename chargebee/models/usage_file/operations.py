from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class UsageFile:

    env: environment.Environment

    class Status(Enum):
        QUEUED = "queued"
        IMPORTED = "imported"
        PROCESSING = "processing"
        PROCESSED = "processed"
        FAILED = "failed"

        def __str__(self):
            return self.value

    class UploadDetail(TypedDict):
        url: Required[str]
        expires_at: Required[int]

    class UploadParams(TypedDict):
        file_name: Required[str]
        mime_type: Required[str]

    def upload(self, params: UploadParams, headers=None) -> UploadResponse:
        jsonKeys = {}
        return request.send(
            "post",
            request.uri_path("usage_files", "upload"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UploadResponse,
            "file-ingest",
            False,
            jsonKeys,
        )

    def status(self, id, headers=None) -> StatusResponse:
        jsonKeys = {}
        return request.send(
            "get",
            request.uri_path("usage_files", id, "status"),
            self.env,
            None,
            headers,
            StatusResponse,
            "file-ingest",
            False,
            jsonKeys,
        )
