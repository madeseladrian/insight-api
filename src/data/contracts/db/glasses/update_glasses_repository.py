from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass
class UpdateGlassesRepository(ABC):

    @abstractmethod
    def update(self, data: Dict) -> None:
        raise NotImplementedError('Should implement method: update')
