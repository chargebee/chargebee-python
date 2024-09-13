from typing import TypedDict, Required, NotRequired, Dict, List, Any


class Download(TypedDict):
    download_url: Required[str]
    valid_till: Required[int]
    mime_type: NotRequired[str]


class ImpactedItems(TypedDict):
    count: NotRequired[int]
    download: NotRequired[Download]
    items: NotRequired[List[Dict[Any, Any]]]
