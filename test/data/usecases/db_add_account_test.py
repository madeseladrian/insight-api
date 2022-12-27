import pytest
from typing import Tuple
from unittest.mock import patch

from src.domain.params import AddAccountParams
from src.data.usecases import DbAddAccount

from ...domain.mocks import mock_add_account_params
from ..mocks.db.account import CheckAccountByEmailRepositorySpy
from ..mocks.cryptography import HasherSpy


class TestDbAddAccount:
    # SetUp
    params: AddAccountParams = mock_add_account_params()

    SutTypes = Tuple[
        DbAddAccount,
        CheckAccountByEmailRepositorySpy,
        HasherSpy
    ]

    def make_sut(self) -> SutTypes:
        check_account_by_email_repository_spy = CheckAccountByEmailRepositorySpy()
        hasher_spy = HasherSpy()
        sut = DbAddAccount(
            hasher=hasher_spy,
            check_account_by_email_repository=check_account_by_email_repository_spy,
        )
        return sut, check_account_by_email_repository_spy, hasher_spy

    def test_1_should_call_CheckAccountByEmailRepository_with_correct_email(self):
        sut, check_account_by_email_repository_spy, _ = self.make_sut()
        sut.add(self.params)

        assert check_account_by_email_repository_spy.email == self.params['email']

    def test_2_should_return_true_if_CheckAccountByEmailRepository_returns_false(self):
        sut, _, _ = self.make_sut()
        is_valid = sut.add(self.params)

        assert is_valid

    def test_3_should_return_false_if_CheckAccoutByEmailRepository_returns_true(self):
        sut, check_account_by_email_repository_spy, _ = self.make_sut()
        check_account_by_email_repository_spy.result = True
        is_valid = sut.add(self.params)

        assert not is_valid

    @patch('test.data.mocks.db.account.CheckAccountByEmailRepositorySpy.check_by_email')
    def test_4_should_return_an_error_if_CheckAccountByEmailRepository_throws(self, mocker):
        sut, _, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.add(self.params)

    def test_5_should_call_Hasher_with_correct_plaintext(self):
        sut, _, hasher_spy = self.make_sut()
        sut.add(self.params)

        assert hasher_spy.plaintext == self.params['password']
