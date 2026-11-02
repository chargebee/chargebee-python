from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class AttachmentResponse(Model):
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


@dataclass
class EmailMessageResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    email_conversation_id: str = None
    message_type: str = None
    author_type: str = None
    send_status: str = None
    content_html: str = None
    content_text: str = None
    created_at: int = None
    updated_at: int = None
    resource_version: int = None
    mailbox_id: str = None
    author_id: str = None
    author_name: str = None
    from_email: str = None
    to_emails: List[str] = None
    cc_emails: List[str] = None
    attachments: List[AttachmentResponse] = None
