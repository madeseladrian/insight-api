from dataclasses import dataclass
from typing import Any

from ...domain.features import LoadAccountByToken

from ..errors import AccessDeniedError
from ..helpers import forbidden
from ..params import AuthMiddlewareRequest


@dataclass
class AuthMiddleware:
    load_account_by_token: LoadAccountByToken

    def handle(self, request: AuthMiddlewareRequest) -> Any:
        if access_token := request['access_token']:
            self.load_account_by_token.load(
                access_token=access_token
            )
        return forbidden(AccessDeniedError())
