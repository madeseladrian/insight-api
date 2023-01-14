from inspect import isabstract

from src.data.contracts.db.glasses import AddImageStorage


class TestAddImageStorage:
    def test_1_should_AddImageStorage_is_an_abstract_class(self):
        assert isabstract(AddImageStorage)
