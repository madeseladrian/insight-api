from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db.glasses import GetGlassesRepository


class TestGetGlassesRepository:
    def test_1_should_GetGlassesRepository_is_an_abstract_class(self):
        assert isabstract(GetGlassesRepository)

    @patch.multiple(GetGlassesRepository, __abstractmethods__=set())
    def test_2_should_GetGlassesRepository_raise_a_NotImplementedError_if_not_implemented(self):
        get_glasses_repository = GetGlassesRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: get'):
            get_glasses_repository.get(user_id='any_id')
