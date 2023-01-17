from dataclasses import dataclass

from ...domain.features import UpdateImage
from ...domain.params import UpdateImageParams

from ..contracts.db.glasses import UpdateImageStorage


@dataclass
class DbUpdateImage(UpdateImage):
    update_image_storage: UpdateImageStorage

    def update_image(self, params: UpdateImageParams) -> None:
        self.update_image_storage.update_image(params)
