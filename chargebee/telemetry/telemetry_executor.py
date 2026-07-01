"""Executes Chargebee API calls with optional telemetry adapter hooks."""

from __future__ import annotations

import logging
import time
from typing import Awaitable, Callable, TypeVar
from urllib.parse import urlparse

from chargebee import environment
from chargebee.telemetry.telemetry_support import (
    BuildRequestTelemetryContextInput,
    TelemetryAdapter,
    build_request_telemetry_context,
    build_request_telemetry_result,
    extract_http_status_code,
    extract_request_telemetry_error,
    resolve_chargebee_api_version,
)
from chargebee.version import VERSION

logger = logging.getLogger(__name__)

HttpResult = tuple[object, object, int]
SyncHttpAction = Callable[[dict[str, str] | None], HttpResult]
AsyncHttpAction = Callable[[dict[str, str] | None], Awaitable[HttpResult]]
T = TypeVar("T")


def resolve_adapter(
    env: environment.Environment, adapter_override: TelemetryAdapter | None = None
) -> TelemetryAdapter | None:
    if adapter_override is not None:
        return adapter_override
    return getattr(env, "telemetry_adapter", None)


def build_context(
    env: environment.Environment,
    resource: str,
    operation: str,
    method: str,
    url: str,
    subDomain: str | None,
    request_headers: dict[str, str] | None = None,
) -> BuildRequestTelemetryContextInput:
    full_url = env.api_url(url, subDomain)
    parsed = urlparse(full_url)
    http_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    server_address = parsed.hostname or parsed.netloc.split(":")[0]
    api_path = f"/api/{env.API_VERSION}"
    return BuildRequestTelemetryContextInput(
        resource=resource,
        operation=operation,
        http_method=method.upper(),
        http_url=http_url,
        server_address=server_address,
        chargebee_site=env.site,
        chargebee_api_version=resolve_chargebee_api_version(api_path),  # type: ignore[arg-type]
        sdk_version=VERSION,
        request_headers=request_headers,
    )


def _start_telemetry(
    env: environment.Environment,
    adapter: TelemetryAdapter,
    resource: str,
    operation: str,
    method: str,
    url: str,
    subDomain: str | None,
    headers: dict[str, str] | None,
) -> tuple[object | None, dict[str, str]]:
    telemetry_headers = dict(headers or {})
    try:
        context = build_request_telemetry_context(
            build_context(env, resource, operation, method, url, subDomain, headers)
        )
        handle = adapter.on_request_start(context, telemetry_headers)
        return handle, telemetry_headers
    except Exception as err:
        logger.exception(
            "Telemetry adapter on_request_start failed: %s. Continuing without telemetry.",
            err,
        )
        return None, dict(headers or {})


def _end_success(
    adapter: TelemetryAdapter,
    handle: object | None,
    start_ms: float,
    http_status_code: int,
) -> None:
    try:
        adapter.on_request_end(
            handle,
            build_request_telemetry_result(
                http_status_code, int(time.time() * 1000 - start_ms), None
            ),
        )
    except Exception as err:
        logger.exception("Telemetry adapter on_request_end failed: %s", err)


def _end_failure(
    adapter: TelemetryAdapter,
    handle: object | None,
    start_ms: float,
    err: BaseException,
) -> None:
    status = extract_http_status_code(err)
    http_status_code = status if status is not None else 500
    try:
        adapter.on_request_end(
            handle,
            build_request_telemetry_result(
                http_status_code,
                int(time.time() * 1000 - start_ms),
                extract_request_telemetry_error(err),
            ),
        )
    except Exception as telemetry_err:
        logger.exception("Telemetry adapter on_request_end failed: %s", telemetry_err)


def execute_sync(
    env: environment.Environment,
    resource: str | None,
    operation: str | None,
    method: str,
    url: str,
    subDomain: str | None,
    headers: dict[str, str] | None,
    action: SyncHttpAction,
    adapter_override: TelemetryAdapter | None = None,
) -> HttpResult:
    adapter = resolve_adapter(env, adapter_override)
    if adapter is None or not resource or not operation:
        return action(headers)

    start_ms = time.time() * 1000
    handle, telemetry_headers = _start_telemetry(
        env, adapter, resource, operation, method, url, subDomain, headers
    )

    try:
        result = action(telemetry_headers)
        _end_success(adapter, handle, start_ms, result[2])
        return result
    except Exception as err:
        _end_failure(adapter, handle, start_ms, err)
        raise


async def execute_async(
    env: environment.Environment,
    resource: str | None,
    operation: str | None,
    method: str,
    url: str,
    subDomain: str | None,
    headers: dict[str, str] | None,
    action: AsyncHttpAction,
    adapter_override: TelemetryAdapter | None = None,
) -> HttpResult:
    adapter = resolve_adapter(env, adapter_override)
    if adapter is None or not resource or not operation:
        return await action(headers)

    start_ms = time.time() * 1000
    handle, telemetry_headers = _start_telemetry(
        env, adapter, resource, operation, method, url, subDomain, headers
    )

    try:
        result = await action(telemetry_headers)
        _end_success(adapter, handle, start_ms, result[2])
        return result
    except Exception as err:
        _end_failure(adapter, handle, start_ms, err)
        raise
