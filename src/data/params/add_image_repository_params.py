from typing import TypedDict

from ...domain.params import AddImageParams


class AddImageRepositoryParams(AddImageParams):
    pass

class AddImageRepositoryResult(TypedDict):
    glasses_id: str
    url_image: str
