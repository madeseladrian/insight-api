from inspect import isabstract

from src.domain.features import AddAccount


class TestAddAccount:
    def test_1_should_AddAccount_is_an_abstract_class(self):
        assert isabstract(AddAccount)
