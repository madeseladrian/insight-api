from src.presentation.helpers import HttpResponse
from src.main.adapters import route_response_adapter


class TestRouteResponseAdapter:

    def test_1_should_adapter_return_correct_data_on_200(self):
        http_response = HttpResponse(
            status_code=200,
            body=True
        )

        assert route_response_adapter(http_response) == http_response
