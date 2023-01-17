from dataclasses import dataclass

from ...domain.features import DeleteGlasses

from ..contracts import Controller, Validation
from ..helpers import (
    bad_request,
    HttpResponse,
    no_content,
    server_error
)
from ..params import AddGlassesControllerRequest


@dataclass
class DeleteGlassesController(Controller):
    delete_glasses: DeleteGlasses
    validation: Validation

    def handle(self, request: AddGlassesControllerRequest) -> HttpResponse:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)
            self.delete_glasses.delete(request)
            return no_content()
        except Exception as e:
            return server_error(e)
