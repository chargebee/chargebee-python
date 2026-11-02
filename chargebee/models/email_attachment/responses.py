from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class EmailAttachmentResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    email_message_id: str = None
    file_name: str = None
    content_type: str = None
    size_bytes: int = None
    content_disposition: str = None
    created_at: int = None
    updated_at: int = None
    resource_version: int = None
