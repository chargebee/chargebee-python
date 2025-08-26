from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class ConfigurationResponse(Model):
    raw_data: Dict[Any, Any] = None
    domain: str = None
    product_catalog_version: str = None
    chargebee_response_schema_type: str = None


@dataclass
class ListResponse(Response):
    configurations: List[ConfigurationResponse]
