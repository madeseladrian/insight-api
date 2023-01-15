from typing import BinaryIO, TypedDict


class AddImageParams(TypedDict):
    content_type: str
    glasses_id: str
    image: BinaryIO
