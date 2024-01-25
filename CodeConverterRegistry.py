from TreeModule import Tree

class CodeConverterRegistry(Tree):
    def __init__(self):
        Tree.__init__()
        self.initialize_project_with_root("CodeConverterToUml")
    
    def initialize_project_with_root(self, root_element_name):
        self.set_root(root_element_name)
