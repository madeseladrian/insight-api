from dataclasses import dataclass
from firebase_admin import storage
from typing import BinaryIO, Tuple
import uuid

from .....data.contracts.db.glasses import AddImageStorage


@dataclass
class GlassesImageStorageRepository(AddImageStorage):
    def add_image(self, image: BinaryIO, image_type: str) -> Tuple[str, str]:
        glasses_id = str(uuid.uuid4())
        bucket = storage.bucket()
        blob = bucket.blob(glasses_id)
        blob.upload_from_file(image, content_type=image_type)
        blob.make_public()

        return blob.public_url, glasses_id
