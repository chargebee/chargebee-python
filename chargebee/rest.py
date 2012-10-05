import chargebee

class Rest(object):

    def request(self, method, url, env, params=None):
        if not env:
            raise chargebee.APIError('No environment configured.')
