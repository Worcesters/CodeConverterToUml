# Assurez-vous d'importer Tree et TreeElement correctement depuis leurs modules respectifs.
from TreeModule.Tree import Tree
from TreeModule.TreeElement import TreeElement

class Registry( Tree ):
    """
    This class implements a registry of structural elements.
    The registry is a tree, where the root is the root of the source code,
    and each branch represents a sub-structure of the code.
    The registry allows to navigate through the code and to keep track of the
    current structural element.
    """

    def __init__( self, root_element ):
        super().__init__()
        # Ici, on suppose que root_element est une instance appropriée pour être la racine.
        # Si root_element est déjà un TreeElement, on peut directement le mettre comme racine.
        # Autrement, on l'enveloppe dans un TreeElement.
        if isinstance(root_element, TreeElement):
            self.set_root(root_element)
        else:
            self.set_root(TreeElement(root_element))
        self.active_element = self.get_root()
        print("iiiiiiiiiiiiiiiiciiiiiiiiiiiiiiiiiiiiiiii")
        print(self.active_element)# On commence avec l'élément racine comme élément actif.

    def set_active_element( self, active_element ):
        """Set the active element of the registry."""
        if isinstance(active_element, TreeElement):
            self.active_element = active_element
        else:
            self.active_element = TreeElement(active_element)

    def get_active_element(self):
        """Get the active element of the registry."""
        return self.active_element

    # ... Vous pouvez ajouter d'autres méthodes nécessaires pour votre Registry ici ...