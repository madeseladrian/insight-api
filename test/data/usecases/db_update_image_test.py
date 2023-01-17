from typing import Tuple

from src.data.usecases import DbUpdateImage

from ...domain.mocks import mock_add_image_params
from ..mocks.db.glasses import UpdateImageStorageSpy


class TestDbAddImages:
    # SetUp
    params = mock_add_image_params()

    SutTypes = Tuple[
        DbUpdateImage,
        UpdateImageStorageSpy
    ]

    def make_sut(self) -> SutTypes:
        update_image_repository_spy = UpdateImageStorageSpy()
        sut = DbUpdateImage(
            update_image_storage=update_image_repository_spy
        )
        return (
            sut,
            update_image_repository_spy
        )

    def test_1_should_call_UpdateImageStorage_with_correct_values(self):
        sut, update_image_repository_spy = self.make_sut()
        sut.update_image(self.params)

        assert update_image_repository_spy.params == self.params
