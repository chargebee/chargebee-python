import sys
try:
    import simplejson as json
except ImportError:
    import json

is_py2 = sys.version_info[0] == 2
is_py3 = sys.version_info[0] == 3

if is_py2:
    from urllib import urlencode
    from urllib2 import urlopen as _urlopen, Request
elif is_py3:
    from urllib.parse import urlencode
    from urllib.request import urlopen as _urlopen, Request

def urlopen(url):
    if is_py2:
        return _urlopen(url).read()

    response = _urlopen(url)
    encoding = response.headers.get_content_charset()

    return response.readall().decode(encoding)
