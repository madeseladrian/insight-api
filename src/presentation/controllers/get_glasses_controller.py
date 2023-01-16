from dataclasses import dataclass

from ...domain.features import GetGlasses

from ..contracts import Controller, Validation
from ..helpers import (
    bad_request,
    HttpResponse,
    ok,
    server_error
)
from ..params import GetGlassesControllerRequest


@dataclass
class GetGlassesController(Controller):
    get_glasses: GetGlasses
    validation: Validation

    def handle(self, request: GetGlassesControllerRequest) -> HttpResponse:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

            glasses = self.get_glasses.get(request)
            return ok(glasses)
        except Exception as e:
            return server_error(e)
