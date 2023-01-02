from inspect import isabstract

from src.data.contracts.cryptography import Encrypter

class TestEncrypter:
    def test_1_should_Encrypter_is_an_abstract_class(self):
        assert isabstract(Encrypter)
