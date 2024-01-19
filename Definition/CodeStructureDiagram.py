
class CodeStructureDiagram:
    def __init__(self):
        self.hierarchies = []
        self.classes = []
        self.methods = []
        self.interfaces = []

    def add_hierarchy(self, hierarchy):
        self.hierarchies.append(hierarchy)

    def add_class(self, class_obj):
        self.classes.append(class_obj)

    def add_method(self, method):
        self.methods.append(method)

    def add_interface(self, interface):
        self.interfaces.append(interface)

    def generate_diagram_code(self):
        interfaces_code = "\n".join([interface.generate_uml_code() for interface in self.interfaces])
        elements_code = "\n".join([element.generate_uml_code() for element in self.classes])
        inheritance_relations_code = "\n".join([hierarchy.generate_uml_code() for hierarchy in self.hierarchies])

        diagram_code = f"""
        @startuml

        skinparam classAttributeIconSize 0

        {interfaces_code}
        {elements_code}
        {inheritance_relations_code}
        @enduml
        """
        return diagram_code