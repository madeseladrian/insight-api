from abc import ABC, abstractmethod
from ....params import AddGlassesRepositoryParams


class AddGlassesRepository(ABC):

    @abstractmethod
    def add(self, data: AddGlassesRepositoryParams) -> None:
        raise NotImplementedError('Should implement method: add')
