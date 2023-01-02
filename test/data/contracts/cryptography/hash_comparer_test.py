from inspect import isabstract

from src.data.contracts.cryptography import HashComparer


class TestHashComparer:
    def test_1_should_HashComparer_is_an_abstract_class(self):
        assert isabstract(HashComparer)
