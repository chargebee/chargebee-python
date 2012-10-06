import json

def sample_auth_error():
    return json.dumps({
        "error_code": "api_authentication_invalid_key",
        "http_status_code": 401,
        "error_msg":"Sorry, authentication failed. Invalid api key"
    })

def sample_param_error():
    return json.dumps({
        "error_code": "param_required",
        "http_status_code": 400,
        "error_msg": "cannot be blank",
        "error_param": "card[gateway]"
    })
