from faker import Faker
from mockfirestore import MockFirestore
import pytest

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
