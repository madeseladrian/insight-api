from dataclasses import dataclass

from ..contracts import Validation
from ..helpers import bad_request
from ..params import SignUpControllerRequest


@dataclass
class SignUpController():
    validation: Validation

    def handle(self, request: SignUpControllerRequest):
        if error := self.validation.validate(request):
            return bad_request(error)
