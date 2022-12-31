from dataclasses import dataclass

from .....data.contracts.db.account import AddAccountRepository
from .....data.params import (
    AddAccountRepositoryParams,
    AddAccountRepositoryResult
)
from .firebase_helper import firebase_helper


@dataclass
class AccountFirebaseRepository(AddAccountRepository):

    def add(self, data: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
        account = firebase_helper.get_collection()
        account.set(data)
        return bool(account.get().to_dict())
