from fastapi import FastAPI
from src.main.config import create_app


class TestApp:
    app = create_app()

    def test_1_should_create_app_is_instance_of_fastapi(self):
        assert isinstance(create_app(), FastAPI)

    def test_2_should_create_app_calls_with_middlewares(self):
        middlewares = self.app.user_middleware[0].__dict__
        middlewares_options = middlewares['options']

        assert middlewares_options['allow_origins'] == ['*']
        assert middlewares_options['allow_credentials']
        assert middlewares_options['allow_methods'] == ['*']
        assert middlewares_options['allow_headers'] == ['*']
