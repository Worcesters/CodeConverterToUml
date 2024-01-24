import ArbreElement

class Arbre:
    def __init__(self):
        self.root = None

    def set_root(self, element):
        self.root = ArbreElement(element)
        
    def get_root(self):
        return self.root
