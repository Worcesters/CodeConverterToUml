from TreeModule.Tree import Tree
from Registry.StructuralElement import StructuralElement

class Registry( Tree ):
    """
    This class implements a registry of structural elements.
    The registry is a tree, where the root is the root of the source code,
    and each branch represents a sub structure of the code.
    The registry allows to navigate through the code and to keep track of the
    current structural element.
    """

    root_element: StructuralElement
    active_element: StructuralElement

    def __init__( self, root_element ):
        super().__init__()
        self.set_root( root_element )
        self.set_active_element( root_element )

    def set_active_element( self, active_element: StructuralElement ):
        """Set the active element of the registry"""
        self.active_element = active_element

    def get_active_element( self ):
        """Get the active element of the registry"""
        return self.active_element
