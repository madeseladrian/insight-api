from dataclasses import dataclass

from ...domain.features import UpdateGlasses

from ..contracts import Controller, Validation
from ..helpers import (
    bad_request,
    HttpResponse,
    no_content,
    server_error
)
from ..params import UpdateGlassesControllerRequest


@dataclass
class UpdateGlassesController(Controller):
    validation: Validation
    update_glasses: UpdateGlasses

    def handle(self, request: UpdateGlassesControllerRequest) -> HttpResponse:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

            self.update_glasses.update(request)
            return no_content()
        except Exception as e:
            return server_error(e)
