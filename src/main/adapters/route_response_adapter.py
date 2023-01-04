from fastapi import HTTPException, status
from typing import Any

from ...presentation.helpers import HttpResponse


def route_response_adapter(http_response: HttpResponse) -> Any:
    status_code: int = http_response['status_code']

    match status_code:
        case 200: return http_response
        case _: raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{http_response['body']}"
        )
