import json
import urllib

from chargebee import compat, environment, util, http_request
from chargebee.responses import Response
from chargebee.telemetry.telemetry_executor import execute_async, execute_sync


def lowercase_keys(data):
    if isinstance(data, dict):
        return {
            (k if k.startswith("cf_") else k.lower()): lowercase_keys(v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [lowercase_keys(item) for item in data]
    else:
        return data


def send_list_request(
    method,
    url,
    env: environment.Environment = None,
    params=None,
    headers=None,
    response_type=None,
    subDomain=None,
    isJsonRequest=False,
    jsonKeys=None,
    options=None,
    resource=None,
    operation=None,
    telemetry_adapter=None,
):
    serialized = {}

    if params is None:
        params = {}

    for k, v in list(params.items()):
        if isinstance(v, list):
            v = json.dumps(v)
        serialized.update({k: v})
    return send(
        method,
        url,
        env,
        serialized,
        headers,
        response_type,
        subDomain,
        isJsonRequest,
        jsonKeys,
        options,
        resource=resource,
        operation=operation,
        telemetry_adapter=telemetry_adapter,
    )


def send(
    method,
    url,
    env: environment.Environment,
    params=None,
    headers=None,
    response_type=None,
    subDomain=None,
    isJsonRequest=False,
    jsonKeys=None,
    options=None,
    resource=None,
    operation=None,
    telemetry_adapter=None,
):
    params = lowercase_keys(params)

    if params is None:
        params = {}

    ser_params = (
        params if isJsonRequest else util.serialize(params, None, None, jsonKeys)
    )

    request_args = {
        "method": method,
        "url": url,
        "env": env,
        "params": ser_params,
        "headers": headers,
        "subDomain": subDomain,
        "isJsonRequest": isJsonRequest,
        "options": options,
        "use_async_client": env.use_async_client,
    }

    def run_http(request_headers):
        args = {**request_args, "headers": request_headers}
        return http_request.request(**args)

    async def run_http_async(request_headers):
        args = {**request_args, "headers": request_headers}
        return await http_request.request(**args)

    if env.use_async_client:

        async def async_request():
            response, response_headers, http_code = await execute_async(
                env,
                resource,
                operation,
                method,
                url,
                subDomain,
                headers,
                run_http_async,
                telemetry_adapter,
            )
            return Response(
                response_type, response, response_headers, http_code
            ).parse()

        return async_request()
    else:
        response, response_headers, http_code = execute_sync(
            env,
            resource,
            operation,
            method,
            url,
            subDomain,
            headers,
            run_http,
            telemetry_adapter,
        )
        return Response(response_type, response, response_headers, http_code).parse()


def uri_path(*paths):
    url = ""
    for path in paths:
        if path is None or len(str(path).strip()) < 1:
            raise Exception("Id is None or empty")
        if compat.py_major_v >= 3:
            url = url + "/" + urllib.parse.quote(str(path).strip())
        else:
            url = url + "/" + urllib.quote(str(util.get_val(path)))
    return url
