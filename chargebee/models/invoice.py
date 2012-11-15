import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Invoice(Model):
    class LineItem(Model):
      pass
    class Discount(Model):
      pass


    @staticmethod
    def list(params=None, env=None):
        return request.send('get', '/invoices', params, env)

    @staticmethod
    def retrieve(id, env=None):
        return request.send('get', '/invoices/%s' % id, None, env)

    @staticmethod
    def invoices_for_subscription(id, params=None, env=None):
        return request.send('get', '/subscriptions/%s/invoices' % id, params, env)

    @staticmethod
    def charge(params, env=None):
        return request.send('post', '/invoices/charge', params, env)

    @staticmethod
    def charge_addon(params, env=None):
        return request.send('post', '/invoices/charge_addon', params, env)
