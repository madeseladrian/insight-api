from dataclasses import dataclass
from typing import Any, Optional

from ..contracts.cryptography import Decrypter
from ..contracts.db.account import LoadAccountByTokenRepository


@dataclass
class DbLoadAccountByToken:
    decrypter: Decrypter
    load_account_by_token_repository: LoadAccountByTokenRepository

    def load(self, access_token: str, role: Optional[str] = None) -> Any:
        if self.decrypter.decrypt(token=access_token):
            if account := self.load_account_by_token_repository.load_by_token(
                token=access_token,
                role=role
            ):
                return account
        return None
