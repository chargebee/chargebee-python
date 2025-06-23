import os

from collections import OrderedDict
from enum import Enum


def serialize(value, prefix=None, idx=None, jsonKeys=None, level=0):
    if level is None:
        level = 0

    if jsonKeys is None:
        jsonKeys = {}

    serialized = OrderedDict()

    if isinstance(value, dict):
        for k, v in list(value.items()):
            should_json_encode = k in jsonKeys and jsonKeys[k] == level
            if should_json_encode:
                key = f"{prefix or ''}{f'[{k}]' if prefix else k}{f'[{idx}]' if idx is not None else ''}"
                serialized.update({key: v})
            elif k in ("in", "not_in", "between") and isinstance(v, list):
                v = [str(i) for i in v]
                key = "".join(
                    [
                        prefix or "",
                        "[%s]" % k if prefix is not None else k,
                        "[%s]" % idx if idx is not None else "",
                    ]
                )
                serialized.update({key: str(v)})
            elif isinstance(v, (dict, list, tuple)):
                temp_prefix = f"{prefix}[{k}]" if prefix is not None else k
                serialized.update(serialize(v, temp_prefix, None, jsonKeys, level + 1))
            else:
                if isinstance(v, Enum):
                    v = str(v)
                key = "".join(
                    [
                        prefix or "",
                        "[%s]" % k if prefix is not None else k,
                        "[%s]" % idx if idx is not None else "",
                    ]
                )
                serialized.update({key: get_val(v)})

    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            serialized.update(serialize(v, prefix, i, jsonKeys, level))

    else:
        if prefix is not None and idx is not None:
            key = prefix + "[" + str(idx) + "]"
            serialized.update({key: get_val(value)})
        else:
            raise TypeError("only hash or arrays are allowed as value")

    return serialized


def get_val(val):
    if val is None:
        return ""
    elif isinstance(val, bool):
        return str(val).lower()
    else:
        return val


def generate_uuid_v4() -> str:
    # Generate 16 random bytes
    try:
        bytes_ = os.urandom(16)
    except NotImplementedError:
        # Fallback: insecure random if urandom not available (highly unlikely)
        import random

        bytes_ = bytes([random.randint(0, 255) for _ in range(16)])

    byte_array = list(bytes_)

    # Set version to 4 -> bits 12-15 of time_hi_and_version
    byte_array[6] = (byte_array[6] & 0x0F) | 0x40
    # Set variant to RFC 4122 -> bits 6-7 of clock_seq_hi_and_reserved
    byte_array[8] = (byte_array[8] & 0x3F) | 0x80

    hex_str = "".join(f"{byte:02x}" for byte in byte_array)

    return f"{hex_str[0:8]}-{hex_str[8:12]}-{hex_str[12:16]}-{hex_str[16:20]}-{hex_str[20:32]}"
