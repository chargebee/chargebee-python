class RetryConfig:
    def __init__(self, enabled=False, max_retries=3, delay_ms=200, retry_on=None):
        self.enabled = enabled
        self.max_retries = max_retries
        self.delay_ms = delay_ms
        self.retry_on = retry_on or [500, 502, 503, 504]

    def is_enabled(self):
        return self.enabled

    def get_max_retries(self):
        return self.max_retries

    def get_delay_ms(self):
        return self.delay_ms

    def get_retry_on(self):
        return self.retry_on

    def get_enable_debug_logs(self):
        return self.enable_debug_logs
