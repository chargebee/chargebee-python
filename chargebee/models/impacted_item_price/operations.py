from .responses import *
from chargebee import request
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


class ImpactedItemPrice:

    class Download(TypedDict):
        download_url: Required[str]
        valid_till: Required[int]
        mime_type: NotRequired[str]

    pass
