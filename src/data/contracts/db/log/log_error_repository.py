from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class LogErrorRepository(ABC):

    @abstractmethod
    def log_error(self, error: Any) -> None:
        raise NotImplementedError('Should implement method: log_error')
