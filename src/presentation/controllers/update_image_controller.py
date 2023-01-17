from dataclasses import dataclass

from ...domain.features import UpdateImage

from ..contracts import Controller, Validation
from ..helpers import (
    bad_request,
    HttpResponse,
    no_content,
    server_error
)
from ..params import UpdateImageControllerRequest


@dataclass
class UpdateImageController(Controller):
    update_image: UpdateImage
    validation: Validation

    def handle(self, request: UpdateImageControllerRequest) -> HttpResponse:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)
            self.update_image.update_image(request)
            return no_content()

        except Exception as e:
            return server_error(e)
