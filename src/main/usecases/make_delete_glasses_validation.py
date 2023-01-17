from typing import List

from ...presentation.contracts import Validation
from ...validation.validators import (
    ValidationComposite,
    RequiredFieldValidation,
)

fields: list = ['glasses_id']

def make_delete_glasses_validation() -> ValidationComposite:
    validations: List[Validation] = [
        RequiredFieldValidation(field_name=field)
        for field in fields
    ]

    return ValidationComposite(validations=validations)
