from typing import TypedDict, Required, NotRequired, Dict, List, Any
from enum import Enum
from chargebee.models import enums


class WebhookStatus(Enum):
    NOT_CONFIGURED = "not_configured"
    SCHEDULED = "scheduled"
    SUCCEEDED = "succeeded"
    RE_SCHEDULED = "re_scheduled"
    FAILED = "failed"
    SKIPPED = "skipped"
    NOT_APPLICABLE = "not_applicable"

    def __str__(self):
        return self.value


class WebhookWebhookStatus(Enum):
    NOT_CONFIGURED = "not_configured"
    SCHEDULED = "scheduled"
    SUCCEEDED = "succeeded"
    RE_SCHEDULED = "re_scheduled"
    FAILED = "failed"
    SKIPPED = "skipped"
    NOT_APPLICABLE = "not_applicable"

    def __str__(self):
        return self.value


class Webhook(TypedDict):
    id: Required[str]
    webhook_status: Required[WebhookWebhookStatus]


class Events(TypedDict):
    id: Required[str]
    occurred_at: Required[int]
    source: Required[enums.Source]
    user: NotRequired[str]
    webhook_status: Required[WebhookStatus]
    webhook_failure_reason: NotRequired[str]
    webhooks: NotRequired[List[Webhook]]
    event_type: NotRequired[enums.EventType]
    api_version: NotRequired[enums.ApiVersion]
    content: Required[Dict[Any, Any]]
    origin_user: NotRequired[str]
