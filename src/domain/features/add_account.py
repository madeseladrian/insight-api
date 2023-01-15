from dataclasses import dataclass
from abc import ABC, abstractmethod

from ..params import AddAccountParams, AddAccountResult


@dataclass
class AddAccount(ABC):
    @abstractmethod
    def add(self, account: AddAccountParams) -> AddAccountResult:
        raise NotImplementedError('Should implement method: add')
