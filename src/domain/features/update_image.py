from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import UpdateImageParams


@dataclass
class UpdateImage(ABC):

    @abstractmethod
    def update_image(self, params: UpdateImageParams) -> None:
        raise NotImplementedError('Should implement method: update_image')
