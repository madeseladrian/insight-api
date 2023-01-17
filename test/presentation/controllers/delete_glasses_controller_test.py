from faker import Faker
from typing import Tuple

from src.presentation.controllers import DeleteGlassesController

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
