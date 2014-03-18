def serialize(value, prefix=None, idx=None):

    serialized = {}

    if isinstance(value, dict):
        for k, v in value.items():
            if isinstance(v, (dict, list, tuple)):
                serialized.update(serialize(v, k))
            else:
                key = ''.join([
                    prefix or '',
                    '[%s]' % k if prefix is not None else k,
                    '[%s]' % idx if idx is not None else '',
                ])
                serialized.update({key: get_as_str(v)})

    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            serialized.update(serialize(v, prefix, i))

    else:
        if prefix is not None and idx is not None:
            key = prefix + '[' + str(idx) +']'
            serialized.update({key: get_as_str(value)})
        else:
            raise TypeError("only hash or arrays are allowed as value")

    return serialized

def get_as_str(val):
    if val is None:
        return ''
    elif isinstance(val, bool):
        return str(val).lower()
    else:
        return val;
