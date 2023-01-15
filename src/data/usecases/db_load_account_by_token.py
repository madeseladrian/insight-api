from dataclasses import dataclass
from typing import Optional

from ...domain.features import LoadAccountByToken
from ...domain.params import LoadAccountByTokenResult

from ..contracts.cryptography import Decrypter
from ..contracts.db.account import LoadAccountByTokenRepository


@dataclass
class DbLoadAccountByToken(LoadAccountByToken):
    decrypter: Decrypter
    load_account_by_token_repository: LoadAccountByTokenRepository

    def load(self, access_token: str) -> Optional[LoadAccountByTokenResult]:
        if self.decrypter.decrypt(token=access_token):
            if account := self.load_account_by_token_repository.load_by_token(
                token=access_token
            ):
                return account
        return None
