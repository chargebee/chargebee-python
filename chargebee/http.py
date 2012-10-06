import urllib
import urllib2
import base64
import json

from chargebee import APIError

def _basic_auth_str(username):
    return 'Basic ' + base64.b64encode(('%s:' % username).encode('latin1')).strip().decode('latin1')

def request(method, url, env, params=None):
    if not env:
        raise APIError('No environment configured.')

    headers = {}

    url = env.api_url(url)

    if method.lower() in ('get', 'head', 'delete'):
        url = '%s?%s' % (url, urllib.urlencode(params))
        payload = None
    else:
        payload = params

    headers.update({
        'User-Agent': 'ChargeBee-Python-Client',
        'accept': 'json',
    })

    request = urllib2.Request(url, payload, headers)
    request.add_header('Authorization', _basic_auth_str(env.api_key))

    return urllib2.urlopen(request)


def process_response(response, http_code):
    resp_json = json.loads(response)

    if http_code < 200 or http_code > 299:
        pass


def handle_api_resp_error(http_code, resp_json):
    message = ''

    if 'error_param' in resp_json:
        message = 'param %s ' % resp_json['error_param']

    message += resp_json['error_msg']

    raise APIError(message, http_code, 0, resp_json)
