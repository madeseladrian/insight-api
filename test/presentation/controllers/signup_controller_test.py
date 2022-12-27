from faker import Faker
from typing import Tuple

from src.domain.params import AddAccountParams
from src.presentation.controllers import SignUpController

from ...domain.mocks import mock_add_account_params
from ..mocks.validation import ValidationSpy


class TestSignUpController:
    # SetUp
    faker = Faker()
    params: AddAccountParams = mock_add_account_params()

    SutTypes = Tuple[
        SignUpController,
        ValidationSpy
    ]

    def make_sut(self) -> SutTypes:
        validation_spy = ValidationSpy()
        sut = SignUpController(
          validation=validation_spy
        )

        return sut, validation_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, validation_spy = self.make_sut()
        request = self.params
        sut.handle(request=request)

        assert validation_spy.value == request
