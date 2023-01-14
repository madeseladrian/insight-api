from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AddImageStorage(ABC):

    @abstractmethod
    def add_image(self, image: bytes) -> str:
        raise NotImplementedError('Should implement method: add_image')
