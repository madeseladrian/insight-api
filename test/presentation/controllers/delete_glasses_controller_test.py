from faker import Faker
from typing import Tuple

from src.presentation.controllers import DeleteGlassesController
from src.presentation.errors import MissingParamError
from src.presentation.helpers import (
    bad_request
)

from ...domain.mocks import mock_add_glasses_params
from ..mocks.validation import ValidationSpy


class TestAddGlassesController:
    # SetUp
    faker = Faker()
    params = mock_add_glasses_params()

    SutTypes = Tuple[
        DeleteGlassesController,
        ValidationSpy
    ]

    def make_sut(self) -> SutTypes:
        validation_spy = ValidationSpy()
        sut = DeleteGlassesController(
            validation=validation_spy
        )

        return sut, validation_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, validation_spy = self.make_sut()
        sut.handle(request=self.params)

        assert validation_spy.value == self.params

    def test_2_should_return_400_if_Validation_returns_an_error(self):
        sut, validation_spy = self.make_sut()
        validation_spy.error = MissingParamError(param_name=self.faker.word())
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 400
        assert http_response == bad_request(validation_spy.error)
