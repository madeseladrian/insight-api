from src.domain.features import UpdateGlasses
from src.domain.params import UpdateGlassesParams


class UpdateGlassesSpy(UpdateGlasses):
    params: UpdateGlassesParams

    def update(self, params: UpdateGlassesParams) -> None:
        self.params = params
