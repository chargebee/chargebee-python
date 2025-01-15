from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class ConfigurationResponse(Model):
    raw_data: Dict[Any, Any] = None
    domain: str = None
    product_catalog_version: str = None


@dataclass
class ListResponse:
    configurations: List[ConfigurationResponse]
    headers: Dict[str, str] = None
