from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum


@dataclass
class OfferEvent:
    env: environment.Environment

    class Type(Enum):
        VIEWED = "viewed"
        DISMISSED = "dismissed"

        def __str__(self):
            return self.value

    class OfferEventsParams(TypedDict):
        personalized_offer_id: Required[str]
        type: Required["OfferEvent.Type"]

    def offer_events(
        self, params: OfferEventsParams, headers=None
    ) -> OfferEventsResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "post",
            request.uri_path("offer_events"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            OfferEventsResponse,
            "grow",
            True,
            jsonKeys,
            options,
        )
