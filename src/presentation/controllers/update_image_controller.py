from dataclasses import dataclass
from typing import Any

from ..contracts import Validation
from ..helpers import bad_request, server_error
from ..params import UpdateImageControllerRequest


@dataclass
class UpdateGlassesController:
    validation: Validation

    def handle(self, request: UpdateImageControllerRequest) -> Any:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)
        except Exception as e:
            return server_error(e)
