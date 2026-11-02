from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class PrivateNoteResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    email_conversation_id: str = None
    author_type: str = None
    author_id: str = None
    author_name: str = None
    content_html: str = None
    content_text: str = None
    meta_data: str = None
    created_at: int = None
    resource_version: int = None
    updated_at: int = None
