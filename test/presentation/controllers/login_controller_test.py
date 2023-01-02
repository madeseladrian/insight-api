from faker import Faker
from typing import Tuple

from src.domain.params import AuthenticationParams

from src.presentation.contracts import Validation
from src.presentation.controllers import LoginController
from src.presentation.errors import MissingParamError
from src.presentation.helpers import bad_request

from ...domain.mocks import mock_authentication_params
from ..mocks.validation import ValidationSpy


class TestAuthenticationController:
    # SetUp
    faker = Faker()
    params: AuthenticationParams = mock_authentication_params()

    SutTypes = Tuple[LoginController, Validation]

    def make_sut(self) -> SutTypes:
        validation_spy = ValidationSpy()
        sut = LoginController(
            validation=validation_spy
        )

        return sut, validation_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, validation_spy = self.make_sut()
        request = self.params
        sut.handle(request=request)

        assert validation_spy.value == request

    def test_2_should_return_400_if_Validation_returns_an_error(self):
        sut, validation_spy = self.make_sut()
        validation_spy.error = MissingParamError(self.faker.word())
        http_response = sut.handle(self.params)

        assert http_response['status_code'] == 400
        assert http_response == bad_request(validation_spy.error)
