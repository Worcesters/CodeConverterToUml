from Registry.Enum import RegistryVisibility, RegistryType
from Registry.RegistryElement import RegistryElement

class StructuralElement( RegistryElement ):
    """
    Base class for common elements in the registry.
    """

    def __init__(self, name: str = '', visibility: 'RegistryVisibility' = RegistryVisibility.PUBLIC,
                 element_type: 'RegistryType' = RegistryType.UNKNOWN):
        """
        Initialize a new RegistryCommonElement.

        Args:
            name (str): The name of the element.
            visibility (RegistryVisibility): The visibility of the element.
            element_type (RegistryType): The type of the element.
        """

        self.mutability = True  # Whether the element is mutable
        self.name = name  # The name of the element
        self.visibility = visibility  # The visibility of the element
        self.element_type = element_type  # The type of the element

    def set_mutability(self, mutability: bool):
        """
        Set the mutability of the element.

        Args:
            mutability (bool): The new mutability value.
        """
        self.mutability = mutability

    def set_name(self, name: str):
        """
        Set the name of the element.

        Args:
            name (str): The new name.
        """
        if name:
            self.name = name

    def set_visibility( self, visibility: 'RegistryVisibility' ):
        """
        Set the visibility of the element.

        Args:
            visibility (RegistryVisibility): The new visibility.
        """
        if visibility:
            self.visibility = visibility

    def set_type( self, element_type: 'RegistryType' ):
        """
        Set the type of the element.

        Args:
            element_type (RegistryType): The new type.
        """
        if element_type:
            self.element_type = element_type

    def get_name(self):
        return self.name