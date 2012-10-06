import base64

from chargebee import APIError
from chargebee import compat


def _basic_auth_str(username):
    return 'Basic ' + base64.b64encode(('%s:' % username).encode('latin1')).strip().decode('latin1')


def request(method, url, env, params=None):
    if not env:
        raise APIError('No environment configured.')

    headers = {}

    url = env.api_url(url)

    if method.lower() in ('get', 'head', 'delete'):
        url = '%s?%s' % (url, compat.urlencode(params))
        payload = None
    else:
        payload = compat.urlencode(params)
        headers['Content-type'] = 'application/x-www-form-urlencoded'

    headers.update({
        'User-Agent': 'ChargeBee-Python-Client',
        'Accept': 'json',
        'Authorization': _basic_auth_str(env.api_key),
    })

    meta = compat.urlparse(url)
    connection = compat.HTTPSConnection(meta.netloc)
    connection.request(method.upper(), meta.path + meta.query, payload, headers)

    try:
        response = connection.getresponse()
        data = response.read()
        if compat.is_py3:
            data = data.decode('utf-8')

        return process_response(data, response.status)

    finally:
        connection.close()


def process_response(response, http_code):
    resp_json = compat.json.loads(response)

    if http_code < 200 or http_code > 299:
        pass

    return resp_json


def handle_api_resp_error(http_code, resp_json):
    message = ''

    if 'error_param' in resp_json:
        message = 'param %s ' % resp_json['error_param']

    message += resp_json['error_msg']

    raise APIError(message, http_code, 0, resp_json)
