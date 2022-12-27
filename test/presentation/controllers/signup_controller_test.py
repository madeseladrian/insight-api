from faker import Faker
from typing import Tuple
from unittest.mock import patch

from src.domain.params import AddAccountParams

from src.presentation.controllers import SignUpController
from src.presentation.errors import MissingParamError
from src.presentation.helpers import (
    bad_request,
    server_error
)

from ...domain.mocks import mock_add_account_params
from ..mocks.account import AddAccountSpy
from ..mocks.validation import ValidationSpy


class TestSignUpController:
    # SetUp
    faker = Faker()
    params: AddAccountParams = mock_add_account_params()

    SutTypes = Tuple[
        SignUpController,
        AddAccountSpy,
        ValidationSpy
    ]

    def make_sut(self) -> SutTypes:
        add_account_spy = AddAccountSpy()
        validation_spy = ValidationSpy()
        sut = SignUpController(
            add_account=add_account_spy,
            validation=validation_spy
        )

        return sut, add_account_spy, validation_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, _, validation_spy = self.make_sut()
        request = self.params
        sut.handle(request=request)

        assert validation_spy.value == request

    def test_2_should_return_400_if_Validation_returns_an_error(self):
        sut, _, validation_spy = self.make_sut()
        validation_spy.error = MissingParamError(self.faker.word())
        http_response = sut.handle(self.params)

        assert http_response['status_code'] == 400
        assert http_response == bad_request(validation_spy.error)

    @patch('test.presentation.mocks.validation.ValidationSpy.validate')
    def test_3_should_return_500_if_Validation_throws(self, mocker):
        sut, _, _ = self.make_sut()
        exception = Exception()
        mocker.side_effect = exception
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 500
        assert http_response == server_error(error=exception)

    def test_4_should_call_AddAccount_with_correct_values(self):
        sut, add_account_spy, _ = self.make_sut()
        request = self.params
        sut.handle(request=request)

        assert add_account_spy.params == request
