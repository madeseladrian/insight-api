from dataclasses import dataclass
from typing import Any

from ..contracts import Validation
from ..params import UpdateImageControllerRequest


@dataclass
class UpdateGlassesController:
    validation: Validation

    def handle(self, request: UpdateImageControllerRequest) -> Any:
        self.validation.validate(request)
