from typing import List

from ...presentation.contracts import Validation
from ...validation.validators import (
  ValidationComposite,
  RequiredFieldValidation,
  UpdateFieldValidation
)


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

def make_update_glasses_validation() -> ValidationComposite:
    validations: List[Validation] = [
        RequiredFieldValidation(field_name=field)
        for field in fields
    ]

    validations.append(UpdateFieldValidation(
        list_of_fields_to_compare=list_of_fields_to_compare
    ))

    return ValidationComposite(validations=validations)
