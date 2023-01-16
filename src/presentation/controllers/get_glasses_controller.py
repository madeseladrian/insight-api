from dataclasses import dataclass
from typing import Any

from ..contracts import Validation
from ..helpers import bad_request, server_error
from ..params import GetGlassesControllerRequest


@dataclass
class GetGlassesController:
    validation: Validation

    def handle(self, request: GetGlassesControllerRequest) -> Any:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

        except Exception as e:
            return server_error(e)
