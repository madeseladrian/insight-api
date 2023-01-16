from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..params import DeleteGlassesParams


@dataclass
class DeleteGlasses(ABC):

    @abstractmethod
    def delete(self, params: DeleteGlassesParams) -> None:
        raise NotImplementedError('Should implement method: delete')
