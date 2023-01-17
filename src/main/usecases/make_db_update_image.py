from ...domain.features import UpdateImage
from ...data.usecases import DbUpdateImage
from ...infra.db.firebase.glasses import GlassesImageStorageRepository


def make_db_update_image() -> UpdateImage:
    glasses_image_storage_repository = GlassesImageStorageRepository()
    return DbUpdateImage(update_image_storage=glasses_image_storage_repository)
