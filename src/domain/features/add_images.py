from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import AddImagesParams


@dataclass
class AddImages(ABC):

    @abstractmethod
    def add_image(self, params: AddImagesParams) -> None:
        raise NotImplementedError('Should implement method: add_image')
