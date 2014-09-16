class Environment(object):

    chargebee_domain = None
    protocol= "https"

    def __init__(self, options):
        self.api_key = options['api_key']
        self.site = options['site']

        if self.chargebee_domain is None:
            self.api_endpoint = 'https://%s.chargebee.com/api/v1' % self.site
        else:
            self.api_endpoint = 'http://%s.%s/api/v1' % (self.site, self.chargebee_domain)

    def api_url(self, url):
        return self.api_endpoint + url
