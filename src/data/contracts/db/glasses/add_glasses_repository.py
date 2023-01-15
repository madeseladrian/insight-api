from abc import ABC, abstractmethod
from dataclasses import dataclass

from ....params import AddGlassesRepositoryParams, AddAccountRepositoryResult


@dataclass
class AddGlassesRepository(ABC):

    @abstractmethod
    def add(self, data: AddGlassesRepositoryParams) -> AddAccountRepositoryResult:
        raise NotImplementedError('Should implement method: add')
