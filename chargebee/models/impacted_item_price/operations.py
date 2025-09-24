from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


@dataclass
class ImpactedItemPrice:

    env: environment.Environment

    class Download(TypedDict):
        download_url: Required[str]
        valid_till: Required[int]
        mime_type: NotRequired[str]

    pass
