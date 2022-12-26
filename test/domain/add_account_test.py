from inspect import isabstract
import pytest
from unittest.mock import patch

from src.domain.features import AddAccount
from src.domain.params import AddAccountParams


class TestAddAccount:
    def test_1_should_AddAccount_is_an_abstract_class(self):
        assert isabstract(AddAccount)

    @patch.multiple(AddAccount, __abstractmethods__=set())
    def test_2_should_AddAccount_raise_a_NotImplementedError_if_not_implemented(self):
        params = AddAccountParams(
          name='any_name',
          email='any_email@any.com',
          password='any_password'
        )
        add_account = AddAccount()

        with pytest.raises(NotImplementedError, match='Should implement method: add'):
            add_account.add(account=params)
