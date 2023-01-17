from dataclasses import dataclass
from typing import Any

from ..contracts import Validation
from ..params import UpdateGlassesControllerRequest


@dataclass
class UpdateGlassesController:
    validation: Validation

    def handle(self, request: UpdateGlassesControllerRequest) -> Any:
        self.validation.validate(request)
