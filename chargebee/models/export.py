import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Export(Model):
    class Download(Model):
      fields = ["download_url", "valid_till", "mime_type"]
      pass

    fields = ["id", "operation_type", "mime_type", "status", "created_at", "download"]

    def wait_for_export_completion(self):
        return wait_for_export_completion()

    def wait_for_export_completion(self, env=None, headers=None):
        import time
        count = 0
        sleep_time_millis = (10000 if env == None else env.export_sleep_millis)/1000.0

        while self.status == 'in_process':
            if count > 50:
                raise RuntimeError('Export is taking too long')
            count+=1
            time.sleep(sleep_time_millis);
            self.values = Export.retrieve(self.id, env, headers).export.values
            self.load(self.values)
        return self

    @staticmethod
    def retrieve(id, env=None, headers=None):
        json_keys = { 
        }
        return request.send('get', request.uri_path("exports",id), None, env, headers, None, False,json_keys)

    @staticmethod
    def revenue_recognition(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","revenue_recognition"), params, env, headers, None, False,json_keys)

    @staticmethod
    def deferred_revenue(params, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","deferred_revenue"), params, env, headers, None, False,json_keys)

    @staticmethod
    def plans(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","plans"), params, env, headers, None, False,json_keys)

    @staticmethod
    def addons(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","addons"), params, env, headers, None, False,json_keys)

    @staticmethod
    def coupons(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","coupons"), params, env, headers, None, False,json_keys)

    @staticmethod
    def customers(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","customers"), params, env, headers, None, False,json_keys)

    @staticmethod
    def subscriptions(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","subscriptions"), params, env, headers, None, False,json_keys)

    @staticmethod
    def invoices(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","invoices"), params, env, headers, None, False,json_keys)

    @staticmethod
    def credit_notes(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","credit_notes"), params, env, headers, None, False,json_keys)

    @staticmethod
    def transactions(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","transactions"), params, env, headers, None, False,json_keys)

    @staticmethod
    def orders(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","orders"), params, env, headers, None, False,json_keys)

    @staticmethod
    def item_families(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","item_families"), params, env, headers, None, False,json_keys)

    @staticmethod
    def items(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def item_prices(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","item_prices"), params, env, headers, None, False,json_keys)

    @staticmethod
    def attached_items(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","attached_items"), params, env, headers, None, False,json_keys)

    @staticmethod
    def differential_prices(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","differential_prices"), params, env, headers, None, False,json_keys)

    @staticmethod
    def price_variants(params=None, env=None, headers=None):
        json_keys = { 
        }
        return request.send('post', request.uri_path("exports","price_variants"), params, env, headers, None, False,json_keys)
