from typing import TypedDict


class AddGlassesParams(TypedDict):
    url_image: str
    glasses_id: str
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
