class Environment(object):

    chargebee_domain = None
    protocol= "https"
    API_VERSION = "v2"
    connect_timeout = 30
    read_timeout = 80

    def __init__(self, options):
        self.api_key = options['api_key']
        self.site = options['site']

        if self.chargebee_domain is None:
            self.api_endpoint = 'https://%s.chargebee.com/api/%s' % (self.site, self.API_VERSION)
        else:
            self.api_endpoint = 'http://%s.%s/api/%s' % (self.site, self.chargebee_domain, self.API_VERSION)

    def api_url(self, url, subDomain=None):
        if subDomain is None:
            return self.api_endpoint + url
        else:
            if self.chargebee_domain is None:
               return 'https://%s.%s.chargebee.com/api/%s' % (self.site,subDomain, self.API_VERSION) + url
            else:
               return 'http://%s.%s.%s/api/%s' % (self.site, subDomain, self.chargebee_domain, self.API_VERSION) + url
