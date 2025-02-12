import importlib
from dataclasses import fields
from typing import Type, TypeVar, Any

T = TypeVar("T")


def _is_primitive(field_type):
    return field_type in (int, str, float, bool)


def get_class_from_string(class_path: str):
    module_name, class_name = class_path.rsplit(".", 1)
    module_path = "chargebee.models." + module_name + ".responses"
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


class Response(object):
    IDEMPOTENCY_REPLAYED_HEADER = "chargebee-idempotency-replayed"

    def __init__(
        self, response_type: Type[T], response, response_header=None, http_code=None
    ):
        self._response = response
        if "list" in response:
            self._response = response["list"]
            self._next_offset = response.get("next_offset", None)
        self._response_header = response_header
        self._response_type = response_type
        self._response_status_code = http_code

    def is_idempotency_replayed(self) -> bool:
        return bool(self._response_header.get(self.IDEMPOTENCY_REPLAYED_HEADER, False))

    def http_status_code(self) -> bool:
        return bool(self._response_status_code)

    def parse_response(self) -> T:
        init_data = {}
        for field in fields(self._response_type):
            field_name = field.name
            field_type = field.type
            if field_name == "is_idempotency_replayed":
                init_data["is_idempotency_replayed"] = self.is_idempotency_replayed()
            if field_name in self._response:
                if hasattr(field_type, "__origin__") and field_type.__origin__ == list:
                    list_data = []
                    for response in self._response:
                        data = {}
                        for inner_field in fields(field_type.__args__[0]):
                            inner_field_name = inner_field.name
                            inner_field_type = inner_field.type
                            if inner_field_name in response:
                                if _is_primitive(inner_field_type):
                                    data[inner_field_name] = response[inner_field_name]
                                else:
                                    if type(inner_field_type) == str:
                                        inner_field_type = get_class_from_string(
                                            inner_field_type
                                        )
                                    data[inner_field_name] = inner_field_type.construct(
                                        response[inner_field_name]
                                    )
                        list_data.append(field_type.__args__[0](**data))
                    init_data[field_name] = list_data
                elif _is_primitive(field_type):
                    init_data[field_name] = self._response[field_name]
                else:
                    if type(field_type) == str:
                        field_type = get_class_from_string(field_type)
                    if field_type == Any:
                        init_data[field_name] = self._response[field_name]
                    else:
                        init_data[field_name] = field_type.construct(
                            self._response[field_name]
                        )

            init_data["headers"] = self._response_header
            init_data["http_status_code"] = self._response_status_code

        return self._response_type(**init_data)

    def parse_list_response(self) -> T:
        result = {}
        for field in fields(self._response_type):
            field_name = field.name
            field_type = field.type

            if hasattr(field_type, "__origin__") and field_type.__origin__ == list:
                list_data = []
                for response in self._response:
                    data = {}
                    for inner_field in fields(field_type.__args__[0]):
                        inner_field_name = inner_field.name
                        inner_field_type = inner_field.type
                        if inner_field_name in response:
                            if _is_primitive(inner_field_type):
                                data[inner_field_name] = response[inner_field_name]
                            else:
                                if type(inner_field_type) == str:
                                    inner_field_type = get_class_from_string(
                                        inner_field_type
                                    )
                                if field_type == Any:
                                    data[inner_field_name] = response[inner_field_name]
                                else:
                                    data[inner_field_name] = inner_field_type.construct(
                                        response[inner_field_name]
                                    )

                    list_data.append(field_type.__args__[0](**data))

                result[field_name] = list_data
                result["next_offset"] = self._next_offset
                result["headers"] = self._response_header
                result["http_status_code"] = self._response_status_code

        return self._response_type(**result)
