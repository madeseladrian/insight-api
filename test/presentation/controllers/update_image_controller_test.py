from faker import Faker
from typing import Tuple
from unittest.mock import patch

from src.presentation.controllers import UpdateImageController

from src.presentation.errors import MissingParamError
from src.presentation.helpers import (
    bad_request,
    server_error
)

from ...domain.mocks import mock_add_image_params
from ..mocks.glasses import UpdateImageSpy
from ..mocks.validation import ValidationSpy


class TestUpdateImageController:
    # SetUp
    faker = Faker()
    params = mock_add_image_params()

    SutTypes = Tuple[
        UpdateImageController,
        ValidationSpy,
        UpdateImageSpy
    ]

    def make_sut(self) -> SutTypes:
        validation_spy = ValidationSpy()
        update_image_spy = UpdateImageSpy()
        sut = UpdateImageController(
            validation=validation_spy,
            update_image=update_image_spy
        )

        return sut, validation_spy, update_image_spy

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

    def test_4_should_call_UpdateImage_with_correct_values(self):
        sut, _, update_image_spy = self.make_sut()
        sut.handle(self.params)

        assert update_image_spy.params == self.params
