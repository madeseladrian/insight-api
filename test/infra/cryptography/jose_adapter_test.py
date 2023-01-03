from unittest.mock import patch

from src.infra.cryptography import JoseAdapter


class TestJoseAdapter:

    def make_sut(self) -> JoseAdapter:
        return JoseAdapter(
            algorithm='HS256',
            expire_in_days=1,
            key='any_key'
        )

    @patch('src.infra.cryptography.JoseAdapter.encrypt')
    def test_1_should_call_encrypt_with_correct_value(self, mocker):
        sut = self.make_sut()
        sut.encrypt('any_value')

        mocker.assert_called_once_with('any_value')
