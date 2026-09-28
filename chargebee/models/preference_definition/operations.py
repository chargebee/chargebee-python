from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters
from chargebee.models import enums

@dataclass
class PreferenceDefinition:

    env: environment.Environment
    class ApplicabilityOperator(Enum):
        AND = "and"
        OR = "or"

        def __str__(self):
            return self.value

    class Operator(Enum):
        IS = "is"
        IN = "in"

        def __str__(self):
            return self.value
    class VariantCriteriaAllowedOperator(Enum):
        IS = "is"
        IN = "in"

        def __str__(self):
            return self.value

    class Applicability(TypedDict):
        setting: NotRequired[str]
        operator: NotRequired["PreferenceDefinition.Operator"]
        values: NotRequired[List[str]]

    class VariantCriteria(TypedDict):
        operand: NotRequired[enums.Operand]
        allowed_operator: NotRequired["PreferenceDefinition.VariantCriteriaAllowedOperator"]
        value_schema: NotRequired[ValueSchema]



    class ListDefinitionsParams(TypedDict):
        setting_group: Required[Filters.EnumFilter]

    def list_definitions(self, params: ListDefinitionsParams, headers=None) -> ListDefinitionsResponse:
        jsonKeys = {
        
        }
        options = {
        
        }
        return request.send(
            "get",
            request.uri_path("preferences", "definitions"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListDefinitionsResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="preferenceDefinition",
            operation="listDefinitions",
        )