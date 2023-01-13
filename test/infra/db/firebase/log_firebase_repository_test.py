from faker import Faker
from mockfirestore import MockFirestore

from src.infra.db.firebase.log import LogFirebaseRepository
from src.infra.db.firebase import firebase_helper


class TestLogFirebaseRepository:
    faker = Faker()
    error = faker.word()
    firebase_helper.connect(MockFirestore())

    def make_sut(self) -> LogFirebaseRepository:
        return LogFirebaseRepository()

    def test_1_should_create_an_error_log_on_success(self):
        sut = self.make_sut()
        sut.log_error(self.error)

        log_error = firebase_helper.get_collection('logs').where(
            'log', '==', self.error
        ).stream()
        errors = [e.to_dict() for e in log_error]

        count = len(errors)
        log = errors[0]

        assert count == 1
        assert log['log'] == self.error
