from dataclasses import dataclass
from typing import Any

from ..contracts import Validation
from ..helpers import bad_request
from ..params import UpdateImageControllerRequest


@dataclass
class UpdateGlassesController:
    validation: Validation

    def handle(self, request: UpdateImageControllerRequest) -> Any:
        if error := self.validation.validate(request):
            return bad_request(error)
