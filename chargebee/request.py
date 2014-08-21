import urllib
from chargebee import util, http
from chargebee.main import ChargeBee

def send(method, url, params=None, env=None):
    if params is None:
        params = {}

    env = env or ChargeBee.default_env

    ser_params = util.serialize(params)

    response = http.request(method, url, env, ser_params)

    from chargebee.result import Result
    from chargebee.list_result import ListResult
    if 'list' in response:
        return ListResult(response['list'], response.get('next_offset', None))
    return Result(response)

def uri_path(*paths):
    return "/" + "/".join(map(lambda path : urllib.quote(str(path)), paths))
        
