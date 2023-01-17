from dataclasses import dataclass

from .....data.contracts.db.glasses import (
    AddGlassesRepository,
    DeleteGlassesRepository,
    GetGlassesRepository
)
from .....data.params import (
    AddGlassesRepositoryParams,
    AddGlassesRepositoryResult,
    DeleteGlassesRepositoryParams,
    GetGlassesRepositoryParams,
    GetGlassesRepositoryResult
)
from ..firebase_helper import firebase_helper


@dataclass
class GlassesFirebaseRepository(
    AddGlassesRepository,
    DeleteGlassesRepository,
    GetGlassesRepository
):

    def add(self, data: AddGlassesRepositoryParams) -> AddGlassesRepositoryResult:
        account = firebase_helper.get_document('glasses')
        account.set(data)

        return bool(account.get().to_dict())

    def get(self, params: GetGlassesRepositoryParams) -> GetGlassesRepositoryResult:
        user_id = params['id']

        glasses = firebase_helper.get_collection('glasses').where(
            'user_id', '==', user_id
        ).stream()
        list_glasses = [g.to_dict() for g in glasses]

        return GetGlassesRepositoryResult(glasses=list_glasses)

    def delete(self, params: DeleteGlassesRepositoryParams) -> None:
        glasses_id = params['glasses_id']

        glasses = firebase_helper.get_collection('glasses').where(
            'glasses_id', '==', glasses_id
        ).stream()

        document_id = [doc.id for doc in glasses][0]
        firebase_helper.get_collection('glasses').document(document_id).delete()
