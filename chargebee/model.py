from chargebee.compat import json


class Model(object):

    def __init__(self, values):
        self.raw_data = values

    def __str__(self):
        return json.dumps(self.raw_data, indent=4)

    def __getattr__(self, name):
        raise AttributeError("Attribute %s not found " % name)

    def hydrate(self):
        for k, v in list(self.raw_data.items()):
            val = None
            if isinstance(v, dict):
                val = self.construct(v)
            elif isinstance(v, (list, tuple)):
                val = [
                    self.construct(item) if isinstance(item, dict) else item
                    for item in v
                ]
            else:
                val = v

            setattr(self, k, val)

    @classmethod
    def construct(cls, values):
        obj = cls(values)
        obj.hydrate()
        return obj
