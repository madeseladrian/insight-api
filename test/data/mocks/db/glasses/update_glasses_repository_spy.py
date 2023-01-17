from typing import Dict

from src.data.contracts.db.glasses import UpdateGlassesRepository


class UpdateGlassesRepositorySpy(UpdateGlassesRepository):
    data: Dict

    def update(self, data: Dict) -> None:
        self.data = data
