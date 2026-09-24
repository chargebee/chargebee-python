from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


@dataclass
class ApplyRule:
    env: environment.Environment

    class Rule(TypedDict):
        id: Required[str]
        version: NotRequired[int]
        name: NotRequired[str]
        description: NotRequired[str]
        evaluation_result: NotRequired[bool]
        error_message: NotRequired[str]
        actions: NotRequired[List[Dict[Any, Any]]]

    pass
