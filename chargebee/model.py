from chargebee.compat import json


class Model(object):
    fields = []           # field list
    repr_field = None     # field to use for repr(), default is fields[0]
    sub_types = {}        # mapping {attr: type}
    dependant_types = {}  # mapping {attr: type}. If type is a 1-tuple, indicates it's a list.

    def __init__(self, values):
        self.values = values
        for field in self.fields:
            setattr(self, field, None)

    def __repr__(self):
        repr_field = self.repr_field or self.fields[0]
        return "<chargebee.{}: {}={}>".format(self.__class__.__name__, repr_field, getattr(self, repr_field))

    def __str__(self):
        return json.dumps(self.values, indent=4)

    def load(self, values):
        for k, v in list(values.items()):
            set_val = None
            if isinstance(v, dict) and k in self.dependant_types:
                continue
            elif isinstance(v, dict):
                set_val = self.sub_types[k].construct(v) if k in self.sub_types else v
            elif isinstance(v, (list, tuple)):
                if k in self.sub_types:
                    set_val = [self.sub_types[k].construct(x) for x in v]
                else:
                    set_val = v
            else:
                set_val = v

            if k not in ('content',):  # Skipping models properties
                setattr(self, k, set_val)

    # Returns null for any attribute that starts with cf_ to access the custom fields.
    def __getattr__(self, name):
        if( name[0:3] == "cf_"):
            return None
        raise AttributeError("Attribute %s not found " % name)

    @classmethod
    def construct(cls, values):
        obj = cls(values)
        obj.load(values)
        for k, dependent_type in cls.dependant_types.items():
            if values.get(k) is not None:
                if isinstance(dependent_type, tuple):
                    # dependent type being a 1-tuple indicates a list
                    set_val = [dependent_type[0].construct(v) for v in values[k]]
                else:
                    set_val = dependent_type.construct(values[k])
                setattr(obj, k, set_val)
        return obj
