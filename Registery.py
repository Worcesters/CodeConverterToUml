from Arbre import Arbre

class Registery(Arbre):
    def add_class(self, class_name: str):
        class_node = ArbreElement(class_name)
        self.root.add_child(class_node)
        return class_node
    
