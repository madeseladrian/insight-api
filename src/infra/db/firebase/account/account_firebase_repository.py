from dataclasses import dataclass

from .....data.contracts.db.account import (
    AddAccountRepository,
    CheckAccountByEmailRepository
)
from .....data.params import (
    AddAccountRepositoryParams,
    AddAccountRepositoryResult
)
from .firebase_helper import firebase_helper


@dataclass
class AccountFirebaseRepository(
    AddAccountRepository,
    CheckAccountByEmailRepository
):

    def add(self, data: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
        account = firebase_helper.get_document()
        account.set(data)
        return bool(account.get().to_dict())

    def check_by_email(self, email: str) -> bool:
        account = firebase_helper.get_collection().where(
            'email', '==', email
        ).stream()
        return bool([e.to_dict() for e in account])
