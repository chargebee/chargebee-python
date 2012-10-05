from chargebee.model import Model
from chargebee import request


class LineItem(Model):
    pass


class Discount(Model):
    pass


class Invoice(Model):

    def list(self, params=None, env=None):
        return request.send('get', '/invoices', params, env)
    
    def retrieve(self, id, env=None):
        return request.send('get', '/invoices/%s' % id, {}, env)

    def invoices_for_subscription(self, id, params=None, env=None):
        return request.send('get', '/subscriptions/%s/invoices' % id, params, env)

    def charge(self, params, env=None):
        return request.send('post', '/invoices/charge', params, env)

    def charge_addon(self, params, env=None):
        return request.send('post', '/invoices/charge_addon', params, env)
