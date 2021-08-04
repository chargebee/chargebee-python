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
