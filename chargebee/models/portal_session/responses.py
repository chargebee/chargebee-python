from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response


@dataclass
class LinkedCustomerResponse(Model):
    customer_id: str = None
    email: str = None
    has_billing_address: bool = None
    has_payment_method: bool = None
    has_active_subscription: bool = None


@dataclass
class PortalSessionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    token: str = None
    access_url: str = None
    redirect_url: str = None
    status: str = None
    created_at: int = None
    expires_at: int = None
    customer_id: str = None
    login_at: int = None
    logout_at: int = None
    login_ipaddress: str = None
    logout_ipaddress: str = None
    linked_customers: List[LinkedCustomerResponse] = None


@dataclass
class CreateResponse(Response):
    portal_session: PortalSessionResponse
    headers: Dict[str, str] = None


@dataclass
class RetrieveResponse:
    portal_session: PortalSessionResponse
    headers: Dict[str, str] = None


@dataclass
class LogoutResponse(Response):
    portal_session: PortalSessionResponse
    headers: Dict[str, str] = None


@dataclass
class ActivateResponse(Response):
    portal_session: PortalSessionResponse
    headers: Dict[str, str] = None
