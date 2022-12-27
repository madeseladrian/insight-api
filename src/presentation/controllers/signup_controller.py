from dataclasses import dataclass

from ..contracts import Validation
from ..helpers import bad_request, server_error
from ..params import SignUpControllerRequest


@dataclass
class SignUpController():
    validation: Validation

    def handle(self, request: SignUpControllerRequest):
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

        except Exception as e:
            return server_error(e)
