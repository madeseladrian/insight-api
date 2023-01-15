from dataclasses import dataclass

from ...domain.features import AddImage

from ..contracts import Controller, Validation
from ..helpers import (
    bad_request,
    HttpResponse,
    no_content,
    server_error
)
from ..params import AddImageControllerRequest


@dataclass
class AddImageController(Controller):
    add_image: AddImage
    validation: Validation

    def handle(self, request: AddImageControllerRequest) -> HttpResponse:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

            self.add_image.add_image(request)
            return no_content()
        except Exception as e:
            return server_error(e)
