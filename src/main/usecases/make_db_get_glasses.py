from ...domain.features import GetGlasses
from ...data.usecases import DbGetGlasses
from ...infra.db.firebase.glasses import GlassesFirebaseRepository


def make_db_get_glasses() -> GetGlasses:
    glasses_firebase_repository = GlassesFirebaseRepository()
    return DbGetGlasses(
        get_glasses_repository=glasses_firebase_repository
    )
