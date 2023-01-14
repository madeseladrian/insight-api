from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import AddGlassesParams


@dataclass
class AddGlasses(ABC):

    @abstractmethod
    def add(self, data: AddGlassesParams) -> None:
        raise NotImplementedError('Should implement method: add')
