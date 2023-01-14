from dataclasses import dataclass
from firebase_admin import storage
from tempfile import SpooledTemporaryFile
import uuid

from .....data.contracts.db.glasses import AddGlassesRepository, AddImageStorage
from .....data.params import AddGlassesRepositoryParams, AddGlassesRepositoryResult

from ..firebase_helper import firebase_helper


@dataclass
class GlassesFirebaseRepository(AddGlassesRepository, AddImageStorage):

    def add(self, data: AddGlassesRepositoryParams) -> AddGlassesRepositoryResult:
        account = firebase_helper.get_document('glasses')
        account.set(data)

        return bool(account.get().to_dict())

    def add_image(self, image: SpooledTemporaryFile, image_type: str) -> str:
        bucket = storage.bucket()
        blob = bucket.blob(uuid.uuid4())
        blob.upload_from_file(image, content_type=image_type)
        blob.make_public()

        return blob.public_url
