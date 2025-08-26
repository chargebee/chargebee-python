from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class CommentResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    entity_type: str = None
    added_by: str = None
    notes: str = None
    created_at: int = None
    type: str = None
    entity_id: str = None
    business_entity_id: str = None


@dataclass
class CreateResponse(Response):
    is_idempotency_replayed: bool
    comment: CommentResponse


@dataclass
class RetrieveResponse(Response):
    comment: CommentResponse


@dataclass
class ListCommentResponse:
    comment: CommentResponse


@dataclass
class ListResponse(Response):
    list: List[ListCommentResponse]
    next_offset: str = None


@dataclass
class DeleteResponse(Response):
    is_idempotency_replayed: bool
    comment: CommentResponse
