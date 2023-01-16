from inspect import isabstract

from src.domain.features import GetGlasses


class TestGetGlasses:
    def test_1_should_GetGlasses_is_an_abstract_class(self):
        assert isabstract(GetGlasses)
