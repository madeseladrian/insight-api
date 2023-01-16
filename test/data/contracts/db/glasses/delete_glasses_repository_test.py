from inspect import isabstract

from src.data.contracts.db.glasses import DeleteGlassesRepository


class TestDeleteGlassesRepository:
    def test_1_should_DeleteGlassesRepository_is_an_abstract_class(self):
        assert isabstract(DeleteGlassesRepository)
