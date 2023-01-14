from src.domain.features import AddGlasses
from src.domain.params import AddGlassesParams


class AddGlassesSpy(AddGlasses):
    params: AddGlassesParams

    def add(self, params: AddGlassesParams) -> None:
        self.params = params
