from faker import Faker
from typing import Tuple
from unittest.mock import patch

from src.presentation.controllers import AddGlassesController
from src.presentation.errors import MissingParamError
from src.presentation.helpers import (
    bad_request,
    server_error
)

from ...domain.mocks import mock_add_glasses_params
from ..mocks.glasses import AddGlassesSpy
from ..mocks.validation import ValidationSpy


class TestAddSurveyController:
    # SetUp
    faker = Faker()
    params = mock_add_glasses_params()

    SutTypes = Tuple[
        AddGlassesController,
        AddGlassesSpy,
        ValidationSpy
    ]

    def make_sut(self) -> SutTypes:
        add_glasses_spy = AddGlassesSpy()
        validation_spy = ValidationSpy()
        sut = AddGlassesController(
            add_glasses=add_glasses_spy,
            validation=validation_spy
        )

        return sut, add_glasses_spy, validation_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, _, validation_spy = self.make_sut()
        sut.handle(request=self.params)

        assert validation_spy.value == self.params

    def test_2_should_return_400_if_Validation_returns_an_error(self):
        sut, _, validation_spy = self.make_sut()
        validation_spy.error = MissingParamError(param_name=self.faker.word())
        http_response = sut.handle(request=self.params)

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

    def test_4_should_call_AddGlasses_with_correct_values(self):
        sut, add_glasses_spy, _ = self.make_sut()
        sut.handle(self.params)

        assert add_glasses_spy.params == self.params

    def test_5_should_return_204_if_valid_data_is_provided(self):
        sut, _, _ = self.make_sut()
        http_response = sut.handle(self.params)

        assert http_response['status_code'] == 204
        assert http_response['body'] is None
