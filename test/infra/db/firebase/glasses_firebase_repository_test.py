from faker import Faker
from mockfirestore import MockFirestore
import pytest
from unittest.mock import patch

from src.data.params import (
    GetGlassesRepositoryParams,
    DeleteGlassesRepositoryParams,
    UpdateGlassesRepositoryParams
)
from src.infra.db.firebase import firebase_helper
from src.infra.db.firebase.glasses import GlassesFirebaseRepository

from ....domain.mocks import mock_add_glasses_params


class TestGlassesFirebaseRepository:
    # SetUp
    faker = Faker()
    params = mock_add_glasses_params()
    firebase_helper.connect(MockFirestore())

    def make_sut(self) -> GlassesFirebaseRepository:
        return GlassesFirebaseRepository()

    @pytest.fixture
    def clear_db(self) -> None:
        firebase_helper.client_firebase.reset()

    def test_1_should_return_true_on_success(self, clear_db):
        sut = self.make_sut()
        is_valid = sut.add(dict(self.params))

        assert is_valid

    @patch('src.infra.db.firebase.glasses.GlassesFirebaseRepository.add')
    def test_2_should_return_false_on_fail(self, mocker, clear_db):
        mocker.return_value = False

        sut = self.make_sut()
        is_valid = sut.add(dict(self.params))

        assert is_valid is False

    def test_3_should_return_a_list_of_glasses_on_success(self, clear_db):
        sut = self.make_sut()
        collections = firebase_helper.get_document('glasses')
        collections.set(self.params)

        list_glasses = sut.get(GetGlassesRepositoryParams(id=self.params['user_id']))

        assert list_glasses['glasses'][0] == self.params

    def test_4_should_return_a_empty_list_of_glasses_on_fail(self, clear_db):
        sut = self.make_sut()

        list_glasses = sut.get(GetGlassesRepositoryParams(id=self.params['user_id']))

        assert list_glasses['glasses'] == []

    def test_5_should_delete_glasses_data_on_success(self, clear_db):
        sut = self.make_sut()
        collections = firebase_helper.get_document('glasses')
        collections.set(self.params)

        glasses = firebase_helper.get_collection('glasses').where(
            'glasses_id', '==', self.params['glasses_id']
        ).stream()
        glasses_data = [f.to_dict() for f in glasses][0]

        assert glasses_data

        sut.delete(DeleteGlassesRepositoryParams(
            glasses_id=self.params['glasses_id']
        ))

        glasses = firebase_helper.get_collection('glasses').where(
            'glasses_id', '==', self.params['glasses_id']
        ).stream()
        glasses_data = [f.to_dict() for f in glasses]

        assert glasses_data == []

    def test_6_should_update_glasses_data_on_success(self, clear_db):
        sut = self.make_sut()
        collections = firebase_helper.get_document('glasses')
        collections.set(self.params)

        glasses = firebase_helper.get_collection('glasses').where(
            'glasses_id', '==', self.params['glasses_id']
        ).stream()
        glasses_data = [f.to_dict() for f in glasses][0]

        assert glasses_data['glasses_id'] == self.params['glasses_id']

        updated_data = {'model': 'updated_model'}
        sut.update(UpdateGlassesRepositoryParams(
            glasses_id=self.params['glasses_id'],
            data=updated_data
        ))

        glasses = firebase_helper.get_collection('glasses').where(
            'glasses_id', '==', self.params['glasses_id']
        ).stream()
        glasses_data = [f.to_dict() for f in glasses][0]

        assert glasses_data['model'] == updated_data['model']
