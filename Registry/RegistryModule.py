from TreeModule.Tree import Tree
from Registry.RegistryElement import RegistryElement
class Registry(Tree):
    
    root_element: RegistryElement
    active_elements: RegistryElement
    
    def __init__(self, root_element):
        super().__init__()
        self.set_root(root_element)
        self.set_active_element(root_element)
    
    def set_active_element(self, active_element: RegistryElement):
        self.active_element = active_element
    
    def get_active_element(self):
        return self.active_element