from abc import ABC, abstractmethod
from dataclasses import dataclass
from tempfile import SpooledTemporaryFile


@dataclass
class AddImageStorage(ABC):

    @abstractmethod
    def add_image(self, image: SpooledTemporaryFile, image_type: str) -> str:
        raise NotImplementedError('Should implement method: add_image')
