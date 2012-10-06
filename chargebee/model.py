from chargebee.compat import json


class Model(object):

    def __init__(self, values, sub_types=None):
        if sub_types is None:
            sub_types = {}

        self.values = values
        self.sub_types = sub_types

    def __str__(self):
        return json.dumps(self.values)

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

            setattr(self, v, set_val)
