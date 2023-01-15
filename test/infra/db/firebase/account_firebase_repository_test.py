from faker import Faker
from mockfirestore import MockFirestore
import pytest
from unittest.mock import patch

from src.infra.db.firebase import firebase_helper
from src.infra.db.firebase.account import AccountFirebaseRepository
from ....domain.mocks import mock_add_account_params


class TestAccountFirebaseRepository:
    # SetUp
    faker = Faker()
    access_token = faker.uuid4()
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
        collections = firebase_helper.get_document('users')
        collections.set(dict(self.params))
        exists = sut.check_by_email(self.params['email'])

        assert exists

    @patch('src.infra.db.firebase.account.AccountFirebaseRepository.check_by_email')
    def test_4_should_return_false_if_email_is_not_valid(self, mocker, clear_db):
        mocker.return_value = False
        sut = self.make_sut()
        collections = firebase_helper.get_document('users')
        collections.set(dict(self.params))
        exists = sut.check_by_email(self.params['email'])

        assert exists is False

    def test_5_should_return_an_account_on_success(self, clear_db):
        sut = self.make_sut()
        collections = firebase_helper.get_document('users')
        collections.set(dict(self.params))
        account = sut.load_by_email(self.params['email'])

        assert account
        assert account['id']
        assert account['name'] == self.params['name']
        assert account['password'] == self.params['password']

    def test_6_should_return_None_if_load_by_email_fails(self, clear_db):
        sut = self.make_sut()
        account = sut.load_by_email(self.params['email'])

        assert account is None

    def test_7_should_update_account_access_token_on_success(self, clear_db):
        sut = self.make_sut()
        collections = firebase_helper.get_document('users')
        collections.set(dict(self.params))
        fake_account = firebase_helper.get_collection('users').where(
            'id', '==', self.params['id']
        ).stream()
        fake_account = [f.to_dict() for f in fake_account][0]

        assert not fake_account.get('access_token')

        sut.update_access_token(user_id=fake_account['id'], token=self.access_token)
        account = firebase_helper.get_collection('users').where(
            'id', '==', fake_account['id']
        ).stream()
        account = [a.to_dict() for a in account][0]

        assert account
        assert account['access_token'] == self.access_token

    def test_8_should_return_an_id_on_success(self, clear_db):
        sut = self.make_sut()
        collections = firebase_helper.get_document('users')
        collections.set({
            'id': self.params['id'],
            'name': self.params['name'],
            'email': self.params['email'],
            'password': self.params['password'],
            'access_token': self.access_token
        })
        user_id = sut.load_by_token(self.access_token)

        assert user_id['id'] == self.params['id']

    def test_9_should_return_None_if_load_by_token_fails(self, clear_db):
        sut = self.make_sut()
        user_id = sut.load_by_token(self.access_token)

        assert user_id is None
