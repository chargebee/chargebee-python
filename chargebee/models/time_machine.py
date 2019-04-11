import json
from chargebee.model import Model
from chargebee import request
from chargebee import APIError
from chargebee import OperationFailedError
class TimeMachine(Model):

    fields = ["name", "time_travel_status", "genesis_time", "destination_time", "failure_code", \
    "failure_reason", "error_json"]
    def wait_for_time_travel_completion(self):
        return wait_for_time_travel_completion()

    def wait_for_time_travel_completion(self, env = None):
        import time
        count = 0
        sleep_time_millis = (3000 if env == None else env.time_travel_sleep_millis)/1000.0
        
        while self.time_travel_status == 'in_progress':
            if count > 30:
                raise RuntimeError('Time travel is taking too much time')
            count+=1
            time.sleep(sleep_time_millis);
            self.values = TimeMachine.retrieve(self.name, env).time_machine.values
            self.load(self.values)
        
        if self.time_travel_status == 'failed':
            err = json.loads(self.error_json)
            raise OperationFailedError(err['http_code'], err)
        
        if self.time_travel_status in ('not_enabled', '_unknown'):
            raise RuntimeError('Time travel is in wrong state \'' + self.time_travel_status + '\'')
        
        return self


    @staticmethod
    def retrieve(id, env=None, headers=None):
        return request.send('get', request.uri_path("time_machines",id), None, env, headers)

    @staticmethod
    def start_afresh(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("time_machines",id,"start_afresh"), params, env, headers)

    @staticmethod
    def travel_forward(id, params=None, env=None, headers=None):
        return request.send('post', request.uri_path("time_machines",id,"travel_forward"), params, env, headers)
