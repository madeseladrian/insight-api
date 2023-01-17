from inspect import isabstract
from io import BytesIO
import pytest
from unittest.mock import patch

from src.data.contracts.db.glasses import UpdateImageStorage
from src.data.params import UpdateImageRepositoryParams


class TestUpdateImageStorage:
    def test_1_should_UpdateImageStorage_is_an_abstract_class(self):
        assert isabstract(UpdateImageStorage)

    @patch.multiple(UpdateImageStorage, __abstractmethods__=set())
    def test_2_should_UpdateImageStorage_raise_a_NotImplementedError_if_not_implemented(self):
        update_image_storage = UpdateImageStorage()
        params = UpdateImageRepositoryParams(
            content_type='any_type',
            glasses_id='any_id',
            image=BytesIO()
        )
        with pytest.raises(NotImplementedError, match='Should implement method: update_image'):
            update_image_storage.update_image(params)
