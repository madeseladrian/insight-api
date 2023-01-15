from dataclasses import dataclass
from typing import Any, Optional

from ..contracts.cryptography import Decrypter


@dataclass
class DbLoadAccountByToken:
    decrypter: Decrypter

    def load(self, access_token: str, role: Optional[str] = None) -> Any:
        self.decrypter.decrypt(token=access_token)
