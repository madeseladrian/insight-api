from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db.glasses import UpdateGlassesRepository


class TestUpdateGlassesRepository:
    def test_1_should_UpdateGlassesRepository_is_an_abstract_class(self):
        assert isabstract(UpdateGlassesRepository)

    @patch.multiple(UpdateGlassesRepository, __abstractmethods__=set())
    def test_2_should_UpdateGlassesRepository_raise_a_NotImplementedError_if_not_implemented(self):
        update_glasses_repository = UpdateGlassesRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: update'):
            update_glasses_repository.update({})
