from dataclasses import dataclass

from ...domain.features import LoadAccountByToken

from ..contracts import Middleware
from ..errors import AccessDeniedError
from ..helpers import forbidden, HttpResponse, ok, server_error
from ..params import AuthMiddlewareRequest


@dataclass
class AuthMiddleware(Middleware):
    load_account_by_token: LoadAccountByToken

    def handle(self, request: AuthMiddlewareRequest) -> HttpResponse:
        try:
            if access_token := request['access_token']:
                if account := self.load_account_by_token.load(
                    access_token=access_token
                ):
                    return ok({'user_id': account['id']})
            return forbidden(AccessDeniedError())

        except Exception as e:
            return server_error(e)
