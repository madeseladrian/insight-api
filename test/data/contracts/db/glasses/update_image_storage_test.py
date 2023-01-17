from inspect import isabstract

from src.data.contracts.db.glasses import UpdateImageStorage


class TestUpdateImageStorage:
    def test_1_should_UpdateImageStorage_is_an_abstract_class(self):
        assert isabstract(UpdateImageStorage)
