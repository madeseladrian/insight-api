from dataclasses import dataclass

from ...domain.features import AddGlasses

from ..contracts import Controller, Validation
from ..helpers import (
    bad_request,
    HttpResponse,
    no_content,
    server_error
)
from ..params import AddGlassesControllerRequest


@dataclass
class AddGlassesController(Controller):
    add_glasses: AddGlasses
    validation: Validation

    def handle(self, request: AddGlassesControllerRequest) -> HttpResponse:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

            self.add_glasses.add(request)
            return no_content()
        except Exception as e:
            return server_error(e)
