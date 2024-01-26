from TreeModule.Tree import Tree

class Registry(Tree):
    def __init__(self):
        super().__init__()
        self.initialize_project_with_root("CodeConverterToUml")
    
    def initialize_project_with_root(self, root_element_name):
        self.set_root(root_element_name)
