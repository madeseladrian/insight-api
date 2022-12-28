from unittest.mock import patch

from src.infra.cryptography import BCryptAdapter


class TestBCryptAdapter:

    def make_sut(self) -> BCryptAdapter:
        return BCryptAdapter()

    # Hasher

    @patch('src.infra.cryptography.BCryptAdapter.get_password_hash')
    def test_1_should_call_hash_with_correct_value(self, mocker):
        sut = self.make_sut()
        sut.get_password_hash('any_value')

        mocker.assert_called_once_with('any_value')

    def test_2_should_return_a_string_on_hash_success(self):
        sut = self.make_sut()
        hashed_password = sut.get_password_hash('any_value')

        assert isinstance(hashed_password, str)
