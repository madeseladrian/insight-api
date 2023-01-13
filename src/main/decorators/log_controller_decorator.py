from dataclasses import dataclass
from typing import Any

from ...data.contracts.db.log import LogErrorRepository

from ...presentation.contracts import Controller
from ...presentation.helpers import HttpResponse

@dataclass
class LogControllerDecorator(Controller):
    controller: Controller
    log_error_repository: LogErrorRepository

    def handle(self, request: Any) -> HttpResponse:
        http_response = self.controller.handle(request)
        return http_response
