from inspect import isabstract
from io import BytesIO
import pytest
from unittest.mock import patch

from src.domain.features import AddImages
from src.domain.params import AddImagesParams


class TestAddAccount:
    def test_1_should_AddImages_is_an_abstract_class(self):
        assert isabstract(AddImages)

    @patch.multiple(AddImages, __abstractmethods__=set())
    def test_2_should_AddImages_raise_a_NotImplementedError_if_not_implemented(self):
        params = AddImagesParams(
            image=BytesIO(),
            glasses_id='any_id'
        )
        add_images = AddImages()

        with pytest.raises(NotImplementedError, match='Should implement method: add_image'):
            add_images.add_image(params)
