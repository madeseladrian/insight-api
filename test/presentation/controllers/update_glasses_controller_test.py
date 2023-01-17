from faker import Faker
from typing import Tuple
from unittest.mock import patch

from src.presentation.controllers import UpdateGlassesController
from src.presentation.errors import MissingParamError
from src.presentation.helpers import (
    bad_request,
    server_error
)

from ...domain.mocks import mock_update_glasses_params
from ..mocks.validation import ValidationSpy
from ..mocks.glasses import UpdateGlassesSpy

class TestUpdateGlassesController:
    # SetUp
    faker = Faker()
    params = mock_update_glasses_params()

    SutTypes = Tuple[
        UpdateGlassesController,
        ValidationSpy,
        UpdateGlassesSpy
    ]

    def make_sut(self) -> SutTypes:
        validation_spy = ValidationSpy()
        update_glasses_spy = UpdateGlassesSpy()
        sut = UpdateGlassesController(
            validation=validation_spy,
            update_glasses=update_glasses_spy
        )

        return sut, validation_spy, update_glasses_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, validation_spy, _ = self.make_sut()
        sut.handle(request=self.params)

        assert validation_spy.value == self.params

    def test_2_should_return_400_if_Validation_returns_an_error(self):
        sut, validation_spy, _ = self.make_sut()
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

    def test_4_should_call_UpdateGlasses_with_correct_values(self):
        sut, _, update_glasses_spy = self.make_sut()
        sut.handle(self.params)

        assert update_glasses_spy.params == self.params

    def test_5_should_return_204_if_valid_data_is_provided(self):
        sut, _, _ = self.make_sut()
        http_response = sut.handle(self.params)

        assert http_response['status_code'] == 204
        assert http_response['body'] is None

    @patch('test.presentation.mocks.glasses.UpdateGlassesSpy.update')
    def test_6_should_return_500_if_UpdateGlasses_throws(self, mocker):
        sut, _, _ = self.make_sut()
        exception = Exception()
        mocker.side_effect = exception
        http_response = sut.handle(request=self.params)

        assert http_response['status_code'] == 500
        assert http_response == server_error(error=exception)
