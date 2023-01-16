from typing import List, TypedDict


class GetGlassesParams(TypedDict):
    id: str

class GetGlassesResult(TypedDict):
    glasses: List[dict]
