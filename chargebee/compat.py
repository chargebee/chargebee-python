
from chargebee.main import Environment

import re
import sys
import socket

try:
    import simplejson as json
except ImportError:
    import json

py_major_v = sys.version_info[0]
py_minor_v = sys.version_info[1]

if py_major_v < 3:
    from urllib import urlencode
    from urlparse import urlparse
    from urllib2 import urlopen as _urlopen, Request
elif py_major_v >= 3:
    from urllib.parse import urlencode, urlparse
    from urllib.request import urlopen as _urlopen, Request



try:
    SSLError = None
    ssl = None
    
    if Environment.chargebee_domain is None:
        HTTPSConnection = object
    else:
        HTTPConnection = object
            
    if py_major_v < 3:
        from httplib import HTTPConnection, HTTPSConnection, HTTPException
    else:
        from http.client import HTTPConnection, HTTPSConnection, HTTPException

    import ssl
    SSLError = ssl.SSLError

except (ImportError, AttributeError):  # Platform-specific: No SSL
    pass


class VerifiedHTTPSConnection(HTTPSConnection):
    """Based on httplib.HTTPSConnection but wraps socket with SSL certification"""

    def set_cert(self, ca_certs, cert_reqs='CERT_REQUIRED'):
        ssl_req_scheme = {
            'CERT_NONE': ssl.CERT_NONE,
            'CERT_OPTIONAL': ssl.CERT_OPTIONAL,
            'CERT_REQUIRED': ssl.CERT_REQUIRED
        }

        self.cert_reqs = ssl_req_scheme.get(cert_reqs) or ssl.CERT_NONE
        self.ca_certs = ca_certs

    def connect(self):
        # Add certificate verification
        sock = socket.create_connection((self.host, self.port), self.timeout)

        # Wrap socket using verification with the root certs in
        # trusted_root_certs
        self.sock = ssl.wrap_socket(sock, cert_reqs=self.cert_reqs, ca_certs=self.ca_certs)

        if self.ca_certs:
            match_hostname(self.sock.getpeercert(), self.host)


class CertificateError(ValueError):
    pass


def _dnsname_to_pat(dn):
    pats = []
    for frag in dn.split(r'.'):
        if frag == '*':
            # When '*' is a fragment by itself, it matches a non-empty dotless
            # fragment.
            pats.append('[^.]+')
        else:
            # Otherwise, '*' matches any dotless fragment.
            frag = re.escape(frag)
            pats.append(frag.replace(r'\*', '[^.]*'))
    return re.compile(r'\A' + r'\.'.join(pats) + r'\Z', re.IGNORECASE)


def match_hostname(cert, hostname):
    """Verify that *cert* (in decoded format as returned by
    SSLSocket.getpeercert()) matches the *hostname*.  RFC 2818 rules
    are mostly followed, but IP addresses are not accepted for *hostname*.

    CertificateError is raised on failure. On success, the function
    returns nothing.
    """

    if not cert:
        raise ValueError("empty or no certificate")
    dnsnames = []
    san = cert.get('subjectAltName', ())
    for key, value in san:
        if key == 'DNS':
            if _dnsname_to_pat(value).match(hostname):
                return
            dnsnames.append(value)
    if not dnsnames:
        # The subject is only checked when there is no dNSName entry
        # in subjectAltName
        for sub in cert.get('subject', ()):
            for key, value in sub:
                # XXX according to RFC 2818, the most specific Common Name
                # must be used.
                if key == 'commonName':
                    if _dnsname_to_pat(value).match(hostname):
                        return
                    dnsnames.append(value)
    if len(dnsnames) > 1:
        raise CertificateError("hostname %r "
                               "doesn't match either of %s"
                               % (hostname, ', '.join(map(repr, dnsnames))))
    elif len(dnsnames) == 1:
        raise CertificateError("hostname %r "
                               "doesn't match %r"
                               % (hostname, dnsnames[0]))
    else:
        raise CertificateError("no appropriate commonName or "
                               "subjectAltName fields were found")
