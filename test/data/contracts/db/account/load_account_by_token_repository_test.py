from inspect import isabstract

from src.data.contracts.db.account import LoadAccountByTokenRepository


class TestLoadAccountByEmailRepository:
    def test_1_should_LoadAccountByTokenRepository_is_an_abstract_class(self):
        assert isabstract(LoadAccountByTokenRepository)
