from src.data.contracts.db.glasses import UpdateGlassesRepository
from src.data.params import UpdateGlassesRepositoryParams


class UpdateGlassesRepositorySpy(UpdateGlassesRepository):
    data: UpdateGlassesRepositoryParams

    def update(self, data: UpdateGlassesRepositoryParams) -> None:
        self.data = data
