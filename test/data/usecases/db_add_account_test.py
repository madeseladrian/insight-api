from typing import Tuple

from src.domain.params import AddAccountParams
from src.data.usecases import DbAddAccount

from ...domain.mocks import mock_add_account_params
from ..mocks.db.account import CheckAccountByEmailRepositorySpy


class TestDbAddAccount:
    # SetUp
    params: AddAccountParams = mock_add_account_params()

    SutTypes = Tuple[
        DbAddAccount,
        CheckAccountByEmailRepositorySpy,
    ]

    def make_sut(self) -> SutTypes:
        check_account_by_email_repository_spy = CheckAccountByEmailRepositorySpy()
        sut = DbAddAccount(
            check_account_by_email_repository=check_account_by_email_repository_spy,
        )
        return sut, check_account_by_email_repository_spy

    def test_1_should_call_CheckAccountByEmailRepository_with_correct_email(self):
        sut, check_account_by_email_repository_spy = self.make_sut()
        sut.add(self.params)

        assert check_account_by_email_repository_spy.email == self.params['email']

    def test_2_should_return_true_if_CheckAccountByEmailRepository_returns_false(self):
        sut, _ = self.make_sut()
        is_valid = sut.add(self.params)

        assert is_valid
