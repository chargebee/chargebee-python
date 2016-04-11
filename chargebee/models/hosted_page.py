import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class HostedPage(Model):

    fields = ["id", "type", "url", "state", "failure_reason", "pass_thru_content", "embed", \
    "created_at", "expires_at"]

    @property
    def content(self):
        from chargebee import Content
        if 'content' in self.values:
            return Content(self.values['content'])
        return None

    @staticmethod
    def checkout_new(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","checkout_new"), params, env, headers)

    @staticmethod
    def checkout_existing(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","checkout_existing"), params, env, headers)

    @staticmethod
    def update_card(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","update_card"), params, env, headers)

    @staticmethod
    def update_payment_method(params, env=None, headers=None):
        return request.send('post', request.uri_path("hosted_pages","update_payment_method"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("hosted_pages",id), None, env, headers)
