from ...domain.features import AddAccount
from ...data.usecases import DbAddAccount

from ...infra.cryptography import BCryptAdapter
from ...infra.db.firebase.account import AccountFirebaseRepository


def make_db_add_account() -> AddAccount:
    account_firebase_repository = AccountFirebaseRepository()

    return DbAddAccount(
        add_account_repository=account_firebase_repository,
        check_account_by_email_repository=account_firebase_repository,
        hasher=BCryptAdapter()
    )
