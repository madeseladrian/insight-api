from faker import Faker
from typing import Tuple

from src.main.decorators import LogControllerDecorator

from ...data.mocks.log import LogErrorRepositorySpy
from .mocks import LogControllerSpy


class TestLogControllerDecorator:
    faker = Faker()
    request = {'status': 201, 'body': True}

    SutTypes = Tuple[
        LogControllerDecorator,
        LogControllerSpy,
        LogErrorRepositorySpy
    ]

    def make_sut(self) -> SutTypes:
        log_controller_spy = LogControllerSpy()
        log_error_repository = LogErrorRepositorySpy()
        sut = LogControllerDecorator(
            controller=log_controller_spy,
            log_error_repository=log_error_repository
        )

        return sut, log_controller_spy, log_error_repository

    def test_1_should_call_controller_handle(self):
        sut, log_controller_spy, _ = self.make_sut()
        sut.handle(self.request)

        assert self.request['body'] == log_controller_spy.request['body']
