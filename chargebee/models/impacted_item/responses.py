from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class DownloadResponse(Model):
    raw_data: Dict[Any, Any] = None
    download_url: str = None
    valid_till: int = None
    mime_type: str = None


@dataclass
class ImpactedItemResponse(Model):
    raw_data: Dict[Any, Any] = None
    count: int = None
    download: DownloadResponse = None
    items: List[Dict[Any, Any]] = None
