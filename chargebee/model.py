from chargebee.compat import json


class Model(object):
    
    fields = []

    def __init__(self, values, sub_types=None):
        if sub_types is None:
            sub_types = {}

        self.values = values
        self.sub_types = sub_types
        for field in self.fields:
            setattr(self, field, None)

    def __str__(self):
        return json.dumps(self.values, indent=4)

    def load(self, values):
        for k, v in values.items():
            set_val = None
            if isinstance(v, dict):
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
    def construct(cls, values, sub_types=None):
        obj = cls(values, sub_types)
        obj.load(values)
        return obj
    
