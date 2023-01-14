from inspect import isabstract
import pytest
from unittest.mock import patch

from src.data.contracts.db.glasses import AddImageStorage


class TestAddImageStorage:
    def test_1_should_AddImageStorage_is_an_abstract_class(self):
        assert isabstract(AddImageStorage)

    @patch.multiple(AddImageStorage, __abstractmethods__=set())
    def test_2_should_AddImageStorage_raise_a_NotImplementedError_if_not_implemented(self):
        add_image_storage = AddImageStorage()

        with pytest.raises(NotImplementedError, match='Should implement method: add_image'):
            add_image_storage.add_image(image='', image_type='')
