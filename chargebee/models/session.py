import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Session(Model):

    fields = ["id", "created_at", "expires_at"]

    @property
    def content(self):
        from chargebee import Content
        if 'content' in self.values:
            return Content(self.values['content'])
        return None

    @staticmethod
    def create(params=None, env=None, headers=None):
        return request.send('post', request.uri_path("sessions"), params, env, headers)

    @staticmethod
    def retrieve(id, params=None, env=None, headers=None):
        return request.send('get', request.uri_path("sessions",id), params, env, headers)
