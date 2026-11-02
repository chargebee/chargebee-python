from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class EmailMessage:
    env: environment.Environment

    class AuthorType(Enum):
        CONTACT = "contact"
        SITE_USER = "site_user"
        AGENT = "agent"
        OTHER = "other"

        def __str__(self):
            return self.value

    class SendStatus(Enum):
        PENDING = "pending"
        SENT = "sent"
        FAILED = "failed"

        def __str__(self):
            return self.value

    class Attachment(TypedDict):
        id: Required[str]
        email_message_id: NotRequired[str]
        file_name: NotRequired[str]
        content_type: NotRequired[str]
        size_bytes: NotRequired[int]
        content_disposition: NotRequired[str]
        created_at: Required[int]
        updated_at: Required[int]
        resource_version: NotRequired[int]

    pass
