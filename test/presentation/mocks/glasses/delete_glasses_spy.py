from src.domain.features import DeleteGlasses
from src.domain.params import DeleteGlassesParams


class DeleteGlassesSpy(DeleteGlasses):
    params: DeleteGlassesParams

    def delete(self, params: DeleteGlassesParams) -> None:
        self.params = params
