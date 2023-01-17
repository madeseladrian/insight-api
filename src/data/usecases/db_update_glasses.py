from dataclasses import dataclass
from typing import Dict

from ...domain.features import UpdateGlasses

from ..contracts.db.glasses import UpdateGlassesRepository


@dataclass
class DbUpdateGlasses(UpdateGlasses):
    update_glasses_repository: UpdateGlassesRepository

    def update(self, data: Dict) -> None:
        self.update_glasses_repository.update(data)
