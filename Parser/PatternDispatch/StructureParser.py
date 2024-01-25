from ..Interface import ParseInterface
import re

class StructureParser(ParseInterface):
    def __init__(self, code_converter_registry):
        self.code_converter_registry = code_converter_registry

    def parse(self, code: str):
        class_pattern = re.compile(r'\s*(?P<visibility>public|protected|private)?\s*class\s+(?P<class_name>\w+)\s*')
        interface_pattern = re.compile(r'\s*(?P<visibility>public|protected|private)?\s*interface\s+(?P<interface_name>\w+)\s*')
        entity_pattern = re.compile(r'\s*(?P<visibility>public|protected|private)?\s*entity\s+(?P<entity_name>\w+)\s*')

        for match in re.finditer(class_pattern, code):
            class_info = {
                'visibility': match.group('visibility'),
                'class_name': match.group('class_name') 
            }

            self.registry.get_root().set_parent(class_info)

        for match in re.finditer(interface_pattern, code):
            interface_info = {
                'visibility': match.group('visibility'),
                'interface_name': match.group('interface_name') 
            }

            self.registry.get_root().set_parent(interface_info)

        for match in re.finditer(entity_pattern, code):
            entity_info = {
                'visibility': match.group('visibility'),
                'entity_name': match.group('entity_name') 
            }

            self.registry.get_root().set_parent(entity_info)