from dataclasses import dataclass

from .....data.contracts.db.glasses import (
    AddGlassesRepository,
    GetGlassesRepository
)
from .....data.params import (
    AddGlassesRepositoryParams,
    AddGlassesRepositoryResult,
    GetGlassesRepositoryParams,
    GetGlassesRepositoryResult
)
from ..firebase_helper import firebase_helper


@dataclass
class GlassesFirebaseRepository(
    AddGlassesRepository,
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
