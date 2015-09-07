import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Event(Model):
    class Webhook(Model):
      fields = ["id", "webhook_status"]
      pass

    fields = ["id", "occurred_at", "source", "user", "webhook_status", "webhook_failure_reason", \
    "webhooks", "event_type"]

    @property
    def content(self):
        from chargebee import Content
        return Content(self.values['content'])

    @staticmethod
    def deserialize(json_data):
        try:
            webhook_data = json.loads(json_data)
        except (TypeError, ValueError) as ex:
            raise Exception("The passed json_data is not JSON formatted . " + ex.message)

        return Event.construct(webhook_data)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send('get', request.uri_path("events"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("events",id), None, env, headers)
