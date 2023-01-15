from typing import Tuple

from src.presentation.errors import AccessDeniedError
from src.presentation.helpers import forbidden
from src.presentation.middlewares import AuthMiddleware
from src.presentation.params import AuthMiddlewareRequest

from ..mocks.account import LoadAccountByTokenSpy
from ...domain.mocks import mock_auth_middleware_params


class TestAuthMiddleware:
    params: AuthMiddlewareRequest = mock_auth_middleware_params()

    SutTypes = Tuple[
        AuthMiddleware,
        LoadAccountByTokenSpy
    ]

    def make_sut(self) -> SutTypes:
        load_account_by_token_spy = LoadAccountByTokenSpy()
        sut = AuthMiddleware(
            load_account_by_token=load_account_by_token_spy,
        )
        return sut, load_account_by_token_spy

    def test_1_should_call_LoadAccountByToken_with_correct_access_token(self):
        sut, load_account_by_token_spy = self.make_sut()
        sut.handle(self.params)

        assert load_account_by_token_spy.access_token == self.params['access_token']

    def test_2_should_return_403_if_no_access_token_exists_in_headers(self):
        sut, _ = self.make_sut()
        http_response = sut.handle({'access_token': None})

        assert http_response == forbidden(AccessDeniedError())
