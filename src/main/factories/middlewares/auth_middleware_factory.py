from ....presentation.contracts import Middleware
from ....presentation.middlewares import AuthMiddleware

from ...usecases import make_db_load_account_by_token


def auth_middleware_factory() -> Middleware:
    return AuthMiddleware(
        load_account_by_token=make_db_load_account_by_token(),
    )
