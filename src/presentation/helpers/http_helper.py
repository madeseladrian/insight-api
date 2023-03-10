from typing import Any

from ..errors import ServerError, UnauthorizedError
from .http_response import HttpResponse


def bad_request(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=400, body=error)

def forbidden(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=403, body=error)

def ok(data: Any) -> HttpResponse:
    return HttpResponse(status_code=200, body=data)

def no_content() -> HttpResponse:
    return HttpResponse(status_code=204, body=None)

def server_error(error: Exception) -> HttpResponse:
    return HttpResponse(status_code=500, body=ServerError(error=error))

def unauthorized() -> HttpResponse:
    return HttpResponse(status_code=401, body=UnauthorizedError())
