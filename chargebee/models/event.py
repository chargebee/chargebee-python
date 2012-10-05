import json

from chargebee.model import Model
from chargebee import request, result
from chargebee.api_error import APIError


class Content(result.Result):
    pass


class Event(Model):

    def content(self):
        return Content(self.values['content'])

    def deserialize(self, json_data):
        try:
            webhook_data = json.loads(json_data)
        except (TypeError, ValueError):
            raise APIError("Invalid webhook object to deserialize")

        return Event.construct(webhook_data)

    def list(self, params=None, env=None):
        return request.send('get', '/events', params, env)

    def retrieve(self, id, env=None):
        return request.send('get', '/events/%s' % id, env)
