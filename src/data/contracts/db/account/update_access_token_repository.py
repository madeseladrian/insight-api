from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class UpdateAccessTokenRepository(ABC):

    @abstractmethod
    def update_access_token(self, user_id: str, token: str) -> None:
        raise NotImplementedError('Should implement method: update_access_token')
