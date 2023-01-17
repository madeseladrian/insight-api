from dataclasses import dataclass
from typing import Any

from ...domain.features import UpdateGlasses

from ..contracts import Validation
from ..helpers import bad_request, server_error
from ..params import UpdateGlassesControllerRequest


@dataclass
class UpdateGlassesController:
    validation: Validation
    update_glasses: UpdateGlasses

    def handle(self, request: UpdateGlassesControllerRequest) -> Any:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

            self.update_glasses.update(request)
        except Exception as e:
            return server_error(e)
