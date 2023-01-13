from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import AddGlassesParams, AddGlassesResult


@dataclass
class AddGlasses(ABC):

    @abstractmethod
    def add(self, data: AddGlassesParams) -> AddGlassesResult:
        raise NotImplementedError('Should implement method: add')
