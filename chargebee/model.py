from chargebee.compat import json
from typing import get_type_hints, get_origin, get_args


class Model(object):
    def __init__(self, values):
        self.raw_data = values
        self._response_type = self.__class__

    def __str__(self):
        return json.dumps(self.raw_data, indent=4)

    def __getattr__(self, name):
        raise AttributeError("Attribute %s not found " % name)

    def hydrate(self, depth=0):
        if depth > 10:
            return

        type_map = {
            name: type_ for name, type_ in get_type_hints(self.__class__).items()
        }
        for k, v in list(self.raw_data.items()):
            val = None
            field_type = type_map.get(k, None)
            if isinstance(v, dict):
                if field_type and hasattr(field_type, "construct"):
                    val = field_type.construct(v, depth=depth + 1)
                else:
                    val = v
            elif isinstance(v, (list, tuple)):
                if field_type and get_origin(field_type) in (list, tuple):
                    item_type = (
                        get_args(field_type)[0] if get_args(field_type) else None
                    )
                    val = []
                    for item in v:
                        if (
                            isinstance(item, dict)
                            and item_type
                            and hasattr(item_type, "construct")
                        ):
                            val.append(item_type.construct(item, depth=depth + 1))
                        else:
                            val.append(item)
                else:
                    val = [
                        (
                            self.construct(item, depth=depth + 1)
                            if isinstance(item, dict)
                            else item
                        )
                        for item in v
                    ]
            else:
                val = v

            setattr(self, k, val)

    @classmethod
    def construct(cls, values, depth=0):
        obj = cls(values)
        obj.hydrate(depth=depth + 1)
        return obj
