from dataclasses import dataclass

from ...domain.features import DeleteGlasses
from ...domain.params import DeleteGlassesParams

from ..contracts.db.glasses import DeleteGlassesRepository


@dataclass
class DbDeleteGlasses(DeleteGlasses):
    delete_glasses_repository: DeleteGlassesRepository

    def delete(self, params: DeleteGlassesParams) -> None:
        self.delete_glasses_repository.delete(params)
