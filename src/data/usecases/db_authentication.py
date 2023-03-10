from dataclasses import dataclass
from typing import Optional

from ...domain.features import Authentication
from ...domain.params import AuthenticationParams, AuthenticationResult

from ..contracts.cryptography import Encrypter, HashComparer
from ..contracts.db.account import (
  LoadAccountByEmailRepository,
  UpdateAccessTokenRepository
)


@dataclass
class DbAuthentication(Authentication):
    encrypter: Encrypter
    hash_comparer: HashComparer
    loadAccount_by_email_repository: LoadAccountByEmailRepository
    update_access_token_repository: UpdateAccessTokenRepository

    def auth(self, authentication: AuthenticationParams) -> Optional[AuthenticationResult]:
        if account := self.loadAccount_by_email_repository.load_by_email(
            email=authentication['email']
        ):
            if self.hash_comparer.verify_password(
                plain_password=authentication['password'],
                hashed_password=account['password']
            ):
                access_token = self.encrypter.encrypt(user_id=account['id'])
                self.update_access_token_repository.update_access_token(
                    user_id=account['id'],
                    token=access_token
                )
                return AuthenticationResult(
                    access_token=access_token,
                    name=account['name']
                )
        return None
