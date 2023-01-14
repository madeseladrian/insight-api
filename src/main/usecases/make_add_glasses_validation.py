from typing import List

from ...presentation.contracts import Validation
from ...validation.validators import (
    ValidationComposite,
    RequiredFieldValidation,
)

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

def make_add_glasses_validation() -> ValidationComposite:
    validations: List[Validation] = [
        RequiredFieldValidation(field_name=field)
        for field in fields
    ]

    return ValidationComposite(validations=validations)
