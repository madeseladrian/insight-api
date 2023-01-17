from typing import List

from ...presentation.contracts import Validation
from ...validation.validators import (
  ValidationComposite,
  RequiredFieldValidation
)


fields: list = [
    "content_type",
    "glasses_id",
    "image"
]

def make_update_image_validation() -> ValidationComposite:
    validations: List[Validation] = [
        RequiredFieldValidation(field_name=field)
        for field in fields
    ]

    return ValidationComposite(validations=validations)
