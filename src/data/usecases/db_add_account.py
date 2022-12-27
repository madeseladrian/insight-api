from dataclasses import dataclass

from ...domain.params import AddAccountParams
from ..contracts.db.account import CheckAccountByEmailRepository


@dataclass
class DbAddAccount():
    check_account_by_email_repository: CheckAccountByEmailRepository

    def add(self, account: AddAccountParams):
        self.check_account_by_email_repository.check_by_email(email=account['email'])
        return True
