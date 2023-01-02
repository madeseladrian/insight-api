from dataclasses import dataclass
from typing import Any

from ...domain.features import Authentication
from ...domain.params import AuthenticationParams

from ..contracts.db.account import LoadAccountByEmailRepository


@dataclass
class DbAuthentication(Authentication):
    loadAccount_by_email_repository: LoadAccountByEmailRepository

    def auth(self, authentication: AuthenticationParams) -> Any:
        self.loadAccount_by_email_repository.load_by_email(
            email=authentication['email']
        )
