from interface import ParseInterface
import re

class StructureParser(ParseInterface):
    def __init__(self, registery, current_class):
        self.registery = registery
        self.current_class = current_class

    def parse(self, code: str):
        # Logique pour identifier les déclarations de classes, interfaces, entités, etc.
        class_pattern = re.compile(r'\s*(?P<visibility>public|protected|private)?\s*class\s+(?P<class_name>\w+)\s*')
        interface_pattern = re.compile(r'\s*(?P<visibility>public|protected|private)?\s*interface\s+(?P<interface_name>\w+)\s*')
        entity_pattern = re.compile(r'\s*(?P<visibility>public|protected|private)?\s*entity\s+(?P<entity_name>\w+)\s*')

        # Recherche de déclarations de classes
        for match in re.finditer(class_pattern, code):
            visibility = match.group('visibility')
            class_name = match.group('class_name')
            self.current_class = class_name  # Mettez à jour current_class

            # Enregistrez la classe dans le registre
            self.registery.add_parent(class_name)

        # Recherche de déclarations d'interfaces
        for match in re.finditer(interface_pattern, code):
            visibility = match.group('visibility')
            interface_name = match.group('interface_name')
            self.current_class = interface_name  # Mettez à jour current_class

            # Enregistrez l'interface dans le registre
            self.registery.add_parent(interface_name)

        # Recherche de déclarations d'entités
        for match in re.finditer(entity_pattern, code):
            visibility = match.group('visibility')
            entity_name = match.group('entity_name')
            self.current_class = entity_name  # Mettez à jour current_class

            # Enregistrez l'entité dans le registre
            self.registery.add_parent(entity_name)

        # Vous pouvez ajouter d'autres types (entités, etc.) de la même manière
