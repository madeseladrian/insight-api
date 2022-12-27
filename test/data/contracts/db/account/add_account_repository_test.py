from inspect import isabstract

from src.data.contracts.db.account import AddAccountRepository


class TestAddAccountRepository:
    def test_1_should_AddAccountRepository_is_an_abstract_class(self):
        assert isabstract(AddAccountRepository)
