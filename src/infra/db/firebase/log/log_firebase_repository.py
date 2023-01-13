from dataclasses import dataclass
import datetime
from typing import Any

from .....data.contracts.db.log import LogErrorRepository
from ..firebase_helper import firebase_helper

@dataclass
class LogFirebaseRepository(LogErrorRepository):

    def log_error(self, error: Any) -> None:
        error_collection = firebase_helper.get_document('logs')
        error_collection.set({
            'log': str(error),
            'date': datetime.datetime.now()
        })
