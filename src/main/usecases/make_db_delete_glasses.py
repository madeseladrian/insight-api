from ...domain.features import DeleteGlasses
from ...data.usecases import DbDeleteGlasses
from ...infra.db.firebase.glasses import (
    GlassesFirebaseRepository,
    GlassesImageStorageRepository
)

def make_db_delete_glasses() -> DeleteGlasses:
    glasses_firebase_repository = GlassesFirebaseRepository()
    glasses_image_storage_repository = GlassesImageStorageRepository()

    return DbDeleteGlasses(
        delete_glasses_repository=glasses_firebase_repository,
        delete_image_storage=glasses_image_storage_repository
    )
