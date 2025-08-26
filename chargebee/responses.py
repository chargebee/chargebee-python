import importlib
from dataclasses import fields
from typing import Type, TypeVar, Any, get_type_hints

T = TypeVar("T")


def parse_any_type_data(data):
    if isinstance(data, dict):
        return dict(data)
    elif isinstance(data, list):
        return list(data)
    return data


def _is_primitive(field_type):
    return field_type in (int, str, float, bool)


class Response(object):
    IDEMPOTENCY_REPLAYED_HEADER = "chargebee-idempotency-replayed"

    def __init__(
        self, response_type: Type[T], response, response_header=None, http_code=None
    ):
        self._response = response
        self._is_list_response = "list" in response
        if self._is_list_response:
            self._response = response["list"]
            self._next_offset = response.get("next_offset", None)
        self._response_header = response_header
        self._response_type = response_type
        self._response_status_code = http_code

    def is_idempotency_replayed(self) -> bool:
        return bool(self._response_header.get(self.IDEMPOTENCY_REPLAYED_HEADER, False))

    def http_status_code(self) -> int:
        return int(self._response_status_code)

    def parse(self) -> T:
        return (
            self.parse_list_response()
            if self._is_list_response
            else self.parse_response()
        )

    def parse_response(self) -> T:
        init_data = {}
        for name, type in get_type_hints(self._response_type).items():
            field_name = name
            field_type = type
            if field_name == "is_idempotency_replayed":
                init_data["is_idempotency_replayed"] = self.is_idempotency_replayed()
            if field_name in self._response:
                if hasattr(field_type, "__origin__") and field_type.__origin__ == list:
                    list_data = []
                    for response in self._response:
                        data = {}
                        for inner_name, inner_type in get_type_hints(
                            field_type.__args__[0]
                        ).items():
                            inner_field_name = inner_name
                            inner_field_type = inner_type
                            if inner_field_name in response:
                                if _is_primitive(inner_field_type):
                                    data[inner_field_name] = response[inner_field_name]
                                else:
                                    data[inner_field_name] = inner_field_type.construct(
                                        response[inner_field_name]
                                    )
                        list_data.append(field_type.__args__[0](**data))
                    init_data[field_name] = list_data
                elif _is_primitive(field_type):
                    init_data[field_name] = self._response[field_name]
                else:
                    if field_type == Any:
                        init_data[field_name] = parse_any_type_data(
                            self._response[field_name]
                        )
                    else:
                        init_data[field_name] = field_type.construct(
                            self._response[field_name]
                        )

            init_data["headers"] = self._response_header
            init_data["http_status_code"] = self._response_status_code

        return self._response_type(**init_data)

    def parse_list_response(self) -> T:
        result = {}
        for name, type in get_type_hints(self._response_type).items():
            field_name = name
            field_type = type

            if hasattr(field_type, "__origin__") and field_type.__origin__ == list:
                list_data = []
                for response in self._response:
                    data = {}
                    for inner_name, inner_type in get_type_hints(
                        field_type.__args__[0]
                    ).items():
                        inner_field_name = inner_name
                        inner_field_type = inner_type
                        if inner_field_name in response:
                            if _is_primitive(inner_field_type):
                                data[inner_field_name] = response[inner_field_name]
                            if field_type == Any:
                                data[inner_field_name] = parse_any_type_data(
                                    response[inner_field_name]
                                )
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
