from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db.glasses import DeleteImageStorage
from src.data.params import DeleteImageRepositoryParams


class TestDeleteImageStorage:
    def test_1_should_DeleteImageStorage_is_an_abstract_class(self):
        assert isabstract(DeleteImageStorage)

    @patch.multiple(DeleteImageStorage, __abstractmethods__=set())
    def test_2_should_DeleteImageStorage_raise_a_NotImplementedError_if_not_implemented(self):
        delete_image_storage = DeleteImageStorage()
        params = DeleteImageRepositoryParams(glass_id='any_id')

        with pytest.raises(NotImplementedError, match='Should implement method: delete_image'):
            delete_image_storage.delete_image(params)
