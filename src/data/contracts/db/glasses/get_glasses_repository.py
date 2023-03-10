from abc import ABC, abstractmethod
from dataclasses import dataclass

from ....params import GetGlassesRepositoryParams, GetGlassesRepositoryResult


@dataclass
class GetGlassesRepository(ABC):

    @abstractmethod
    def get(self, params: GetGlassesRepositoryParams) -> GetGlassesRepositoryResult:
        raise NotImplementedError('Should implement method: get')
