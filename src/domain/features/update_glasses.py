from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..params import UpdateGlassesParams


@dataclass
class UpdateGlasses(ABC):

    @abstractmethod
    def update(self, params: UpdateGlassesParams) -> None:
        raise NotImplementedError('Should implement method: update')
