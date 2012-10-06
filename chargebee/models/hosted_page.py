from chargebee.model import Model
from chargebee import request


class HostedPage(Model):

    def content(self):
        from chargebee import Content
        return Content(self.values['content'])

    @staticmethod
    def checkout_new(**params):
        return request.send('post', '/hosted_pages/checkout_new', params)

    @staticmethod
    def checkout_existing(**params):
        return request.send('post', '/hosted_pages/checkout_existing', params)

    @staticmethod
    def update_card(**params):
        return request.send('post', '/hosted_pages/update_card', params)

    @staticmethod
    def retrieve(id, **params):
        return request.send('get', '/hosted_pages/%s' % id, params)
