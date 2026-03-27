from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any


@dataclass
class CpqQuoteSignatureResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    status: str = None
    name: str = None
    document_name: str = None
    customer_acceptance_method: str = None
    quote_type: str = None
    expires_at: int = None
    timezone: str = None
    provider_request_id: str = None
    provider_document_id: str = None
    created_at: int = None
    modified_at: int = None
