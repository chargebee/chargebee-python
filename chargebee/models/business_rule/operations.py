from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from chargebee.filters import Filters


@dataclass
class BusinessRule:
    env: environment.Environment

    class CreateParams(TypedDict):
        id: NotRequired[str]
        name: Required[str]
        description: NotRequired[str]
        tags: NotRequired[List[Dict[Any, Any]]]
        structured_expression: Required[Dict[Any, Any]]
        actions_on_success: NotRequired[List[Dict[Any, Any]]]

    class UpdateDraftParams(TypedDict):
        name: Required[str]
        description: NotRequired[str]
        tags: NotRequired[List[Dict[Any, Any]]]
        structured_expression: Required[Dict[Any, Any]]
        actions_on_success: NotRequired[List[Dict[Any, Any]]]

    class ListParams(TypedDict):
        limit: NotRequired[int]
        offset: NotRequired[str]
        draft: NotRequired[Filters.BooleanFilter]
        active: NotRequired[Filters.BooleanFilter]

    class ApplyRulesParams(TypedDict):
        evaluate: NotRequired[bool]
        rule_id: NotRequired[str]
        ruleset_id: NotRequired[str]
        skip_failed_rules: NotRequired[bool]
        structured_expression: NotRequired[Dict[Any, Any]]
        context: NotRequired[Dict[Any, Any]]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {
            "tags": 0,
            "structured_expression": 0,
            "actions_on_success": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rules"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="create",
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rules", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="delete",
        )

    def update_draft(
        self, id, params: UpdateDraftParams, headers=None
    ) -> UpdateDraftResponse:
        jsonKeys = {
            "tags": 0,
            "structured_expression": 0,
            "actions_on_success": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rules", id, "draft"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            UpdateDraftResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="updateDraft",
        )

    def list(self, params: ListParams = None, headers=None) -> ListResponse:
        jsonKeys = {}
        options = {}
        return request.send_list_request(
            "get",
            request.uri_path("business_rules"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ListResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="list",
        )

    def retrieve(self, id, headers=None) -> RetrieveResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("business_rules", id),
            self.env,
            None,
            headers,
            RetrieveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="retrieve",
        )

    def retrieve_draft(self, id, headers=None) -> RetrieveDraftResponse:
        jsonKeys = {}
        options = {}
        return request.send(
            "get",
            request.uri_path("business_rules", id, "draft"),
            self.env,
            None,
            headers,
            RetrieveDraftResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="retrieveDraft",
        )

    def delete_draft(self, id, headers=None) -> DeleteDraftResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rules", id, "delete_draft"),
            self.env,
            None,
            headers,
            DeleteDraftResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="deleteDraft",
        )

    def activate_rule(self, id, headers=None) -> ActivateRuleResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rules", id, "activate"),
            self.env,
            None,
            headers,
            ActivateRuleResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="activateRule",
        )

    def deactivate_rule(self, id, headers=None) -> DeactivateRuleResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rules", id, "deactivate"),
            self.env,
            None,
            headers,
            DeactivateRuleResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="deactivateRule",
        )

    def release_rule(self, id, headers=None) -> ReleaseRuleResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rules", id, "release"),
            self.env,
            None,
            headers,
            ReleaseRuleResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="releaseRule",
        )

    def apply_rules(
        self, params: ApplyRulesParams = None, headers=None
    ) -> ApplyRulesResponse:
        jsonKeys = {
            "structured_expression": 0,
            "context": 0,
        }
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("business_rules", "apply_rules"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            ApplyRulesResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="businessRule",
            operation="applyRules",
        )
