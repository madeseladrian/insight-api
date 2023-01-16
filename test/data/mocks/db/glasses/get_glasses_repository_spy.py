from src.data.params import GetGlassesRepositoryParams, GetGlassesRepositoryResult
from src.data.contracts.db.glasses import GetGlassesRepository

class GetGlassesRepositorySpy(GetGlassesRepository):
    params: GetGlassesRepositoryParams
    result: GetGlassesRepositoryResult = GetGlassesRepositoryResult(
        glasses=[{'any_key': 'any_value'}]
    )

    def get(self, params: GetGlassesRepositoryParams) -> GetGlassesRepositoryResult:
        self.params = params
        return self.result
