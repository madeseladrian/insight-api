from abc import ABC, abstractmethod
from dataclasses import dataclass
from tempfile import SpooledTemporaryFile
from typing import Tuple

@dataclass
class AddImageStorage(ABC):

    @abstractmethod
    def add_image(self, image: SpooledTemporaryFile, image_type: str) -> Tuple[str, str]:
        raise NotImplementedError('Should implement method: add_image')
