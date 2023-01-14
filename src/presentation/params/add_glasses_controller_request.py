from typing import TypedDict
from tempfile import SpooledTemporaryFile


class AddGlassesControllerRequest(TypedDict):
    image: SpooledTemporaryFile
    image_type: str
    user_id: str
    model: str
    format: str
    gender: str
    public: str
    category: str
    frame_color: str
    lens_color: str
    size_lens: float
    size_bridge: float
    height_frame: float
    size_temples: float
    price: float
    additional_info: str
