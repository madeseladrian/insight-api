from src.domain.features import UpdateImage
from src.domain.params import UpdateImageParams


class UpdateImageSpy(UpdateImage):
    params: UpdateImageParams

    def update_image(self, params: UpdateImageParams) -> None:
        self.params = params
