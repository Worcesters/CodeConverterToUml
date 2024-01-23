from Arbre import Arbre

class Registery(Arbre):
    def __init__(self):
        super().__init__()
    
    def add_element_to_root(self, element_name):
        self.add_child_to_root(element_name)
    
    def initialize_project_with_root(self, root_element_name):
        self.add_root(root_element_name)
