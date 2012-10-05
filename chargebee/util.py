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
                serialized.update({key: v or ''})

    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            serialized.update(serialize(v, prefix, i))

    else:
        raise TypeError("only hash or arrays are allowed as value")

    return serialized
