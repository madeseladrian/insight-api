from inspect import isabstract

from src.domain.features import UpdateGlasses


class TestUpdateGlasses:
    def test_1_should_UpdateGlasses_is_an_abstract_class(self):
        assert isabstract(UpdateGlasses)
