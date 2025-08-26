from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast


@dataclass
class Configuration:
    env: environment.Environment

    def list(self, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("configurations"),
            self.env,
            None,
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
        )
