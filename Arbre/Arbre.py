import ArbreElement

class Arbre:
    def __init__(self):
        self.root = ArbreElement(None)

    def add_hierarchy(self, hierarchy: 'ArbreElement') -> None:
        self.root = hierarchy
