from chargebee import compat
from collections import OrderedDict

def serialize(value, prefix=None, idx=None, json_keys = None, level = 0):

    if level is None:
        level = 0
        
    if json_keys is None:
        json_keys = {}
        
    serialized = OrderedDict()
    if isinstance(value, dict):
        for k, v in list(value.items()):
            should_json_encode = k in json_keys and json_keys[k] == level
            if should_json_encode:
                key = f"{prefix or ''}{f'[{k}]' if prefix else k}{f'[{idx}]' if idx is not None else ''}"
                serialized.update({key : v})
            elif isinstance(v, (dict, list, tuple)):
                temp_prefix = f"{prefix}[{k}]" if prefix is not None else k
                serialized.update(serialize(v, temp_prefix, None, json_keys, level+1))
            else:
                key = ''.join([
                    prefix or '',
                    '[%s]' % k if prefix is not None else k,
                    '[%s]' % idx if idx is not None else '',
                ])
                serialized.update({key: get_val(v)})

    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            serialized.update(serialize(v, prefix, i, json_keys, level))

    else:
        if prefix is not None and idx is not None:
            key = prefix + '[' + str(idx) +']'
            serialized.update({key: get_val(value)})
        else:
            raise TypeError("only hash or arrays are allowed as value")

    return serialized

def get_val(val):
    if val is None:
        return ''
    elif isinstance(val, bool):
        return str(val).lower()
    else:
        if compat.py_major_v < 3 and isinstance(val, unicode): 
              return val.encode("utf-8")
        else:
           return val;
