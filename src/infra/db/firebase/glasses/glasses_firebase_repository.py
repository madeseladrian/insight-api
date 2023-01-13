from dataclasses import dataclass

from .....data.contracts.db.glasses import AddGlassesRepository
from .....data.params import AddGlassesRepositoryParams, AddGlassesRepositoryResult

from ..firebase_helper import firebase_helper


@dataclass
class GlassesFirebaseRepository(AddGlassesRepository):

    def add(self, data: AddGlassesRepositoryParams) -> AddGlassesRepositoryResult:
        account = firebase_helper.get_document('glasses')
        account.set(data)

        return bool(account.get().to_dict())
