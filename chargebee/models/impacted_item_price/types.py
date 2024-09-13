from typing import TypedDict, Required, NotRequired, Dict, List, Any


class Download(TypedDict):
    download_url: Required[str]
    valid_till: Required[int]
    mime_type: NotRequired[str]


class ImpactedItemPrices(TypedDict):
    count: NotRequired[int]
    download: NotRequired[Download]
    item_prices: NotRequired[List[Dict[Any, Any]]]
