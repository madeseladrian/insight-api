from inspect import isabstract

from src.domain.features import Authentication


class TestAuthentication:
    def test_1_should_Authentication_is_an_abstract_class(self):
        assert isabstract(Authentication)
