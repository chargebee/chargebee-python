import base64

from chargebee import APIError,PaymentError,InvalidRequestError,OperationFailedError, compat
from chargebee.main import ChargeBee
from chargebee.main import Environment
from chargebee.version import VERSION

def _basic_auth_str(username):
    return 'Basic ' + base64.b64encode(('%s:' % username).encode('latin1')).strip().decode('latin1')


def request(method, url, env, params=None, headers=None):
    if not env:
        raise Exception('No environment configured.')
    if headers is None:
        headers = {}

    url = env.api_url(url)
    if method.lower() in ('get', 'head', 'delete'):
        url = '%s?%s' % (url, compat.urlencode(params))
        payload = None
    else:
        payload = compat.urlencode(params)
        headers['Content-type'] = 'application/x-www-form-urlencoded'

    headers.update({
        'User-Agent': 'ChargeBee-Python-Client v%s' % VERSION,
        'Accept': 'application/json',
        'Authorization': _basic_auth_str(env.api_key),
    })

    meta = compat.urlparse(url)
    if ChargeBee.verify_ca_certs:
        connection = compat.VerifiedHTTPSConnection(meta.netloc)
        connection.set_cert(ca_certs=ChargeBee.ca_cert_path)
    else:
        if Environment.protocol == "https":
            connection = compat.HTTPSConnection(meta.netloc)
        else:
            connection = compat.HTTPConnection(meta.netloc)    
        
    connection.request(method.upper(), meta.path + '?' + meta.query, payload, headers)
    try:
        response = connection.getresponse()
        data = response.read()
        if compat.py_major_v >= 3:
            data = data.decode('utf-8')

        return process_response(url,data, response.status)
    finally:
        connection.close()


def process_response(url,response, http_code):
    try:
        resp_json = compat.json.loads(response)
    except Exception as ex:     
        raise Exception("Response not in JSON format. Probably not a chargebee error. \n URL is " + url + "\n Content is \n" + response)
    if http_code < 200 or http_code > 299:
        handle_api_resp_error(url,http_code, resp_json)

    return resp_json


def handle_api_resp_error(url,http_code, resp_json):
    if 'api_error_code' not in resp_json:
        raise Exception("The api_error_code is not present. Probably not a chargebee error. \n URL is " + url + "\nContent is \n " + str(resp_json))

    if 'payment' == resp_json.get('type'):
        raise PaymentError(http_code, resp_json)
    elif 'operation_failed' == resp_json.get('type'):
        raise OperationFailedError(http_code, resp_json)
    elif 'invalid_request' == resp_json.get('type'):
        raise InvalidRequestError(http_code, resp_json)
    else:
        raise APIError(http_code, resp_json)


