class Environment(object):

    chargebee_domain = None
    protocol= "https"
    API_VERSION = "v2"
    http_timeout = 20

    def __init__(self, options):
        self.api_key = options['api_key']
        self.site = options['site']

        if self.chargebee_domain is None:
            self.api_endpoint = f'https://{self.site}.chargebee.com/api/{self.API_VERSION}'
        else:
            self.api_endpoint = f'http://{self.site}.{self.chargebee_domain}/api/{self.API_VERSION}'

    def api_url(self, url):
        return self.api_endpoint + url
