from src.data.contracts.db.glasses import AddGlassesRepository
from src.data.params import AddGlassesRepositoryParams


class AddGlassesRepositorySpy(AddGlassesRepository):
    data: AddGlassesRepositoryParams

    def add(self, data: AddGlassesRepositoryParams) -> None:
        self.data = data
