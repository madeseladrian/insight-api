from abc import ABC, abstractmethod
from dataclasses import dataclass

from ....params import AddImageRepositoryParams, AddImageRepositoryResult


@dataclass
class AddImageStorage(ABC):

    @abstractmethod
    def add_image(self, params: AddImageRepositoryParams) -> AddImageRepositoryResult:
        raise NotImplementedError('Should implement method: add_image')
