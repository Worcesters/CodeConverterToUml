class CodeStructureDiagram:
    def __init__(self, backup):
        self.backup = backup

    def traverse_tree(self, node, uml_elements):
        if node is None:
            return

        # Traiter le noeud actuel en fonction de son type (classe, interface, méthode, etc.)
        uml_elements.append(self.generate_uml_element(node))

        # Parcourir les enfants du noeud
        for child in node.get_children():
            self.traverse_tree(child, uml_elements)

    def generate_uml_element(self, node):
        # Générer la représentation UML pour le noeud
        # Cette méthode doit être adaptée en fonction de la structure de vos noeuds
        if node.is_class():
            return f"class {node.name} {{ ... }}"
        elif node.is_method():
            return f"{node.name}() ..."
        # Ajouter des cas pour d'autres types si nécessaire
        return ""

    def generate_diagram_code(self):
        uml_elements = []
        self.traverse_tree(self.backup.get_root(), uml_elements)

        diagram_code = f"""
        @startuml
        skinparam classAttributeIconSize 0
        {' '.join(uml_elements)}
        @enduml
        """
        return diagram_code
