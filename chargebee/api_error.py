class APIError(Exception):

    def __init__(self, http_code,json_obj,headers):
        Exception.__init__(self, json_obj.get('message'))
        self.json_obj = json_obj
        self.http_status_code = http_code
        self.type = json_obj.get('type')
        self.api_error_code = json_obj.get('api_error_code')
        self.param = json_obj.get('param')
        self.http_headers = headers
        
        self.error_code = json_obj['error_code']
        self.http_code = http_code
        self.http_body = None

class PaymentError(APIError):
    def __init__(self, http_code,json_obj,headers):
        APIError.__init__(self, http_code,json_obj,headers)

class InvalidRequestError(APIError):
    def __init__(self, http_code,json_obj,headers):
        APIError.__init__(self, http_code,json_obj,headers)

class OperationFailedError(APIError):
    def __init__(self, http_code,json_obj,headers):
        APIError.__init__(self, http_code,json_obj,headers)


