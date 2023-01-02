from unittest.mock import patch
from src.utils import EmailValidatorAdapter


class TestEmailValidatorAdapter:

    def make_sut(self) -> EmailValidatorAdapter:
        return EmailValidatorAdapter()

    @patch('src.utils.EmailValidatorAdapter.is_valid')
    def test_1_should_call_validator_with_correct_email(self, mocker):
        sut = self.make_sut()
        sut.is_valid('any_email')

        mocker.assert_called_once_with('any_email')

    