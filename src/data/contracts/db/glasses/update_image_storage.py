from abc import ABC, abstractmethod
from dataclasses import dataclass

from ....params import UpdateImageRepositoryParams


@dataclass
class UpdateImageStorage(ABC):

    @abstractmethod
    def update_image(self, params: UpdateImageRepositoryParams) -> None:
        raise NotImplementedError('Should implement method: update_image')
