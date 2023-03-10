from dataclasses import dataclass
from typing import Optional

from .....data.contracts.db.account import (
    AddAccountRepository,
    CheckAccountByEmailRepository,
    LoadAccountByEmailRepository,
    LoadAccountByTokenRepository,
    UpdateAccessTokenRepository
)
from .....data.params import (
    AddAccountRepositoryParams,
    AddAccountRepositoryResult,
    LoadAccountByEmailRepositoryResult,
    LoadAccountByTokenRepositoryResult
)
from ..firebase_helper import firebase_helper


@dataclass
class AccountFirebaseRepository(
    AddAccountRepository,
    CheckAccountByEmailRepository,
    LoadAccountByEmailRepository,
    LoadAccountByTokenRepository,
    UpdateAccessTokenRepository
):

    def add(self, data: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
        account = firebase_helper.get_document('users')
        account.set(data)

        return bool(account.get().to_dict())

    def check_by_email(self, email: str) -> bool:
        account = firebase_helper.get_collection('users').where(
            'email', '==', email
        ).stream()

        return bool([e.to_dict() for e in account])

    def load_by_email(self, email: str) -> LoadAccountByEmailRepositoryResult:
        account = firebase_helper.get_collection('users').where(
            'email', '==', email
        ).stream()

        data = [e.to_dict() for e in account]

        return data[0] if len(data) == 1 else None

    def load_by_token(self, token: str) -> Optional[LoadAccountByTokenRepositoryResult]:
        account = firebase_helper.get_collection('users').where(
            'access_token', '==', token
        ).stream()

        data = [doc.to_dict() for doc in account]
        return LoadAccountByTokenRepositoryResult(id=data[0]['id']) if len(data) == 1 else None

    def update_access_token(self, user_id: str, token: str) -> None:
        account = firebase_helper.get_collection('users').where(
            'id', '==', user_id
        ).stream()

        document_id = [doc.id for doc in account][0]
        firebase_helper.get_collection('users').document(document_id).update({
            'access_token': token
        })
