from ...domain.features import UpdateGlasses
from ...data.usecases import DbUpdateGlasses
from ...infra.db.firebase.glasses import GlassesFirebaseRepository


def make_db_update_glasses() -> UpdateGlasses:
    glasses_firebase_repository = GlassesFirebaseRepository()
    return DbUpdateGlasses(
        update_glasses_repository=glasses_firebase_repository
    )
