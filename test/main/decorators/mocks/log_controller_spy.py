from typing import Any

from src.presentation.contracts import Controller
from src.presentation.helpers import HttpResponse, ok


class LogControllerSpy(Controller):
    http_response: HttpResponse = ok(True)
    request: Any = None

    def handle(self, request: Any) -> HttpResponse:
        self.request = request
        return self.http_response
