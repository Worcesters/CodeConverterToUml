from Arbre import Arbre

class Registery(Arbre):
    def __init__(self):
        super().__init__()
        self.initialize_project_with_root("ProjectRoot")
    
    def add_child_to_root(self, element):
        self.add_child_to_root(element)

    def set_parent_to_root(self, element):
        self.set_parent_to_root(element)
    
    def initialize_project_with_root(self, root_element_name):
        self.add_root(root_element_name)
