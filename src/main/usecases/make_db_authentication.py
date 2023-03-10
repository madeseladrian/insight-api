from ...domain.features import Authentication
from ...data.usecases import DbAuthentication

from ...infra.cryptography import BCryptAdapter, JoseAdapter
from ...infra.db.firebase.account import AccountFirebaseRepository

from ..config.database import settings


def make_db_authentication() -> Authentication:
    jose_adapter = JoseAdapter(
        algorithm=settings.algorithm,
        expire_in_days=settings.access_token_expire_days,
        key=settings.secret_key
    )
    account_firebases_repository = AccountFirebaseRepository()

    return DbAuthentication(
        encrypter=jose_adapter,
        hash_comparer=BCryptAdapter(),
        loadAccount_by_email_repository=account_firebases_repository,
        update_access_token_repository=account_firebases_repository
    )
