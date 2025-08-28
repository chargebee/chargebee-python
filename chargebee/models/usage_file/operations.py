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

    class UploadUrlParams(TypedDict):
        file_name: Required[str]
        mime_type: Required[str]

    def upload_url(self, params: UploadUrlParams, headers=None) -> UploadUrlResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("usage_files", "upload_url"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UploadUrlResponse,
            "file-ingest",
            False,
            jsonKeys,
            options,
        )

    def processing_status(self, id, headers=None) -> ProcessingStatusResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("usage_files", id, "processing_status"),
            self.env,
            None,
            headers,
            ProcessingStatusResponse,
            "file-ingest",
            False,
            jsonKeys,
            options,
        )
