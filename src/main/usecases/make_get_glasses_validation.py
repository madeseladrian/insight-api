from typing import List

from ...presentation.contracts import Validation
from ...validation.validators import (
    ValidationComposite,
    RequiredFieldValidation,
)


fields: list = ['user_id']

def make_get_glasses_validation() -> ValidationComposite:
    validations: List[Validation] = [
        RequiredFieldValidation(field_name=field)
        for field in fields
    ]

    return ValidationComposite(validations=validations)
