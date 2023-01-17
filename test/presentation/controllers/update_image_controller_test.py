from faker import Faker
from typing import Tuple

from src.presentation.controllers import UpdateGlassesController

from ...domain.mocks import mock_add_image_params
from ..mocks.validation import ValidationSpy


class TestUpdateImageController:
    # SetUp
    faker = Faker()
    params = mock_add_image_params()

    SutTypes = Tuple[
        UpdateGlassesController,
        ValidationSpy
    ]

    def make_sut(self) -> SutTypes:
        validation_spy = ValidationSpy()
        sut = UpdateGlassesController(
            validation=validation_spy
        )

        return sut, validation_spy

    def test_1_should_call_Validation_with_correct_values(self):
        sut, validation_spy = self.make_sut()
        sut.handle(request=self.params)

        assert validation_spy.value == self.params
