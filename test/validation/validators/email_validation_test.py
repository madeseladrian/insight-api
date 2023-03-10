from faker import Faker
import pytest
from typing import Tuple
from unittest.mock import patch

from src.presentation.errors import InvalidParamError
from src.validation.validators import EmailValidation

from ..mocks import EmailValidatorSpy


class TestEmailValidation:
    # SetUp
    faker = Faker()
    field_name: str = faker.word()

    SutTypes = Tuple[EmailValidation, EmailValidatorSpy]

    def make_sut(self) -> SutTypes:
        email_validation_spy = EmailValidatorSpy()
        sut = EmailValidation(
          field_name=self.field_name,
          email_validator=email_validation_spy
        )
        return sut, email_validation_spy

    def test_1_should_call_EmailValidator_with_correct_email(self):
        sut, email_validator_spy = self.make_sut()
        email = self.faker.email()
        sut.validate({self.field_name: email})

        assert email_validator_spy.email == email

    def test_2_should_return_an_error_if_EmailValidator_returns_false(self):
        sut, email_validator_spy = self.make_sut()
        email_validator_spy.is_email_valid = False
        email = self.faker.email()
        error = sut.validate({self.field_name: email})

        assert error == InvalidParamError(self.field_name)

    @patch('src.validation.validators.EmailValidation.validate')
    def test_3_should_throw_if_EmailValidator_throws(self, mocker):
        sut, email_validator_spy = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.validate(email_validator_spy)
