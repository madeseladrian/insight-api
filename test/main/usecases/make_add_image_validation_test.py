from src.validation.validators import (
    ValidationComposite,
    RequiredFieldValidation
)
from src.main.usecases import make_add_image_validation


class TestMakeAddGlassesValidation:
    fields: list = [
        "content_type",
        "glasses_id",
        "image"
    ]

    def test_1_should_call_ValidationComposite_with_all_validations(self):
        validations = [
            RequiredFieldValidation(field_name=field)
            for field in self.fields
        ]
        validation_composite = ValidationComposite(validations)

        assert validation_composite == make_add_image_validation()
