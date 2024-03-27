from TreeModule.Tree import Tree
from TreeModule.TreeElement import TreeElement  # Ajoutez l'import de TreeElement
from Registry.StructuralElement import StructuralElement

class Registry(Tree):
    """
    This class implements a registry of structural elements.
    The registry is a tree, where the root is the root of the source code,
    and each branch represents a sub structure of the code.
    The registry allows to navigate through the code and to keep track of the
    current structural element.
    """

    def __init__(self, root_element):
        super().__init__()
        self.root_element = TreeElement(root_element)  # Enveloppez root_element dans un objet TreeElement
        self.active_element = self.root_element  # Enveloppez active_element dans un objet TreeElement

    def set_active_element(self, active_element: StructuralElement):
        """Set the active element of the registry"""
        self.active_element = TreeElement(active_element)  # Enveloppez active_element dans un objet TreeElement

    def get_active_element(self):
        """Get the active element of the registry"""
        return self.active_element
