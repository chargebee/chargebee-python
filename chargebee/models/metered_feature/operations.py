from .responses import *
from chargebee import request, environment
from typing import TypedDict, Required, NotRequired, Dict, List, Any, cast
from enum import Enum
from chargebee.models import column_definition, feature


@dataclass
class MeteredFeature:
    env: environment.Environment

    class ColumnDefinitionDataType(Enum):
        NUMBER = "number"
        STRING = "string"

        def __str__(self):
            return self.value

    class FeatureStatus(Enum):
        ACTIVE = "active"
        ARCHIVED = "archived"
        DRAFT = "draft"

        def __str__(self):
            return self.value

    class FeatureType(Enum):
        SWITCH = "switch"
        CUSTOM = "custom"
        QUANTITY = "quantity"
        RANGE = "range"

        def __str__(self):
            return self.value

    class CreateColumnDefinitionParams(TypedDict):
        column_name: Required[str]
        data_type: Required["MeteredFeature.ColumnDefinitionDataType"]

    class CreateParams(TypedDict):
        name: Required[str]
        description: NotRequired[str]
        feature_unit: Required[str]
        query: Required[str]
        column_definitions: NotRequired[
            List["MeteredFeature.CreateColumnDefinitionParams"]
        ]

    def create(self, params: CreateParams, headers=None) -> CreateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("metered_features"),
            self.env,
            cast(Dict[Any, Any], params),
            headers,
            CreateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="meteredFeature",
            operation="create",
        )

    def archive(self, id, headers=None) -> ArchiveResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("metered_features", id, "archive_command"),
            self.env,
            None,
            headers,
            ArchiveResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="meteredFeature",
            operation="archive",
        )

    def reactivate(self, id, headers=None) -> ReactivateResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("metered_features", id, "reactivate_command"),
            self.env,
            None,
            headers,
            ReactivateResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="meteredFeature",
            operation="reactivate",
        )

    def delete(self, id, headers=None) -> DeleteResponse:
        jsonKeys = {}
        options = {
            "isIdempotent": True,
        }
        return request.send(
            "post",
            request.uri_path("metered_features", id, "delete"),
            self.env,
            None,
            headers,
            DeleteResponse,
            None,
            False,
            jsonKeys,
            options,
            resource="meteredFeature",
            operation="delete",
        )
