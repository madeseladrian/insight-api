from dataclasses import dataclass

from ...domain.params import AddAccountParams
from ..contracts.cryptography import Hasher
from ..contracts.db.account import CheckAccountByEmailRepository


@dataclass
class DbAddAccount():
    check_account_by_email_repository: CheckAccountByEmailRepository
    hasher: Hasher

    def add(self, account: AddAccountParams):
        exists = self.check_account_by_email_repository.check_by_email(email=account['email'])
        is_valid = False

        if not exists:
            self.hasher.get_password_hash(account['password'])
            is_valid = True
        return is_valid
