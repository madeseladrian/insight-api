from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db.glasses import DeleteGlassesRepository
from src.data.params import DeleteGlassesRepositoryParams


class TestDeleteGlassesRepository:
    def test_1_should_DeleteGlassesRepository_is_an_abstract_class(self):
        assert isabstract(DeleteGlassesRepository)

    @patch.multiple(DeleteGlassesRepository, __abstractmethods__=set())
    def test_2_should_DeleteGlassesRepository_raise_a_NotImplementedError_if_not_implemented(self):
        params = DeleteGlassesRepositoryParams(glass_id='any_id')
        delete_glasses_repository = DeleteGlassesRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: delete'):
            delete_glasses_repository.delete(params)
