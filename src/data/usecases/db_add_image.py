from dataclasses import dataclass

from ...domain.features import AddImage
from ...domain.params import AddImageParams, AddImageResult

from ..contracts.db.glasses import AddImageStorage


@dataclass
class DbAddImage(AddImage):
    add_image_storage: AddImageStorage

    def add_image(self, params: AddImageParams) -> AddImageResult:
        return self.add_image_storage.add_image(params)
