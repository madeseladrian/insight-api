from dataclasses import dataclass

# from ...domain.features import AddGlasses

from ..contracts import Validation
from ..params import AddGlassesControllerRequest

@dataclass
class AddGlassesController:
    validation: Validation

    def handle(self, request: AddGlassesControllerRequest) -> None:
        self.validation.validate(request)
