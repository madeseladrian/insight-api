from dataclasses import dataclass
from typing import Any

from ...domain.features import AddImage

from ..contracts import Validation
from ..helpers import bad_request, server_error
from ..params import AddImageControllerRequest


@dataclass
class AddImageController:
    add_image: AddImage
    validation: Validation

    def handle(self, request: AddImageControllerRequest) -> Any:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

            self.add_image.add_image(request)
        except Exception as e:
            return server_error(e)
