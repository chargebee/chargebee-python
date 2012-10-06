from chargebee.model import Model
from chargebee import request


class Invoice(Model):

    class LineItem(Model):
        pass

    class Discount(Model):
        pass

    @staticmethod
    def list(**params):
        return request.send('get', '/invoices', params)

    @staticmethod
    def retrieve(id, **params):
        return request.send('get', '/invoices/%s' % id, params)

    @staticmethod
    def invoices_for_subscription(id, **params):
        return request.send('get', '/subscriptions/%s/invoices' % id, params)

    @staticmethod
    def charge(**params):
        return request.send('post', '/invoices/charge', params)

    @staticmethod
    def charge_addon(**params):
        return request.send('post', '/invoices/charge_addon', params)
