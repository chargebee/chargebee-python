import sys

try:
    import simplejson as json
except ImportError:
    import json

py_major_v = sys.version_info[0]
py_minor_v = sys.version_info[1]

if py_major_v >= 3:
    from urllib.parse import urlencode, urlparse
