from dataclasses import dataclass
from typing import Any

from ..contracts import Validation
from ..params import AddImageControllerRequest


@dataclass
class AddImageController:
    validation: Validation

    def handle(self, request: AddImageControllerRequest) -> Any:
        self.validation.validate(request)
