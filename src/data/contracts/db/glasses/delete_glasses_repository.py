from abc import ABC, abstractmethod
from dataclasses import dataclass

from ....params import DeleteGlassesRepositoryParams


@dataclass
class DeleteGlassesRepository(ABC):

    @abstractmethod
    def delete(self, params: DeleteGlassesRepositoryParams) -> None:
        raise NotImplementedError('Should implement method: delete')
