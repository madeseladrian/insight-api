from dataclasses import dataclass
from typing import Any

from ...domain.features import LoadAccountByToken

from ..errors import AccessDeniedError
from ..helpers import forbidden, ok, server_error
from ..params import AuthMiddlewareRequest


@dataclass
class AuthMiddleware:
    load_account_by_token: LoadAccountByToken

    def handle(self, request: AuthMiddlewareRequest) -> Any:
        try:
            if access_token := request['access_token']:
                if account := self.load_account_by_token.load(
                    access_token=access_token
                ):
                    return ok({'user_id': account['id']})
            return forbidden(AccessDeniedError())

        except Exception as e:
            return server_error(e)
