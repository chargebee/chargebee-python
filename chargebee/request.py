import urllib
from chargebee import util, http_request
from chargebee.main import ChargeBee
from chargebee import compat
import json

def send_list_request(method, url, params=None, env=None, headers=None):
    serialized = {}
    for k, v in list(params.items()):
        if isinstance(v, (list)):
            v = json.dumps(v)
        serialized.update({k:v})
    return send(method,url,serialized,env,headers)

def send(method, url, params=None, env=None, headers=None):
    if params is None:
        params = {}

    env = env or ChargeBee.default_env

    ser_params = util.serialize(params)

    response = http_request.request(method, url, env, ser_params, headers)

    from chargebee.result import Result
    from chargebee.list_result import ListResult
    if 'list' in response:
        return ListResult(response['list'], response.get('next_offset', None))
    return Result(response)

def uri_path(*paths):
    url = ""
    for path in paths:
        if path == None or len(str(path).strip()) < 1 :
            raise Exception("Id is None or empty")
        if compat.py_major_v >= 3:          
            url = url + "/" +  urllib.parse.quote(str(path).strip()) 
        else:
            url =  url + "/" + urllib.quote(str(util.get_val(path)))
    return url    
       
