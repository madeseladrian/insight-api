from dataclasses import dataclass

from ...domain.features import AddGlasses
from ...domain.params import AddGlassesParams
from ..contracts.db.glasses import AddGlassesRepository

@dataclass
class DbAddGlasses(AddGlasses):
    add_glasses_repository: AddGlassesRepository

    def add(self, data: AddGlassesParams) -> None:
        self.add_glasses_repository.add(data)
