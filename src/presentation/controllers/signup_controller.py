from dataclasses import dataclass

from ..contracts import Validation
from ..params import SignUpControllerRequest


@dataclass
class SignUpController():
    validation: Validation

    def handle(self, request: SignUpControllerRequest) -> None:
        self.validation.validate(request)
