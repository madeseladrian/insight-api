from inspect import isabstract

from src.domain.features import UpdateImage


class TestUpdateImage:
    def test_1_should_UpdateImage_is_an_abstract_class(self):
        assert isabstract(UpdateImage)
