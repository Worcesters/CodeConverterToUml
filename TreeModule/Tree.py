from TreeModule.TreeElement import TreeElement

class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, element):
        # Si element est déjà un TreeElement, on l'assigne directement.
        # Sinon, on crée un nouveau TreeElement avec element comme paramètre.
        if isinstance(element, TreeElement):
            self.root = element
        else:
            self.root = TreeElement(element)

    def get_root(self):
        return self.root