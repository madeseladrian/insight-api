from dataclasses import dataclass
from typing import Any

from ...domain.features import UpdateImage

from ..contracts import Validation
from ..helpers import bad_request, server_error
from ..params import UpdateImageControllerRequest


@dataclass
class UpdateImageController:
    update_image: UpdateImage
    validation: Validation

    def handle(self, request: UpdateImageControllerRequest) -> Any:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)
            self.update_image.update_image(request)
        except Exception as e:
            return server_error(e)
