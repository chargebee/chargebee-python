from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


@dataclass
class SubscriptionEntitlementsCreatedDetail:
    env: environment.Environment

    pass
