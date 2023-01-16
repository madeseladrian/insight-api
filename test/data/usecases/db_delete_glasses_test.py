from faker import Faker
import pytest
from typing import Tuple
from unittest.mock import patch

from src.domain.params import DeleteGlassesParams
from src.data.usecases import DbDeleteGlasses

from ..mocks.db.glasses import (
    DeleteGlassesRepositorySpy,
    DeleteImageStorageSpy
)


class TestDbAddGlasses:
    # SetUp
    faker = Faker()
    params = DeleteGlassesParams(glasses_id=faker.uuid4())

    SutTypes = Tuple[
        DbDeleteGlasses,
        DeleteGlassesRepositorySpy,
        DeleteImageStorageSpy
    ]

    def make_sut(self) -> SutTypes:
        delete_glasses_repository_spy = DeleteGlassesRepositorySpy()
        delete_image_storage_spy = DeleteImageStorageSpy()
        sut = DbDeleteGlasses(
            delete_glasses_repository=delete_glasses_repository_spy,
            delete_image_storage=delete_image_storage_spy
        )
        return (
            sut,
            delete_glasses_repository_spy,
            delete_image_storage_spy
        )

    def test_1_should_call_DeleteGlassesRepository_with_correct_values(self):
        sut, delete_glasses_repository_spy, _ = self.make_sut()
        sut.delete(self.params)

        assert delete_glasses_repository_spy.params == self.params

    def test_2_should_return_None_if_DeleteGlassesRepository_succeeds(self):
        sut, _, _ = self.make_sut()
        params = sut.delete(self.params)

        assert params is None

    @patch('test.data.mocks.db.glasses.DeleteGlassesRepositorySpy.delete')
    def test_3_should_throws_if_DeleteGlassesRepository_throws(self, mocker):
        sut, _, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.delete(self.params)

    def test_4_should_call_DeleteImageStorage_with_correct_values(self):
        sut, _, delete_image_storage_spy = self.make_sut()
        sut.delete(self.params)

        assert delete_image_storage_spy.params == self.params

    def test_5_should_return_None_if_DeleteImageStorage_succeeds(self):
        sut, _, _ = self.make_sut()
        params = sut.delete(self.params)

        assert params is None

    @patch('test.data.mocks.db.glasses.DeleteImageStorageSpy.delete_image')
    def test_6_should_throws_if_DeleteImageStorage_throws(self, mocker):
        sut, _, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.delete(self.params)
