from inspect import isabstract

from src.data.contracts.db.glasses import AddGlassesRepository


class TestAddGlassesRepository:
    def test_1_should_AddGlassesRepository_is_an_abstract_class(self):
        assert isabstract(AddGlassesRepository)
