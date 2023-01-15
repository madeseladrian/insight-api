from dataclasses import dataclass
from typing import Any

from ...domain.features import AddGlasses
from ...domain.params import AddGlassesParams

from ..contracts.db.glasses import AddGlassesRepository


@dataclass
class DbAddGlasses(AddGlasses):
    add_glasses_repository: AddGlassesRepository

    def add(self, data: AddGlassesParams) -> Any:
        return self.add_glasses_repository.add(data)
