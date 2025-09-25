from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class SiteMigrationDetailResponse(Model):
    raw_data: Dict[Any, Any] = None
    entity_id: str = None
    other_site_name: str = None
    entity_id_at_other_site: str = None
    migrated_at: int = None
    entity_type: str = None
    status: str = None


@dataclass
class ListSiteMigrationDetailResponse:
    site_migration_detail: SiteMigrationDetailResponse


@dataclass
class ListResponse(Response):
    list: List[ListSiteMigrationDetailResponse]
    next_offset: str = None
