from __future__ import absolute_import

import sys

try:
    import simplejson as json
except ImportError:
    import json

is_py2 = sys.version_info[0] == 2
is_py3 = sys.version_info[0] == 3

if is_py2:
    from urllib import urlencode
    from urlparse import urlparse
    from urllib2 import urlopen as _urlopen, Request
    from httplib import HTTPSConnection
elif is_py3:
    from urllib.parse import urlencode, urlparse
    from urllib.request import urlopen as _urlopen, Request
    from http.client import HTTPSConnection
