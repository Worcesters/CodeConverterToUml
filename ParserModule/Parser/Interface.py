from abc import ABC, abstractmethod
from Registry.Registry import Registry

class IParser(ABC):
    @abstractmethod
    def parse(self, line: str, registry: Registry) -> None:
        raise NotImplementedError("La méthode parse doit être implémentée dans les sous-classes.")
