from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.filters import Filters


@dataclass
class BusinessRuleset:
    env: environment.Environment

    class ExecuteMode(Enum):
        STOP_ON_FIRST_TRUE = "stop_on_first_true"
        STOP_ON_FIRST_FALSE = "stop_on_first_false"
        EXECUTE_ALL = "execute_all"
        EXECUTE_ALL_TRUE = "execute_all_true"

        def __str__(self):
            return self.value

    class CreateParams(TypedDict):
        id: NotRequired[str]
        name: Required[str]
        description: NotRequired[str]
        execute_mode: NotRequired["BusinessRuleset.ExecuteMode"]
        rules: NotRequired[List[Dict[Any, Any]]]

    class UpdateParams(TypedDict):
        name: Required[str]
        description: NotRequired[str]
        execute_mode: NotRequired["BusinessRuleset.ExecuteMode"]
        rules: NotRequired[List[Dict[Any, Any]]]

    class AddRulesParams(TypedDict):
        rules: NotRequired[List[Dict[Any, Any]]]

    class RemoveRulesParams(TypedDict):
        rules: NotRequired[List[Dict[Any, Any]]]

    class ListRulesParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        active: NotRequired[Filters.BooleanFilter]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        active: NotRequired[Filters.BooleanFilter]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "rules": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rulesets"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="create",
        )

    def update(self, id, params: UpdateParams, headers=None) -> UpdateResponse:
        jsonKeys = {
            "rules": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rulesets", id),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="update",
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rulesets", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="delete",
        )

    def activate(self, id, headers=None) -> ActivateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rulesets", id, "activate"),
            self.env,
            None,
            headers,
            ActivateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="activate",
        )

    def deactivate(self, id, headers=None) -> DeactivateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rulesets", id, "deactivate"),
            self.env,
            None,
            headers,
            DeactivateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="deactivate",
        )

    def add_rules(
        self, id, params: AddRulesParams = None, headers=None
    ) -> AddRulesResponse:
        jsonKeys = {
            "rules": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rulesets", id, "add_rules"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            AddRulesResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="addRules",
        )

    def remove_rules(
        self, id, params: RemoveRulesParams = None, headers=None
    ) -> RemoveRulesResponse:
        jsonKeys = {
            "rules": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rulesets", id, "remove_rules"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            RemoveRulesResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="removeRules",
        )

    def list_rules(
        self, id, params: ListRulesParams = None, headers=None
    ) -> ListRulesResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("business_rulesets", id, "rules"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListRulesResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="listRules",
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("business_rulesets"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="list",
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("business_rulesets", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRuleset",
            operation="retrieve",
        )
