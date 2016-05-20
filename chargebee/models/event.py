import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError
from chargebee.main import Environment

class Event(Model):
    class Webhook(Model):
      fields = ["id", "webhook_status"]
      pass

    fields = ["id", "occurred_at", "source", "user", "webhook_status", "webhook_failure_reason", \
    "webhooks", "event_type", "api_version"]

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
        
        api_version = webhook_data.get('api_version', None)
        env_version = Environment.API_VERSION
        if api_version != None and api_version.upper() != env_version.upper(): 
            raise Exception("API version [" + api_version.upper() + "] in response does not match "
                    + "with client library API version [" + env_version.upper() + "]")  
        return Event.construct(webhook_data)

    @staticmethod
    def list(params=None, env=None, headers=None):
        return request.send_list_request('get', request.uri_path("events"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("events",id), None, env, headers)
