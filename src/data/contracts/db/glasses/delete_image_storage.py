from abc import ABC, abstractmethod
from dataclasses import dataclass

from ....params import DeleteImageRepositoryParams


@dataclass
class DeleteImageStorage(ABC):

    @abstractmethod
    def delete_image(self, params: DeleteImageRepositoryParams) -> None:
        raise NotImplementedError('Should implement method: delete_image')
