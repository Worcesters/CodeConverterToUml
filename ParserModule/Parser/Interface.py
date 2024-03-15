from abc import ABC, abstractmethod
from Registry.Registry import Registry

class IParser( ABC ):
    """
    Abstract base class defining the interface for a parser.

    All concrete parsers must implement the `parse` method.
    """

    @abstractmethod
    def parse(self, line: str, registry: 'Registry') -> None:
        """
        Parse a line of code and update the registry accordingly.

        Args:
            line (str): The line of code to parse.
            registry (Registry): The registry to update.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("La méthode parse doit être implémentée dans les sous-classes.")