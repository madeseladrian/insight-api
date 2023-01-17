from src.validation.validators import (
    ValidationComposite,
    RequiredFieldValidation,
    UpdateFieldValidation
)
from src.main.usecases import make_update_glasses_validation


class TestMakeUpdateGlassesValidation:
    list_of_fields_to_compare = [
        'url_image',
        'glasses_id',
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

    fields = ['glasses_id', 'data']

    def test_1_should_call_ValidationComposite_with_all_validations(self):
        validations = [
            RequiredFieldValidation(field_name=field)
            for field in self.fields
        ]
        validations.append(UpdateFieldValidation(
            list_of_fields_to_compare=self.list_of_fields_to_compare
        ))
        validation_composite = ValidationComposite(validations)

        assert validation_composite == make_update_glasses_validation()
