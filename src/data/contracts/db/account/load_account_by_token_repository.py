from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from ....params import LoadAccountByTokenRepositoryResult


@dataclass
class LoadAccountByTokenRepository(ABC):

    @abstractmethod
    def load_by_token(self, token: str) -> Optional[LoadAccountByTokenRepositoryResult]:
        raise NotImplementedError('Should implement method: load_by_token')
