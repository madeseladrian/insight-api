from typing import Tuple
from faker import Faker
import pytest
from unittest.mock import patch

from src.data.usecases import DbLoadAccountByToken
from ..mocks.cryptography import DecrypterSpy


class TestDbLoadAccountByToken:
    # SetUp
    faker = Faker()
    token = faker.uuid4()
    role = faker.word()

    SutTypes = Tuple[
        DbLoadAccountByToken,
        DecrypterSpy
    ]

    def make_sut(self) -> SutTypes:
        decrypter_spy = DecrypterSpy()
        sut = DbLoadAccountByToken(
            decrypter=decrypter_spy
        )
        return sut, decrypter_spy

    def test_1_should_call_Decrypter_with_correct_token(self):
        sut, decrypter_spy = self.make_sut()
        sut.load(access_token=self.token, role=self.role)

        assert decrypter_spy.token == self.token

    def test_2_should_return_None_if_Decrypter_returns_None(self):
        sut, decrypter_spy = self.make_sut()
        decrypter_spy.user_id = None
        account = sut.load(access_token=self.token, role=self.role)

        assert account is None

    @patch('test.data.mocks.cryptography.DecrypterSpy.decrypt')
    def test_3_should_throw_if_Decrypter_throws(self, mocker):
        sut, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.load(access_token=self.token, role=self.role)
