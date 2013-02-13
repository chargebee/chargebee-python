import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Estimate(Model):
    class LineItem(Model):
      pass
    class Discount(Model):
      pass
    class Tax(Model):
      pass


    @staticmethod
    def create_subscription(params, env=None):
        return request.send('post', '/estimates/create_subscription', params, env)

    @staticmethod
    def update_subscription(params, env=None):
        return request.send('post', '/estimates/update_subscription', params, env)
