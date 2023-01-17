from dataclasses import dataclass
from firebase_admin import storage
import uuid

from .....data.contracts.db.glasses import (
    AddImageStorage,
    DeleteImageStorage
)
from .....data.params import (
    AddImageRepositoryParams,
    AddImageRepositoryResult,
    DeleteImageRepositoryParams
)


@dataclass
class GlassesImageStorageRepository(
    AddImageStorage,
    DeleteImageStorage
):
    def add_image(self, params: AddImageRepositoryParams) -> AddImageRepositoryResult:
        glasses_id = str(uuid.uuid4())
        bucket = storage.bucket()
        blob = bucket.blob(glasses_id)
        blob.upload_from_file(params['image'], content_type=params['content_type'])
        blob.make_public()

        return AddImageRepositoryResult(
            glasses_id=glasses_id,
            url_image=blob.public_url
        )

    def delete_image(self, params: DeleteImageRepositoryParams) -> None:
        glasses_id = params['glasses_id']
        bucket = storage.bucket()
        blob = bucket.blob(glasses_id)
        blob.delete()
