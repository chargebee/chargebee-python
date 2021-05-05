import re
from collections import namedtuple


class Environment(object):

    chargebee_domain = None
    protocol= "https"
    API_VERSION = "v2"

    def __init__(self, options):
        self.api_key = options['api_key']
        self.site = options['site']

        if self.chargebee_domain is None:
            self.api_endpoint = 'https://%s.chargebee.com/api/%s' % (self.site, self.API_VERSION)
        else:
            self.api_endpoint = 'http://%s.%s/api/%s' % (self.site, self.chargebee_domain, self.API_VERSION)

    def api_url(self, url):
        return self.api_endpoint + url


class MockEnvironment(Environment):
    Request = namedtuple('Request', ['method', 'url_path', 'payload'])

    def __init__(self, **options):
        params = {
            'api_key': 'mock-api-key',
            'site': 'mock-test',
        }
        params.update(options)
        super(MockEnvironment, self).__init__(params)

        self.clear()

    def clear(self):
        """ Clear any expected and previous requests """
        self.expecting = []
        self.requests = []

    def add(self, url_path, response_body, response_status=200, request_method=None):
        """
        Add a mock response.

        url_path is the API path after the API version. eg. '/subscriptions/1mkVvvHQiQMbLBBf/cancel'
            It can also be a regex pattern from re.compile()
        response_body is the JSON response body to return.
            It can be a string, a JSON-serializable dict, or a callable which
            will be called with (url_path, payload, method) and should return a (json_body_string, http_status) tuple.
        response_status is the HTTP response code to return.
            This is ignored if response_body is a callable.
        request_method optional HTTP method to check against the request

        >>> with chargebee.mock() as mock:
        >>>   mock.add('/subscriptions/1mkVvvHQiQMbLBBf/cancel', {"subscription": {...}})
        >>>   result = chargebee.Subscription.cancel('1mkVvvHQiQMbLBBf')
        >>>   subscription = result.subscription
        >>>   mock.requests
        [Request(method='POST', url_path='/subscriptions/1mkVvvHQiQMbLBBf/cancel', payload={})]
        >>>   chargebee.Subscription.list({})
        AssertionError: No more mock requests left: /subscriptions
        """
        self.expecting.append((url_path, request_method, response_body, response_status))

    def request(self, method, url, payload):
        """
        Called for each Chargebee request

        Adds the request content to MockEnvironment.requests
        Matches the next expected request and returns the associated content

        Returns a (json_body_string, http_status) tuple
        """
        from chargebee.compat import urlsplit, parse_qs, json

        url_obj = urlsplit(url)
        try:
            url_path = url_obj.path.split('/api/%s' % self.API_VERSION)[1]
        except IndexError:
            raise ValueError("Request URL (%s) didn't match endpoint %s" % (url, self.api_endpoint))

        # un-encode the body/querystring payload
        payload = parse_qs(payload or url_obj.query, keep_blank_values=True)

        # save to MockEnvironment.requests
        self.requests.append(MockEnvironment.Request(method, url_path, payload))

        # check the next expected request
        try:
            req_path, req_method, resp_body, resp_status = self.expecting.pop(0)
        except IndexError:
            raise AssertionError("No more mock requests left: %s" % url_path)

        # Match the URL path
        if isinstance(req_path, re._pattern_type):
            # url_path is a regex
            if not req_path.match(url_path):
                raise AssertionError("Request URL %s does not match %s" % (url_path, req_path.pattern))
        elif req_path != url_path:
            # url_path is a string
            raise AssertionError("Request URL %s != %s" % (url_path, req_path))

        # Match any request method
        if req_method and method != req_method.upper():
            raise AssertionError("Request Method %s != %s (%s)" % (method, req_method, url_path))

        # Return the response
        if callable(resp_body):
            # response_body is a callable, use it to generate the response
            return resp_body(url_path, payload, method)
        elif isinstance(resp_body, (dict, list, tuple)):
            # response body is a dict/sequence, JSON-encode it
            return (json.dumps(resp_body), resp_status)
        else:
            # string body
            return (resp_body, resp_status)
