from dataclasses import dataclass

from ...domain.features import AddAccount
from ...domain.params import AddAccountParams

from ..contracts import Validation
from ..helpers import bad_request, server_error
from ..params import SignUpControllerRequest


@dataclass
class SignUpController():
    add_account: AddAccount
    validation: Validation

    def handle(self, request: SignUpControllerRequest):
        try:
            if error := self.validation.validate(request):
                return bad_request(error)
            self.add_account.add(AddAccountParams(
                name=request['name'],
                email=request['email'],
                password=request['password']
            ))

        except Exception as e:
            return server_error(e)
