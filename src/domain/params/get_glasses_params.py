from typing import Dict, List, TypedDict


class GetGlassesParams(TypedDict):
    id: str

class GetGlassesResult(TypedDict):
    glasses: List[Dict]
