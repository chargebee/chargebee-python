from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


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


@dataclass
class CreateResponse:
    comment: CommentResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class RetrieveResponse:
    comment: CommentResponse
    response_headers: Dict[Any, Any] = None


@dataclass
class ListCommentResponse:
    comment: CommentResponse


@dataclass
class ListResponse:
    list: List[ListCommentResponse]
    next_offset: str = None
    response_headers: Dict[Any, Any] = None


@dataclass
class DeleteResponse:
    comment: CommentResponse
    response_headers: Dict[Any, Any] = None
