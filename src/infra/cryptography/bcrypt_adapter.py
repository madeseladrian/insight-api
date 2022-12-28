from dataclasses import dataclass
from passlib.context import CryptContext

from ...data.contracts.cryptography import Hasher


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@dataclass
class BCryptAdapter(Hasher):

    def get_password_hash(self, password: str) -> str:
        return ''
