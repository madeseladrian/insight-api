from src.data.contracts.db.glasses import DeleteGlassesRepository
from src.data.params import DeleteGlassesRepositoryParams


class DeleteGlassesRepositorySpy(DeleteGlassesRepository):
    params: DeleteGlassesRepositoryParams

    def delete(self, params: DeleteGlassesRepositoryParams) -> None:
        self.params = params
