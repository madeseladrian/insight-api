from src.validation.validators import (
    ValidationComposite,
    RequiredFieldValidation
)
from src.main.usecases import make_add_glasses_validation


class TestMakeAddGlassesValidation:
    fields: list = [
        'image',
        'image_type',
        'user_id',
        'model',
        'format',
        'gender',
        'public',
        'category',
        'frame_color',
        'lens_color',
        'size_lens',
        'size_bridge',
        'height_frame',
        'size_temples',
        'price',
        'additional_info'
    ]

    def test_1_should_call_ValidationComposite_with_all_validations(self):
        validations = [
            RequiredFieldValidation(field_name=field)
            for field in self.fields
        ]
        validation_composite = ValidationComposite(validations)

        assert validation_composite == make_add_glasses_validation()
