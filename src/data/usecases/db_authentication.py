from dataclasses import dataclass
from typing import Any

from ...domain.features import Authentication
from ...domain.params import AuthenticationParams

from ..contracts.cryptography import Encrypter, HashComparer
from ..contracts.db.account import LoadAccountByEmailRepository


@dataclass
class DbAuthentication(Authentication):
    encrypter: Encrypter
    hash_comparer: HashComparer
    loadAccount_by_email_repository: LoadAccountByEmailRepository

    def auth(self, authentication: AuthenticationParams) -> Any:
        if account := self.loadAccount_by_email_repository.load_by_email(
            email=authentication['email']
        ):
            if self.hash_comparer.verify_password(
                plain_password=authentication['password'],
                hashed_password=account['password']
            ):
                self.encrypter.encrypt(user_id=account['id'])
