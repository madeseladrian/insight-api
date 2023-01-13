from src.data.contracts.db.glasses import AddGlassesRepository
from src.data.params import AddGlassesRepositoryParams, AddAccountRepositoryResult


class AddGlassesRepositorySpy(AddGlassesRepository):
    data: AddGlassesRepositoryParams
    result: AddAccountRepositoryResult = True

    def add(self, data: AddGlassesRepositoryParams) -> AddAccountRepositoryResult:
        self.data = data
        return self.result
