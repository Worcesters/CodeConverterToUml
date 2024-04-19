from TreeModule.Tree import Tree
from TreeModule.TreeElement import TreeElement
from Registry.StructuralElement import StructuralElement
from Registry.StructuralElement import RegistryProgram

class Registry( Tree ):
    """
    This class implements a registry of structural elements.
    The registry is a tree, where the root is the root of the source code,
    and each branch represents a sub structure of the code.
    The registry allows to navigate through the code and to keep track of the
    current structural element.
    """

    def __init__( self, root_element ):
        super().__init__()

        if not isinstance(root_element, RegistryProgram):
            raise TypeError("The root_element should be an instance of RegistryProgram.")

        if self.get_root() is None:
            self.set_root( TreeElement(root_element) )
            print(f"Registry root: {self.get_root()}")
        self.set_active_element( root_element )

    def set_active_element( self, active_element: StructuralElement ):
        self.active_element = active_element

    def get_active_element( self ):
        return self.active_element