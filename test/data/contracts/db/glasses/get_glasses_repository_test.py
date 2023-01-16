from inspect import isabstract

from src.data.contracts.db.glasses import GetGlassesRepository


class TestGetGlassesRepository:
    def test_1_should_GetGlassesRepository_is_an_abstract_class(self):
        assert isabstract(GetGlassesRepository)
