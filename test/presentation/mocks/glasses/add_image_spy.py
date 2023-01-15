from src.domain.features import AddImage
from src.domain.params import AddImageParams


class AddImageSpy(AddImage):
    params: AddImageParams

    def add_image(self, params: AddImageParams) -> None:
        self.params = params
