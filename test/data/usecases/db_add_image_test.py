import pytest
from typing import Tuple
from unittest.mock import patch

from src.data.usecases import DbAddImage

from ...domain.mocks import mock_add_image_params
from ..mocks.db.glasses import AddImageStorageSpy


class TestDbAddImages:
    # SetUp
    params = mock_add_image_params()

    SutTypes = Tuple[
        DbAddImage,
        AddImageStorageSpy
    ]

    def make_sut(self) -> SutTypes:
        add_images_repository_spy = AddImageStorageSpy()
        sut = DbAddImage(
            add_image_storage=add_images_repository_spy
        )
        return (
            sut,
            add_images_repository_spy
        )

    def test_1_should_call_AddImageStorage_with_correct_values(self):
        sut, add_images_repository_spy = self.make_sut()
        sut.add_image(self.params)

        assert add_images_repository_spy.params == self.params

    @patch('test.data.mocks.db.glasses.AddImageStorageSpy.add_image')
    def test_2_should_throws_if_AddImageStorage_throws(self, mocker):
        sut, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.add_image(self.params)
