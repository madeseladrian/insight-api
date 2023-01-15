from ...domain.features import AddGlasses
from ...data.usecases import DbAddGlasses
from ...infra.db.firebase.glasses import GlassesFirebaseRepository


def make_db_add_glasses() -> AddGlasses:
    glasses_firebase_repository = GlassesFirebaseRepository()
    return DbAddGlasses(
        add_glasses_repository=glasses_firebase_repository
    )
