from faker import Faker

from src.presentation.errors import InvalidParamError
from src.validation.validators import UpdateFieldValidation


class TestUpdateFieldValidation:
    # SetUp
    faker = Faker()
    field = faker.word()
    value = faker.word()
    list_of_fields_to_compare = ['any_field', 'other_field']

    def make_sut(self) -> UpdateFieldValidation:
        return UpdateFieldValidation(
            list_of_fields_to_compare=self.list_of_fields_to_compare
        )

    def test_1_should_return_an_InvalidParamError_if_validation_fails(self):
        sut = self.make_sut()
        error = sut.validate({'data': {self.field: self.value}})

        assert error == InvalidParamError(self.field)

    def test_2_should_return_None_if_validation_succeds(self):
        sut = self.make_sut()
        error = sut.validate({'data': {
            'any_field': 'any_value',
            'other_field': 'other_value'
        }})

        assert error is None
