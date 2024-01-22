from interface import ParseInterface
import re

class StructureParser(ParseInterface):
    def __init__(self, registery):
        self.registery = registery

    def parse(self, code: str):
        class_pattern = re.compile(r'\s*(?P<visibility>public|protected|private)?\s*class\s+(?P<class_name>\w+)\s*')
        interface_pattern = re.compile(r'\s*(?P<visibility>public|protected|private)?\s*interface\s+(?P<interface_name>\w+)\s*')
        entity_pattern = re.compile(r'\s*(?P<visibility>public|protected|private)?\s*entity\s+(?P<entity_name>\w+)\s*')

        for match in re.finditer(class_pattern, code):
            visibility = match.group('visibility')
            class_name = match.group('class_name')

            class_node = ArbreElement(class_name)
            self.registery.add_child(class_node)

            # Utilisez set_parent pour mettre à jour le parent de la classe actuelle
            class_node.set_parent(self.registery.get_parent(class_name))

        for match in re.finditer(interface_pattern, code):
            visibility = match.group('visibility')
            interface_name = match.group('interface_name')

            interface_node = ArbreElement(interface_name)
            self.registery.add_child(interface_node)

            # Utilisez set_parent pour mettre à jour le parent de l'interface actuelle
            interface_node.set_parent(self.registery.get_parent(interface_name))

        for match in re.finditer(entity_pattern, code):
            visibility = match.group('visibility')
            entity_name = match.group('entity_name')

            entity_node = ArbreElement(entity_name)
            self.registery.add_child(entity_node)

            # Utilisez set_parent pour mettre à jour le parent de l'entité actuelle
            entity_node.set_parent(self.registery.get_parent(entity_name))
