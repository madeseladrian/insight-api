from src.presentation.helpers import HttpResponse
from src.main.adapters import route_response_adapter


class TestRouteResponseAdapter:

    def test_1_should_adapter_return_correct_data_on_200(self):
        http_response = HttpResponse(
            status_code=200,
            body=True
        )

        assert route_response_adapter(http_response) == http_response

    def test_2_should_adapter_return_correct_data_on_201(self):
        http_response = HttpResponse(
            status_code=201,
            body=True
        )

        assert route_response_adapter(http_response) == http_response

    def test_3_should_adapter_return_no_data_on_204(self):
        http_response = HttpResponse(
            status_code=204,
            body=True
        )

        assert route_response_adapter(http_response) == http_response
