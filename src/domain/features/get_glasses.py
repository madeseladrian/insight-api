from abc import ABC, abstractmethod
from dataclasses import dataclass

from ..params import GetGlassesParams, GetGlassesResult


@dataclass
class GetGlasses(ABC):

    @abstractmethod
    def get(self, params: GetGlassesParams) -> GetGlassesResult:
        raise NotImplementedError('Should implement method: get')
