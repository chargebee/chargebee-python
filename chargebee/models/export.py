import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError

class Export(Model):
    class Download(Model):
      fields = ["download_url", "valid_till"]
      pass

    fields = ["operation_type", "mime_type", "status", "created_at", "id", "download"]
    def wait_for_export_completion(self):
        return wait_for_export_completion()

    def wait_for_export_completion(self, env=None, headers=None):
        import time
        count = 0
        sleep_time_millis = (10000 if env == None else env.export_sleep_millis)/1000.0

        while self.status == 'in_process':
            if count > 30:
                raise RuntimeError('Export is taking too long')
            count+=1
            time.sleep(sleep_time_millis);
            self.values = Export.retrieve(self.id, env, headers).export.values
            self.load(self.values)
        return self


    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("exports",id), None, env, headers)

    @staticmethod
    def revenue_recognition(params, env=None, headers=None):
        return request.send('post', request.uri_path("exports","revenue_recognition"), params, env, headers)

    @staticmethod
    def deferred_revenue(params, env=None, headers=None):
        return request.send('post', request.uri_path("exports","deferred_revenue"), params, env, headers)
