from dataclasses import dataclass
from typing import Any
# from ...domain.features import AddGlasses

from ..contracts import Validation
from ..helpers import bad_request
from ..params import AddGlassesControllerRequest

@dataclass
class AddGlassesController:
    validation: Validation

    def handle(self, request: AddGlassesControllerRequest) -> Any:
        if error := self.validation.validate(request):
            return bad_request(error)
