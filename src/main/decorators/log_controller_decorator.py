from dataclasses import dataclass
from typing import Any

from ...data.contracts.db.log import LogErrorRepository

from ...presentation.contracts import Controller


@dataclass
class LogControllerDecorator(Controller):
    controller: Controller
    log_error_repository: LogErrorRepository

    def handle(self, request: Any) -> Any:
        self.controller.handle(request)
