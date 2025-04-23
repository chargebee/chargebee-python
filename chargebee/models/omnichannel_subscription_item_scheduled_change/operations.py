from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class OmnichannelSubscriptionItemScheduledChange:

    env: environment.Environment

    class ChangeType(Enum):
        DOWNGRADE = "downgrade"

        def __str__(self):
            return self.value

    class CurrentState(TypedDict):
        item_id_at_source: NotRequired[str]

    class ScheduledState(TypedDict):
        item_id_at_source: NotRequired[str]

    pass
