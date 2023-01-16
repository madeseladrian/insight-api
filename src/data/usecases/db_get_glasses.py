from dataclasses import dataclass

from ...domain.features import GetGlasses
from ...domain.params import GetGlassesParams, GetGlassesResult

from ..contracts.db.glasses import GetGlassesRepository


@dataclass
class DbGetGlasses(GetGlasses):
    get_glasses_repository: GetGlassesRepository

    def get(self, params: GetGlassesParams) -> GetGlassesResult:
        return self.get_glasses_repository.get(params)
