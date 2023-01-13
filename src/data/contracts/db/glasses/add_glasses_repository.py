from abc import ABC, abstractmethod
from ....params import AddGlassesRepositoryParams, AddGlassesRepositoryResult


class AddGlassesRepository(ABC):

    @abstractmethod
    def add(self, data: AddGlassesRepositoryParams) -> AddGlassesRepositoryResult:
        raise NotImplementedError('Should implement method: add')
