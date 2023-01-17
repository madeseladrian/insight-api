from dataclasses import dataclass
from typing import Any

from ...domain.features import DeleteGlasses

from ..contracts import Validation
from ..helpers import (
    bad_request,
    server_error
)
from ..params import AddGlassesControllerRequest


@dataclass
class DeleteGlassesController:
    delete_glasses: DeleteGlasses
    validation: Validation

    def handle(self, request: AddGlassesControllerRequest) -> Any:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)
            self.delete_glasses.delete(request)
        except Exception as e:
            return server_error(e)
