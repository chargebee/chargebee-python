import base64
import datetime
import logging
import platform
import random
import re
import time
import ssl

import httpx

from chargebee import (
    APIError,
    PaymentError,
    InvalidRequestError,
    OperationFailedError,
    UbbBatchIngestionInvalidRequestError,
)
from chargebee import compat, util, environment
from chargebee.main import Chargebee
from chargebee.version import VERSION

_logger = logging.getLogger(__name__)


def _basic_auth_str(username):
    return "Basic " + base64.b64encode(
        ("%s:" % username).encode("latin1")
    ).strip().decode("latin1")


def request(
    method,
    url,
    env: environment.Environment,
    params=None,
    headers=None,
    subDomain=None,
    isJsonRequest=False,
    options={},
    use_async_client=False,
):
    if not env:
        raise Exception("No environment configured.")

    headers = headers or {}
    request_args = {"method": method.upper()}

    retry_config = env.get_retry_config() if hasattr(env, "get_retry_config") else None
    url = env.api_url(url, subDomain)

    match method.lower(), isJsonRequest:
        case "get" | "head" | "delete", _:
            request_args["params"] = params
        case _, True:
            headers["Content-Type"] = "application/json;charset=UTF-8"
            request_args["json"] = params
        case _, False:
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            request_args["data"] = params

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
        and options.get("isIdempotent")
    ):
        headers[Chargebee.idempotency_header] = util.generate_uuid_v4()

    meta = compat.urlparse(url)
    scheme = "https" if Chargebee.verify_ca_certs or env.protocol == "https" else "http"
    full_url = f"{scheme}://{meta.netloc + meta.path + '?' + meta.query}"

    timeout = httpx.Timeout(
        None,
        connect=env.connect_timeout,
        read=env.read_timeout,
    )

    request_args = {
        **request_args,
        "timeout": timeout,
        "headers": headers,
        "url": full_url,
    }

    if Chargebee.verify_ca_certs:
        ctx = ssl.create_default_context(cafile=Chargebee.ca_cert_path)
        request_args["verify"] = ctx

    if use_async_client:
        return _process_response_async(
            full_url, request_args, retry_config, env.enable_debug_logs
        )
    else:
        return _process_response(
            full_url, request_args, retry_config, env.enable_debug_logs
        )


def _process_response(url, request_args, retry_config, enable_debug_logs):
    retry_count = 0

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
            if payload := request_args.get("json", request_args.get("data")):
                _logger.debug("PAYLOAD: {0}".format(payload))

            if retry_count > 0:
                headers = request_args.get("headers", {})
                headers["X-CB-Retry-Attempt"] = str(retry_count)
                request_args["headers"] = headers

            return _make_request(request_args)

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
                sleep(delay_ms)
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
            sleep(delay_ms)
            retry_count += 1


async def _process_response_async(url, request_args, retry_config, enable_debug_logs):
    retry_count = 0

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
            if payload := request_args.get("json", request_args.get("data")):
                _logger.debug("PAYLOAD: {0}".format(payload))

            if retry_count > 0:
                headers = request_args.get("headers", {})
                headers["X-CB-Retry-Attempt"] = str(retry_count)
                request_args["headers"] = headers

            return await _make_request_async(request_args)

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


def _handle_response(request_args: dict, response: httpx.Response):
    _logger.debug(
        f"{request_args['method']} Response: {response.status_code} - {response.text}"
    )

    try:
        resp_json = compat.json.loads(response.text)
    except Exception:
        raise map_plaintext_to_error(response)

    if response.status_code < 200 or response.status_code > 299:
        handle_api_resp_error(
            request_args["url"], response.status_code, resp_json, response.headers
        )

    return resp_json, response.headers, response.status_code


def _make_request(request_args):
    """Make a synchronous HTTP request using httpx"""
    verify = request_args.pop("verify", True)
    with httpx.Client(verify=verify) as client:
        response = client.request(**request_args)
        return _handle_response(request_args, response)


async def _make_request_async(request_args):
    """Make an asynchronous HTTP request using httpx"""
    verify = request_args.pop("verify", True)
    async with httpx.AsyncClient(verify=verify) as client:
        response = await client.request(**request_args)
        return _handle_response(request_args, response)


def map_plaintext_to_error(response):
    text = response.text
    if "503" in text:
        return Exception(
            "Sorry, the server is currently unable to handle the request due to a temporary overload or scheduled maintenance. "
            "Please retry after sometime. \n type: internal_temporary_error, \n http_status_code: 503, \n error_code: internal_temporary_error,\n content:"
            + text
        )
    elif "504" in text:
        return Exception(
            "The server did not receive a timely response from an upstream server, request aborted. If this problem persists, "
            "contact us at support@chargebee.com. \n type: gateway_timeout, \n http_status_code: 504, \n error_code: gateway_timeout,\n content:"
            + text
        )
    return Exception(
        "Sorry, something went wrong when trying to process the request. If this problem persists, contact us at support@chargebee.com. "
        "\n type: internal_error, \n http_status_code: 500, \n error_code: internal_error,\n content:"
        + text
    )


def extract_status_code(err):
    try:
        # Structured errors
        return getattr(
            err,
            "http_code",
            getattr(err.json_obj, "status_code", int(getattr(err, "code", 0))),
        )
    except Exception:
        pass

    # Fallback: Try extracting from string
    try:
        message = str(err)
        match = re.search(r"http_status_code:\s*(\d{3})", message)
        if match:
            return int(match.group(1))
    except Exception:
        pass

    return 0


def parse_retry_after(err):
    headers = getattr(err, "response_headers", {}) or {}
    retry_after = headers.get("retry-after") or headers.get("Retry-After")
    if not retry_after:
        return None
    try:
        return int(retry_after) * 1000
    except ValueError:
        try:
            from email.utils import parsedate_to_datetime

            retry_time = parsedate_to_datetime(retry_after)
            return max(
                0, int((retry_time - datetime.datetime.utcnow()).total_seconds() * 1000)
            )
        except Exception:
            return None


def calculate_backoff_delay(retry_count, base_delay_ms):
    jitter = random.randint(0, 100)
    return base_delay_ms * (2**retry_count) + jitter


def should_retry(status_code, retry_count, retry_config):
    return (
        status_code in retry_config.get_retry_on()
        and retry_count < retry_config.get_max_retries()
    )


def sleep(milliseconds):
    time.sleep(milliseconds / 1000.0)


async def sleep_async(milliseconds):
    await compat.event_loop.sleep(milliseconds / 1000.0)


def log(message, level="INFO", enable_debug_logs=False):
    if enable_debug_logs:
        print(f"[{level}] {message}")


def handle_api_resp_error(url, http_code, resp_json, response_headers=None):
    if "api_error_code" not in resp_json:
        raise Exception(
            "The api_error_code is not present. Probably not a chargebee error. \n URL is "
            + url
            + "\nContent is \n "
            + str(resp_json)
        )

    if "payment" == resp_json.get("type"):
        raise PaymentError(http_code, resp_json, response_headers)
    elif "operation_failed" == resp_json.get("type"):
        raise OperationFailedError(http_code, resp_json, response_headers)
    elif "invalid_request" == resp_json.get("type"):
        raise InvalidRequestError(http_code, resp_json, response_headers)
    elif "ubb_batch_ingestion_invalid_request" == resp_json.get("type"):
        raise UbbBatchIngestionInvalidRequestError(
            http_code, resp_json, response_headers
        )
    else:
        raise APIError(http_code, resp_json, response_headers)
