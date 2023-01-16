from dataclasses import dataclass
from typing import Any

from ...domain.features import GetGlasses

from ..contracts import Validation
from ..helpers import bad_request, server_error
from ..params import GetGlassesControllerRequest


@dataclass
class GetGlassesController:
    get_glasses: GetGlasses
    validation: Validation

    def handle(self, request: GetGlassesControllerRequest) -> Any:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

            self.get_glasses.get(request)
        except Exception as e:
            return server_error(e)
