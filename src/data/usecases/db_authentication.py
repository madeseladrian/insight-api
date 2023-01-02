from dataclasses import dataclass
from typing import Any

from ...domain.features import Authentication
from ...domain.params import AuthenticationParams

from ..contracts.cryptography import HashComparer
from ..contracts.db.account import LoadAccountByEmailRepository


@dataclass
class DbAuthentication(Authentication):
    hash_comparer: HashComparer
    loadAccount_by_email_repository: LoadAccountByEmailRepository

    def auth(self, authentication: AuthenticationParams) -> Any:
        if account := self.loadAccount_by_email_repository.load_by_email(
            email=authentication['email']
        ):
            self.hash_comparer.verify_password(
                plain_password=authentication['password'],
                hashed_password=account['password']
            )
