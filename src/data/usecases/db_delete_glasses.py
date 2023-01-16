from dataclasses import dataclass

from ...domain.features import DeleteGlasses
from ...domain.params import DeleteGlassesParams

from ..params import (
    DeleteGlassesRepositoryParams,
    DeleteImageRepositoryParams
)
from ..contracts.db.glasses import (
    DeleteGlassesRepository,
    DeleteImageStorage
)


@dataclass
class DbDeleteGlasses(DeleteGlasses):
    delete_glasses_repository: DeleteGlassesRepository
    delete_image_storage: DeleteImageStorage

    def delete(self, params: DeleteGlassesParams) -> None:
        self.delete_glasses_repository.delete(
            DeleteGlassesRepositoryParams(
                glasses_id=params['glasses_id']
            ))
        self.delete_image_storage.delete_image(
            DeleteImageRepositoryParams(
                glasses_id=params['glasses_id']
            ))
