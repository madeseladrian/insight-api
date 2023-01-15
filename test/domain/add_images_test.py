from inspect import isabstract

from src.domain.features import AddImages


class TestAddAccount:
    def test_1_should_AddImages_is_an_abstract_class(self):
        assert isabstract(AddImages)
