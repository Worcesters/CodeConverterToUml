from ArbreElement import ArbreElement

class Arbre:
    def __init__(self):
        self.root = None

    def add_root(self, element):
        self.root = ArbreElement(element)

    def add_child_to_root(self, element):
        if self.root is not None:
            child = ArbreElement(element)
            self.root.add_child(child)
