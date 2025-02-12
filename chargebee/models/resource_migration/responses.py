from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class ResourceMigrationResponse(Model):
    raw_data: Dict[Any, Any] = None
    from_site: str = None
    entity_type: str = None
    entity_id: str = None
    status: str = None
    errors: str = None
    created_at: int = None
    updated_at: int = None


@dataclass
class RetrieveLatestResponse(Response):

    resource_migration: ResourceMigrationResponse
