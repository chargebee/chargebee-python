from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class EmailConversationResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    customer_id: str = None
    mailbox_id: str = None
    subject: str = None
    last_message_preview: str = None
    message_count: int = None
    status: str = None
    last_message_at: int = None
    created_at: int = None
    updated_at: int = None
    resource_version: int = None
