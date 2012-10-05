from chargebee.model import Model
from chargebee import request, result


class Content(result.Result):
    pass


class HostedPage(Model):

    def content(self):
        return Content(self.values['content'])

    def checkout_new(self, params, env=None):
        return request.send('post', '/hosted_pages/checkout_new', params, env)

    def checkout_existing(self, params, env=None):
        return request.send('post', '/hosted_pages/checkout_existing', params, env)

    def update_card(self, params, env=None):
        return request.send('post', '/hosted_pages/update_card', params, env)

    def retrieve(self, id, env=None):
        return request.send('get', '/hosted_pages/%s' % id, {}, env)
