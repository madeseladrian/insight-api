from abc import ABC, abstractmethod
from dataclasses import dataclass

from ....params import UpdateGlassesRepositoryParams


@dataclass
class UpdateGlassesRepository(ABC):

    @abstractmethod
    def update(self, params: UpdateGlassesRepositoryParams) -> None:
        raise NotImplementedError('Should implement method: update')
