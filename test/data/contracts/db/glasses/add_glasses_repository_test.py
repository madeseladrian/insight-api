from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db.glasses import AddGlassesRepository


class TestAddGlassesRepository:
    def test_1_should_AddGlassesRepository_is_an_abstract_class(self):
        assert isabstract(AddGlassesRepository)

    @patch.multiple(AddGlassesRepository, __abstractmethods__=set())
    def test_2_should_AddGlassesRepository_raise_a_NotImplementedError_if_not_implemented(self):
        add_glasses_repository = AddGlassesRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: add'):
            add_glasses_repository.add(data={})
