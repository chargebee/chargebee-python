import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class InstallmentConfig(Model):
    class Installment(Model):
      fields = ["period", "amount_percentage"]
      pass

    fields = ["id", "description", "number_of_installments", "period_unit", "period", "preferred_day", \
    "created_at", "resource_version", "updated_at", "installments"]


    @staticmethod
    def create(params, env=None, headers=None):
        return request.send('post', request.uri_path("installment_configs"), params, env, headers)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("installment_configs",id), None, env, headers)

    @staticmethod
    def delete(id, env=None, headers=None):
        return request.send('post', request.uri_path("installment_configs",id,"delete"), None, env, headers)
