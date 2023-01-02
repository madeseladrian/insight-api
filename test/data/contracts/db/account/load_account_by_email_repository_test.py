from inspect import isabstract

from src.data.contracts.db.account import LoadAccountByEmailRepository


class TestLoadAccountByEmailRepository:
    def test_1_should_LoadAccountByEmailRepository_is_an_abstract_class(self):
        assert isabstract(LoadAccountByEmailRepository)
