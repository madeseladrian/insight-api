import pytest
from typing import Tuple
from unittest.mock import patch

from src.data.usecases import DbAddGlasses

from ...domain.mocks import mock_add_glasses_params, mock_add_glasses_repository_params
from ..mocks.db.glasses import AddImageStorageSpy, AddGlassesRepositorySpy


class TestDbAddGlasses:
    # SetUp
    params = mock_add_glasses_params()

    SutTypes = Tuple[
        DbAddGlasses,
        AddImageStorageSpy,
        AddGlassesRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        add_image_storage_spy = AddImageStorageSpy()
        add_glasses_repository_spy = AddGlassesRepositorySpy()
        sut = DbAddGlasses(
            add_image_storage=add_image_storage_spy,
            add_glasses_repository=add_glasses_repository_spy
        )
        return (
            sut,
            add_image_storage_spy,
            add_glasses_repository_spy
        )

    def test_1_should_call_AddImageStorage_with_correct_values(self):
        sut, add_image_storage_spy, _ = self.make_sut()
        sut.add(self.params)

        assert add_image_storage_spy.image == self.params['image']
        assert add_image_storage_spy.image_type == self.params['image_type']

    @patch('test.data.mocks.db.glasses.AddImageStorageSpy.add_image')
    def test_2_should_throws_if_AddImageStorage_throws(self, mocker):
        sut, _, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.add(self.params)

    def test_3_should_call_AddGlassesRepository_with_correct_values(self):
        sut, add_image_storage_spy, add_glasses_repository_spy = self.make_sut()
        sut.add(self.params)
        url_image = add_image_storage_spy.url_image
        glasses_id = add_image_storage_spy.glasses_id
        params_repository = mock_add_glasses_repository_params(url_image=url_image, glasses_id=glasses_id)

        assert add_glasses_repository_spy.data == params_repository

    def test_4_should_return_true_if_AddGlassesRepository_add_data(self):
        sut, _, _ = self.make_sut()
        is_valid = sut.add(self.params)

        assert is_valid

    def test_5_should_return_false_if_AddGlassesRepository_does_not_add_data(self):
        sut, _, add_glasses_repository_spy = self.make_sut()
        add_glasses_repository_spy.result = False
        is_valid = sut.add(self.params)

        assert not is_valid

    @patch('test.data.mocks.db.glasses.AddGlassesRepositorySpy.add')
    def test_6_should_return_an_error_if_AddGlassesRepository_throws(self, mocker):
        sut, _, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.add(self.params)
