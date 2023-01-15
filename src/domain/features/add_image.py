from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.params import AddImageParams, AddImageResult


@dataclass
class AddImage(ABC):

    @abstractmethod
    def add_image(self, params: AddImageParams) -> AddImageResult:
        raise NotImplementedError('Should implement method: add_image')
