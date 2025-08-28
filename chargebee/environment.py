from chargebee.retry_config import RetryConfig


class Environment(object):
    chargebee_domain = "chargebee.com"
    protocol = "https"
    API_VERSION = "v2"
    connect_timeout = 30
    read_timeout = 80
    export_retry_delay_ms = 10000
    time_travel_retry_delay_ms = 3000
    retry_config = RetryConfig()
    enable_debug_logs = False
    use_async_client = False

    def __init__(self, options):
        self.api_key = options["api_key"]
        self.site = options["site"]

    def set_api_endpoint(self):
        self.api_endpoint = "%s://%s.%s/api/%s" % (
            self.protocol,
            self.site,
            self.chargebee_domain,
            self.API_VERSION,
        )

    def api_url(self, url, subDomain=None):
        if subDomain is None:
            return self.api_endpoint + url
        else:
            if self.chargebee_domain is None:
                return (
                    "%s://%s.%s.chargebee.com/api/%s"
                    % (self.protocol, self.site, subDomain, self.API_VERSION)
                    + url
                )
            else:
                return (
                    "%s://%s.%s.%s/api/%s"
                    % (
                        self.protocol,
                        self.site,
                        subDomain,
                        self.chargebee_domain,
                        self.API_VERSION,
                    )
                    + url
                )

    def get_retry_config(self):
        return self.retry_config
