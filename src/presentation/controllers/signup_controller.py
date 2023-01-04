from dataclasses import dataclass
from typing import Any
import uuid

from ...domain.features import AddAccount, Authentication
from ...domain.params import AddAccountParams, AuthenticationParams

from ..contracts import Controller, Validation
from ..errors import EmailInUseError
from ..helpers import (
    bad_request,
    forbidden,
    server_error
)
from ..params import SignUpControllerRequest


@dataclass
class SignUpController(Controller):
    add_account: AddAccount
    authentication: Authentication
    validation: Validation

    def handle(self, request: SignUpControllerRequest) -> Any:
        try:
            if error := self.validation.validate(request):
                return bad_request(error)

            if self.add_account.add(AddAccountParams(
                id=str(uuid.uuid4()),
                name=request['name'],
                email=request['email'],
                password=request['password']
            )):
                self.authentication.auth(AuthenticationParams(
                    email=request['email'],
                    password=request['password']
                ))

            else:
                return forbidden(EmailInUseError())

        except Exception as e:
            return server_error(e)
