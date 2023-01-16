from inspect import isabstract

from src.data.contracts.db.glasses import DeleteImageStorage


class TestDeleteImageStorage:
    def test_1_should_DeleteImageStorage_is_an_abstract_class(self):
        assert isabstract(DeleteImageStorage)
