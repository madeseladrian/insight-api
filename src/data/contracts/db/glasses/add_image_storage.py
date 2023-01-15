from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import BinaryIO, Tuple


@dataclass
class AddImageStorage(ABC):

    @abstractmethod
    def add_image(self, image: BinaryIO, image_type: str) -> Tuple[str, str]:
        raise NotImplementedError('Should implement method: add_image')
