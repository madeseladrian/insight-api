from abc import ABC, abstractmethod
from ....params import AddGlassesRepositoryParams, AddAccountRepositoryResult


class AddGlassesRepository(ABC):

    @abstractmethod
    def add(self, data: AddGlassesRepositoryParams) -> AddAccountRepositoryResult:
        raise NotImplementedError('Should implement method: add')
