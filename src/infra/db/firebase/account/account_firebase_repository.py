from dataclasses import dataclass

from .....data.contracts.db.account import (
    AddAccountRepository,
    CheckAccountByEmailRepository,
    LoadAccountByEmailRepository,
    UpdateAccessTokenRepository
)
from .....data.params import (
    AddAccountRepositoryParams,
    AddAccountRepositoryResult,
    LoadAccountByEmailRepositoryResult
)
from .firebase_helper import firebase_helper


@dataclass
class AccountFirebaseRepository(
    AddAccountRepository,
    CheckAccountByEmailRepository,
    LoadAccountByEmailRepository,
    UpdateAccessTokenRepository
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

    def load_by_email(self, email: str) -> LoadAccountByEmailRepositoryResult:
        account = firebase_helper.get_collection().where(
            'email', '==', email
        ).stream()

        data = [e.to_dict() for e in account]

        return data[0] if len(data) == 1 else None

    def update_access_token(self, user_id: str, token: str) -> None:
        account = firebase_helper.get_collection().where(
            'id', '==', user_id
        ).stream()

        document_id = [doc.id for doc in account][0]
        firebase_helper.get_collection().document(document_id).update({
            'access_token': token
        })
