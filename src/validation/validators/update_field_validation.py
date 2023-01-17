from dataclasses import dataclass
from typing import Any, List, Optional

from ...presentation.contracts import Validation
from ...presentation.errors import InvalidParamError


@dataclass
class UpdateFieldValidation(Validation):
    list_of_fields_to_compare: List

    def validate(self, value: Any) -> Optional[Exception]:
        fields = list(set(value['data']))

        for field in fields:
            if field not in self.list_of_fields_to_compare:
                return InvalidParamError(field)

        return None
