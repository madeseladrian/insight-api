from inspect import isabstract

from src.data.contracts.cryptography import Decrypter


class TestDecrypter:
    def test_1_should_Decrypter_is_an_abstract_class(self):
        assert isabstract(Decrypter)
