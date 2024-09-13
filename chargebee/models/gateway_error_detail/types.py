from typing import TypedDict, Required, NotRequired, Dict, List, Any


class GatewayErrorDetails(TypedDict):
    request_id: NotRequired[str]
    error_category: NotRequired[str]
    error_code: NotRequired[str]
    error_message: NotRequired[str]
    decline_code: NotRequired[str]
    decline_message: NotRequired[str]
    network_error_code: NotRequired[str]
    network_error_message: NotRequired[str]
    error_field: NotRequired[str]
    recommendation_code: NotRequired[str]
    recommendation_message: NotRequired[str]
    processor_error_code: NotRequired[str]
    processor_error_message: NotRequired[str]
