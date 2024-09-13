from typing import TypedDict, Required, NotRequired, Dict, List, Any


class Contacts(TypedDict):
    id: Required[str]
    first_name: NotRequired[str]
    last_name: NotRequired[str]
    email: Required[str]
    phone: NotRequired[str]
    label: NotRequired[str]
    enabled: Required[bool]
    send_account_email: Required[bool]
    send_billing_email: Required[bool]
