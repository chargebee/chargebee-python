from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.models import billing_line_item


@dataclass
class BillingMetadata:
    env: environment.Environment

    pass
