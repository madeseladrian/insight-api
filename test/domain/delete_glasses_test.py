from inspect import isabstract

from src.domain.features import DeleteGlasses


class TestDeleteGlasses:
    def test_1_should_DeleteGlasses_is_an_abstract_class(self):
        assert isabstract(DeleteGlasses)
