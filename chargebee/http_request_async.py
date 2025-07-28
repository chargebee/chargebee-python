import logging
import platform
import asyncio

import httpx

from chargebee import compat, util, http_request
from chargebee.main import Chargebee
from chargebee.version import VERSION

_logger = logging.getLogger(__name__)

# Reuse from http_request module
_basic_auth_str = http_request._basic_auth_str


async def request_async(
    method,
    url,
    env,
    params=None,
    headers=None,
    subDomain=None,
    isJsonRequest=False,
    options=None,
):
    if not env:
        raise Exception("No environment configured.")
    if headers is None:
        headers = {}

    retry_config = env.get_retry_config() if hasattr(env, "get_retry_config") else None
    url = env.api_url(url, subDomain)

    if method.lower() in ("get", "head", "delete"):
        url = "%s?%s" % (url, compat.urlencode(params))
        payload = None
    else:
        if isJsonRequest:
            payload = params
            headers["Content-type"] = "application/json;charset=UTF-8"
        else:
            payload = compat.urlencode(params)
            headers["Content-type"] = "application/x-www-form-urlencoded"

    headers.update(
        {
            "User-Agent": f"Chargebee-Python-Client v{VERSION}",
            "Accept": "application/json",
            "Authorization": _basic_auth_str(env.api_key),
            "Lang-Version": f"{compat.py_major_v}.{compat.py_minor_v}",
            "OS-Version": platform.platform(),
        }
    )

    idempotency_key = headers.get(Chargebee.idempotency_header)
    if (
        idempotency_key is None
        and retry_config.is_enabled()
        and method.lower() == "post"
        and options["isIdempotent"]
    ):
        headers[Chargebee.idempotency_header] = util.generate_uuid_v4()

    meta = compat.urlparse(url)
    scheme = "https" if Chargebee.verify_ca_certs or env.protocol == "https" else "http"
    full_url = f"{scheme}://{meta.netloc + meta.path + '?' + meta.query}"

    request_args = {
        "method": method.upper(),
        "timeout": httpx.Timeout(
            connect=env.connect_timeout,
            read=env.read_timeout,
            write=None,
            pool=None
        ),
        "content": payload,
        "headers": headers,
        "url": full_url,
    }
    if Chargebee.verify_ca_certs:
        request_args["verify"] = Chargebee.ca_cert_path

    return await process_response_async(full_url, request_args, retry_config, env.enable_debug_logs)


async def process_response_async(url, request_args, retry_config, enable_debug_logs):
    retry_count = 0

    async with httpx.AsyncClient() as client:
        while True:
            try:
                _logger.debug(f"{request_args['method']} Request: {url}")
                _logger.debug(
                    "HEADERS: {0}".format(
                        {
                            k: v
                            for k, v in request_args["headers"].items()
                            if k.lower() != "authorization"
                        }
                    )
                )
                if request_args["content"]:
                    _logger.debug("PAYLOAD: {0}".format(request_args["content"]))

                if retry_count > 0:
                    headers = request_args.get("headers", {})
                    headers["X-CB-Retry-Attempt"] = str(retry_count)
                    request_args["headers"] = headers

                response = await client.request(**request_args)
                _logger.debug(
                    f"{request_args['method']} Response: {response.status_code} - {response.text}"
                )

                try:
                    resp_json = compat.json.loads(response.text)
                except Exception:
                    raise map_plaintext_to_error(response)

                if response.status_code < 200 or response.status_code > 299:
                    handle_api_resp_error(
                        url, response.status_code, resp_json, response.headers
                    )

                return resp_json, response.headers, response.status_code

            except Exception as err:
                status_code = extract_status_code(err)

                if not retry_config or not retry_config.is_enabled():
                    raise err

                if status_code == 429:
                    delay_ms = parse_retry_after(err) or retry_config.get_delay_ms()
                    log(
                        f"Rate limit hit. Retrying in {delay_ms}ms",
                        "INFO",
                        enable_debug_logs,
                    )
                    await sleep_async(delay_ms)
                    retry_count += 1
                    continue

                if not should_retry(status_code, retry_count, retry_config):
                    log(
                        f"Request failed after {retry_count} retries: {str(err)}",
                        "ERROR",
                        enable_debug_logs,
                    )
                    raise err

                delay_ms = calculate_backoff_delay(retry_count, retry_config.get_delay_ms())
                log(
                    f"Retrying [{retry_count + 1}/{retry_config.get_max_retries()}] in {delay_ms}ms due to status {status_code}",
                    "INFO",
                    enable_debug_logs,
                )
                await sleep_async(delay_ms)
                retry_count += 1


# Reuse common functions from http_request module
map_plaintext_to_error = http_request.map_plaintext_to_error
extract_status_code = http_request.extract_status_code
parse_retry_after = http_request.parse_retry_after
calculate_backoff_delay = http_request.calculate_backoff_delay
should_retry = http_request.should_retry


async def sleep_async(milliseconds):
    await asyncio.sleep(milliseconds / 1000.0)


# Reuse from http_request module
log = http_request.log
handle_api_resp_error = http_request.handle_api_resp_error