from faker import Faker
from mockfirestore import MockFirestore
import pytest
from unittest.mock import patch

from src.infra.db.firebase.account import (
    AccountFirebaseRepository,
    firebase_helper
)
from ....domain.mocks import mock_add_account_params


class TestAccountMongoRepository:
    # SetUp
    faker = Faker()
    params = mock_add_account_params()
    firebase_helper.connect(MockFirestore())

    def make_sut(self) -> AccountFirebaseRepository:
        return AccountFirebaseRepository()

    @pytest.fixture
    def clear_db(self) -> None:
        firebase_helper.client_firebase.reset()

    def test_1_should_return_true_on_success(self, clear_db):
        sut = self.make_sut()
        is_valid = sut.add(dict(self.params))

        assert is_valid

    @patch('src.infra.db.firebase.account.AccountFirebaseRepository.add')
    def test_2_should_return_false_on_fail(self, mocker, clear_db):
        mocker.return_value = False

        sut = self.make_sut()
        is_valid = sut.add(dict(self.params))

        assert is_valid is False

    def test_3_should_return_true_if_email_is_valid(self, clear_db):
        sut = self.make_sut()
        collections = firebase_helper.get_document()
        collections.set(dict(self.params))
        exists = sut.check_by_email(self.params['email'])

        assert exists
