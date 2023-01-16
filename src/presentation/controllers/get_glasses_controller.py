from dataclasses import dataclass
from typing import Any

from ..contracts import Validation
from ..params import GetGlassesControllerRequest


@dataclass
class GetGlassesController:
    validation: Validation

    def handle(self, request: GetGlassesControllerRequest) -> Any:
        self.validation.validate(request)
