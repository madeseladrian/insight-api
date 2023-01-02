from dataclasses import dataclass
from typing import Any

from ...domain.features import Authentication

from ..contracts import Validation
from ..helpers import bad_request, server_error
from ..params import LoginControllerRequest


@dataclass
class LoginController:
    authentication: Authentication
    validation: Validation

    def handle(self, request: LoginControllerRequest) -> Any:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)
            self.authentication.auth(request)
        except Exception as e:
            return server_error(e)
