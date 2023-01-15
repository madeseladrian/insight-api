from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import AddImageParams


@dataclass
class AddImage(ABC):

    @abstractmethod
    def add_image(self, params: AddImageParams) -> None:
        raise NotImplementedError('Should implement method: add_image')
