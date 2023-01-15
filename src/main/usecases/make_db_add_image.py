from ...domain.features import AddImage
from ...data.usecases import DbAddImage
from ...infra.db.firebase.glasses import GlassesImageStorageRepository


def make_db_add_image() -> AddImage:
    glasses_image_storage_repository = GlassesImageStorageRepository()
    return DbAddImage(add_image_storage=glasses_image_storage_repository)
