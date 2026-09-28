from dataclasses import dataclass
from chargebee.model import Model
from typing import Dict, List, Any
from chargebee.response import Response

@dataclass
class AllowedValueResponse(Model):
    raw_data: Dict[Any, Any] = None
    value: str = None
    description: str = None


@dataclass
class ValueSchemaItemsResponse(Model):
    raw_data: Dict[Any, Any] = None
    type: str = None
    allowed_values: List[AllowedValueResponse] = None


@dataclass
class ValueSchema(Model):
    raw_data: Dict[Any, Any] = None
    type: str = None
    min_value: int = None
    max_value: int = None
    max_chars: int = None
    allowed_values: List[AllowedValueResponse] = None
    items: ValueSchemaItemsResponse = None


ValueSchemaResponse = ValueSchema


@dataclass
class ApplicabilityResponse(Model):
    raw_data: Dict[Any, Any] = None
    setting: str = None
    operator: str = None
    values: List[str] = None


@dataclass
class VariantCriteriaResponse(Model):
    raw_data: Dict[Any, Any] = None
    operand: str = None
    allowed_operator: str = None
    value_schema: ValueSchema = None


@dataclass
class PreferenceDefinitionResponse(Model):
    raw_data: Dict[Any, Any] = None
    id: str = None
    setting_group: str = None
    main_group: str = None
    sub_group: str = None
    description: str = None
    doc_link: str = None
    access_mode: str = None
    overridable_in_interface: bool = None
    overridable_in_api: bool = None
    applicability_operator: str = None
    is_namespace: bool = None
    key_internal_name: str = None
    applicability: List[ApplicabilityResponse] = None
    value_schema: ValueSchemaResponse = None
    variant_criteria: List[VariantCriteriaResponse] = None


@dataclass
class ListDefinitionsResponse(Response):

    preference_definition: PreferenceDefinitionResponse

