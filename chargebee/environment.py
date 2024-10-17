class Environment(object):
    chargebee_domain = "chargebee.com"
    protocol = "https"
    API_VERSION = "v2"
    connect_timeout = 30
    read_timeout = 80
    export_retry_delay_ms = 10000
    time_travel_retry_delay_ms = 3000

    def __init__(self, options):
        self.api_key = options["api_key"]
        self.site = options["site"]
        self.api_endpoint = "%s://%s.%s/api/%s" % (
            self.protocol,
            self.site,
            self.chargebee_domain,
            self.API_VERSION,
        )

    def api_url(self, url):
        return self.api_endpoint + url
