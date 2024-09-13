from typing import TypedDict, Required, NotRequired, Dict, List, Any


class Download(TypedDict):
    download_url: Required[str]
    valid_till: Required[int]
    mime_type: NotRequired[str]


class ImpactedSubscriptions(TypedDict):
    count: NotRequired[int]
    download: NotRequired[Download]
    subscription_ids: NotRequired[List[Dict[Any, Any]]]
