from inspect import isabstract
from io import BytesIO
import pytest
from unittest.mock import patch

from src.data.contracts.db.glasses import AddImageStorage
from src.data.params import AddImageRepositoryParams


class TestAddImageStorage:
    def test_1_should_AddImageStorage_is_an_abstract_class(self):
        assert isabstract(AddImageStorage)

    @patch.multiple(AddImageStorage, __abstractmethods__=set())
    def test_2_should_AddImageStorage_raise_a_NotImplementedError_if_not_implemented(self):
        add_image_storage = AddImageStorage()
        params = AddImageRepositoryParams(
            content_type='any_type',
            glasses_id='any_id',
            image=BytesIO()
        )
        with pytest.raises(NotImplementedError, match='Should implement method: add_image'):
            add_image_storage.add_image(params)
