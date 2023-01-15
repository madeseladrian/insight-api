from abc import ABC, abstractmethod
from dataclasses import dataclass

from ....params import AddAccountRepositoryParams, AddAccountRepositoryResult


@dataclass
class AddAccountRepository(ABC):

    @abstractmethod
    def add(self, data: AddAccountRepositoryParams) -> AddAccountRepositoryResult:
        raise NotImplementedError('Should implement method: add')
