import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class PaymentScheduleScheme(Model):
    class PreferredSchedule(Model):
      fields = ["period", "amount_percentage"]
      pass

    fields = ["id", "name", "description", "number_of_schedules", "period_unit", "period", \
    "created_at", "resource_version", "updated_at", "preferred_schedules"]


    @staticmethod
    def create(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_schedule_schemes"), params, env, headers, None, False,json_keys)

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("payment_schedule_schemes",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def delete(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("payment_schedule_schemes",id,"delete"), None, env, headers, None, False,json_keys)
