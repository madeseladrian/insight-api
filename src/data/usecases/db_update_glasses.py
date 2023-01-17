from dataclasses import dataclass

from ...domain.features import UpdateGlasses

from ..contracts.db.glasses import UpdateGlassesRepository
from ..params import UpdateGlassesRepositoryParams


@dataclass
class DbUpdateGlasses(UpdateGlasses):
    update_glasses_repository: UpdateGlassesRepository

    def update(self, data: UpdateGlassesRepositoryParams) -> None:
        self.update_glasses_repository.update(data)
