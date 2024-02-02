class CodeStructureDiagram:
    def __init__(self, registry):
        self.registry = registry

    def convert_to_plantuml(self):
        # Commence par le début du diagramme UML
        plantuml_code = "@startuml\n"
        
        # Ajoute chaque élément du registre au diagramme UML
        root = self.registry.get_root()
        for element in root.get_children():
            plantuml_code += self.process_element(element)
        
        plantuml_code += "@enduml"
        return plantuml_code

    def process_element(self, element):
        """
        Traite chaque élément du registre et retourne le code PlantUML correspondant.
        """
        uml_code = ""
        if element.type == 'class':
            uml_code += f"class {element.name} "
            if element.extends:
                uml_code += f"extends {element.extends} "
            if element.implements:
                # Supposons que 'implements' est une liste
                uml_code += f"implements {', '.join(element.implements)} "
            uml_code += "{\n"
            for child in element.get_children():
                uml_code += self.process_element(child)
            uml_code += "}\n"
        elif element.type == 'interface':
            uml_code += f"interface {element.name}"+"{\n"
            for child in element.get_children():
                uml_code += self.process_element(child)
            uml_code += "}\n"
        # Ajoutez ici d'autres types d'éléments si nécessaire
        
        return uml_code

    def save_to_file(self, uml_code, file_path):
        """
        Sauvegarde le code UML généré dans un fichier.
        """
        with open(file_path, 'w') as file:
            file.write(uml_code)