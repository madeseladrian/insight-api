import pytest
from typing import Tuple
from unittest.mock import patch

from src.data.usecases import DbAddGlasses

from ...domain.mocks import mock_add_glasses_params
from ..mocks.db.glasses import AddGlassesRepositorySpy


class TestDbAddGlasses:
    # SetUp
    params = mock_add_glasses_params()

    SutTypes = Tuple[
        DbAddGlasses,
        AddGlassesRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        add_glasses_repository_spy = AddGlassesRepositorySpy()
        sut = DbAddGlasses(
            add_glasses_repository=add_glasses_repository_spy
        )
        return (
            sut,
            add_glasses_repository_spy
        )

    def test_1_should_call_AddGlassesRepository_with_correct_values(self):
        sut, add_glasses_repository_spy = self.make_sut()
        sut.add(self.params)

        assert add_glasses_repository_spy.data == self.params

    def test_2_should_return_true_if_AddGlassesRepository_add_data(self):
        sut, _ = self.make_sut()
        is_valid = sut.add(self.params)

        assert is_valid

    def test_3_should_return_false_if_AddGlassesRepository_does_not_add_data(self):
        sut, add_glasses_repository_spy = self.make_sut()
        add_glasses_repository_spy.result = False
        is_valid = sut.add(self.params)

        assert not is_valid

    @patch('test.data.mocks.db.glasses.AddGlassesRepositorySpy.add')
    def test_4_should_return_an_error_if_AddGlassesRepository_throws(self, mocker):
        sut, _ = self.make_sut()
        mocker.side_effect = Exception

        with pytest.raises(Exception):
            sut.add(self.params)
