from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class PrivateNote:
    env: environment.Environment

    class AuthorType(Enum):
        SITE_USER = "site_user"
        AGENT = "agent"
        OTHER = "other"

        def __str__(self):
            return self.value

    pass
