import json

import chargebee


def request(method, url, env, params):
    raise NotImplementedError()


def process_response(response, http_code):
    resp_json = json.loads(response)

    if http_code < 200 or http_code > 299:
        pass

def handle_api_resp_error(http_code, resp_json):
    message = ''

    if 'error_param' in resp_json:
        message = 'param %s ' % resp_json['error_param']

    message += resp_json['error_msg']

    raise chargebee.APIError(message, http_code, 0, resp_json)
