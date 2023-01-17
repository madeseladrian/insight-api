from dataclasses import dataclass
from typing import Any

from ..contracts import Validation
from ..params import AddGlassesControllerRequest


@dataclass
class DeleteGlassesController:
    validation: Validation

    def handle(self, request: AddGlassesControllerRequest) -> Any:
        self.validation.validate(request)
