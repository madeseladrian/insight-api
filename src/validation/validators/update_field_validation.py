from dataclasses import dataclass
from typing import Any, List, Optional

from ...presentation.contracts import Validation
from ...presentation.errors import InvalidParamError


@dataclass
class UpdateFieldValidation(Validation):
    field_name: str
    list_of_fields_to_compare: List

    def validate(self, value: Any) -> Optional[Exception]:
        if value[0] in value[1]:
            return None
        return InvalidParamError(value[0])
