from abc import ABC, abstractmethod

class ParseInterface(ABC):
    @abstractmethod
    def parse(self, line: str) -> None:
        raise NotImplementedError("La méthode parse doit être implémentée dans les sous-classes.")