from inspect import isabstract

from src.domain.features import LoadAccountByToken


class TestLoadAccountByToken:
    def test_1_should_LoadAccountByToken_is_an_abstract_class(self):
        assert isabstract(LoadAccountByToken)
