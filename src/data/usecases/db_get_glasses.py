from dataclasses import dataclass
from typing import Any

from ...domain.params import GetGlassesParams

from ..contracts.db.glasses import GetGlassesRepository


@dataclass
class DbGetGlasses:
    get_glasses_repository: GetGlassesRepository

    def get(self, params: GetGlassesParams) -> Any:
        self.get_glasses_repository.get(params)
