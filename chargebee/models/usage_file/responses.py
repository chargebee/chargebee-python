from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class UploadDetailResponse(Model):
    raw_data: Dict[Any, Any] = None
    url: str = None
    expires_at: int = None


@dataclass
class UsageFileResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    name: str = None
    mime_type: str = None
    error_code: str = None
    error_reason: str = None
    status: str = None
    total_records_count: int = None
    processed_records_count: int = None
    failed_records_count: int = None
    file_size_in_bytes: int = None
    processing_started_at: int = None
    processing_completed_at: int = None
    uploaded_by: str = None
    uploaded_at: int = None
    error_file_path: str = None
    error_file_url: str = None
    upload_details: UploadDetailResponse = None


@dataclass
class UploadUrlResponse(Response):
    is_idempotency_replayed: bool
    usage_file: UsageFileResponse


@dataclass
class ProcessingStatusResponse(Response):
    usage_file: UsageFileResponse
