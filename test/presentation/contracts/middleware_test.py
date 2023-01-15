from inspect import isabstract

from src.presentation.contracts import Middleware


class TestMiddleware:
    def test_1_should_Middleware_is_an_abstract_class(self):
        assert isabstract(Middleware)
