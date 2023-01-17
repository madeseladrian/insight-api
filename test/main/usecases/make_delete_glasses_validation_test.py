from src.validation.validators import (
    ValidationComposite,
    RequiredFieldValidation
)
from src.main.usecases import make_delete_glasses_validation


class TestMakeDeleteGlassesValidation:
    fields: list = ['glasses_id']

    def test_1_should_call_ValidationComposite_with_all_validations(self):
        validations = [
            RequiredFieldValidation(field_name=field)
            for field in self.fields
        ]
        validation_composite = ValidationComposite(validations)

        assert validation_composite == make_delete_glasses_validation()
