import base64
import logging
import platform
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from chargebee import (APIError,PaymentError,InvalidRequestError,
OperationFailedError,compat)
from chargebee.main import ChargeBee
from chargebee.main import Environment
from chargebee.version import VERSION

_logger = logging.getLogger(__name__)


retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)

def _basic_auth_str(username):
    return 'Basic ' + base64.b64encode(('%s:' % username).encode('latin1')).strip().decode('latin1')


def request(method, url, env, params=None, headers=None):
    if not env:
        raise Exception('No environment configured.')
    if headers is None:
        headers = {}

    url = env.api_url(url)
    timeout = env.http_timeout
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
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
        'Lang-Version': str(compat.py_major_v) + "." + str(compat.py_minor_v),
        'OS-Version': platform.platform()
    })

    meta = compat.urlparse(url)
    request_args = {
        'method': method.upper(),
        'data': payload,
        'headers': headers,
        'timeout': timeout,
    }

    uri = meta.netloc + meta.path + '?' + meta.query

    if ChargeBee.verify_ca_certs:
        request_args.update({
            'verify': ChargeBee.ca_cert_path,
            'url': 'https://' + uri,
        })
        http.mount("https://", adapter)
    else:
        if Environment.protocol == "https":
            request_args.update({
                'url': 'https://' + uri,
            })
            http.mount("https://", adapter)
        else:
            request_args.update({
                'url': 'http://' + uri,
            })
            http.mount("http://", adapter)

    _logger.debug('{method} Request: {url}'.format(**request_args))
    _logger.debug('HEADERS: {0}'.format({k: v for k, v in headers.items() if k.lower() != "authorization"}))
    if payload:
        _logger.debug('PAYLOAD: {data}'.format(**request_args))

    response = http.request(**request_args)

    _logger.debug('{method} Response: {status_code} - {text}'.format(
        method=request_args['method'], status_code=response.status_code, text=response.text
    ))

    return process_response(url, response.text, response.status_code)


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


