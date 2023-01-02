from dataclasses import dataclass
from typing import Any

from ..contracts import Validation
from ..helpers import bad_request
from ..params import LoginControllerRequest


@dataclass
class LoginController:
    validation: Validation

    def handle(self, request: LoginControllerRequest) -> Any:
        if error := self.validation.validate(request):
            return bad_request(error)
