class APIError(Exception):

    def __init__(self, message, http_code=None, http_body=None, json_obj=None):
        self.message = message
        self.http_code = http_code
        self.http_body = http_body
        self.json_obj = json_obj

        if json_obj is not None:
            self.error_code = json_obj['error_code']
            self.param = json_obj.get('param')
        else:
            self.error_code = None
            self.param = None

    def __str__(self):
        hc = '' if not self.http_code else '(Http Code %s)' % self.http_code
        return ' '.join([hc, self.message])
