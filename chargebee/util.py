from chargebee import compat
from collections import OrderedDict

def serialize(value, prefix=None, idx=None):

    serialized = OrderedDict()

    if isinstance(value, dict):
        for k, v in list(value.items()):
            # these fields are encoded as a JSON string instead of URL-encoded.
            if k in ('meta_data', 'metaData', 'checkout_info', 'metadata') and isinstance(v, dict):
                serialized.update({k: v})
            elif k in ('exemption_details', 'item_family_ids', 'item_price_periods', 'currencies') and isinstance(v, list):
                serialized.update({k: v})
            elif isinstance(v, (dict, list, tuple)):
                serialized.update(serialize(v, k))
            else:
                key = ''.join([
                    prefix or '',
                    '[%s]' % k if prefix is not None else k,
                    '[%s]' % idx if idx is not None else '',
                ])
                serialized.update({key: get_val(v)})

    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            serialized.update(serialize(v, prefix, i))

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
