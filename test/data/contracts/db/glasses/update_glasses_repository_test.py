from inspect import isabstract

from src.data.contracts.db.glasses import UpdateGlassesRepository


class TestUpdateGlassesRepository:
    def test_1_should_UpdateGlassesRepository_is_an_abstract_class(self):
        assert isabstract(UpdateGlassesRepository)
