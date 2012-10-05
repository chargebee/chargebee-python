from chargebee.models.subscription import Subscription


class Result(object):

    def __init__(self, response):
        self._response = response
        self._response_obj = {}

    def subscription(self):
        return self._get('subscription', Subscription, {'addons': SubscriptionAddon})

    def _get(self, type, cls, sub_types=None):
        if not type in self._response:
            return None

        if not type in self._response_obj:
            self._response_obj[type] = cls(self._response[type], sub_types)

        return self._response_obj[type]
