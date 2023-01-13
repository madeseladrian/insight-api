from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db.log import LogErrorRepository


class TestAddAccountRepository:
    def test_1_should_LogErrorRepository_is_an_abstract_class(self):
        assert isabstract(LogErrorRepository)

    @patch.multiple(AddAccountRepository, __abstractmethods__=set())
    def test_2_should_AddAccountRepository_raise_a_NotImplementedError_if_not_implemented(self):
        add_account_repository = AddAccountRepository()

        with pytest.raises(NotImplementedError, match='Should implement method: add'):
            add_account_repository.add(data={})