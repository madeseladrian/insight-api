from src.domain.features import GetGlasses
from src.domain.params import GetGlassesParams, GetGlassesResult


class GetGlassesSpy(GetGlasses):
    params: GetGlassesParams
    result: GetGlassesResult = GetGlassesResult(glasses=[{'any_key': 'any_value'}])

    def get(self, params: GetGlassesParams) -> GetGlassesResult:
        self.params = params
        return self.result
