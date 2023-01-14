from dataclasses import dataclass
from typing import Any

from ...domain.features import AddGlasses
from ...domain.params import AddGlassesParams

from ..contracts.db.glasses import AddImageStorage, AddGlassesRepository
from ..params import AddGlassesRepositoryParams

@dataclass
class DbAddGlasses(AddGlasses):
    add_image_storage: AddImageStorage
    add_glasses_repository: AddGlassesRepository

    def add(self, data: AddGlassesParams) -> Any:
        url_image, glasses_id = self.add_image_storage.add_image(image=data['image'], image_type=data['image_type'])
        params = AddGlassesRepositoryParams(
            url_image=url_image,
            glasses_id=glasses_id,
            user_id=data['user_id'],
            model=data['model'],
            format=data['format'],
            gender=data['gender'],
            public=data['public'],
            category=data['category'],
            frame_color=data['frame_color'],
            lens_color=data['lens_color'],
            size_lens=data['size_lens'],
            size_bridge=data['size_bridge'],
            height_frame=data['height_frame'],
            size_temples=data['size_temples'],
            price=data['price'],
            additional_info=data['additional_info']
        )
        return self.add_glasses_repository.add(params)
