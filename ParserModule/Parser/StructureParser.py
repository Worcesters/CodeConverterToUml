from ParserModule.Interface import ParseInterface
import re

class StructureParser(ParseInterface):
    def __init__(self, registry, dispatcher):
        print('Initialisation StructureParser')
        print('└────────────────────────────│')
        self.registry = registry
        self.dispatcher = dispatcher

    def parse(self, code: str):
        print('StructureParser -----> [START]')
        # Récupérer le motif regex pour les structures (classes, interfaces, etc.)
        structure_pattern_str = self.dispatcher.get_pattern('structure_pattern')
        structure_pattern = re.compile(structure_pattern_str, re.MULTILINE | re.DOTALL)

        for match in re.finditer(structure_pattern, code):
            structure_type = match.group('type')
            structure_name = match.group('name')
            extends = match.group('extends') or 'None'
            implements = match.group('implements') or 'None'

            structure_info = {
                'type': structure_type,
                'name': structure_name,
                'extends': extends,
                'implements': implements
            }
            
            self.registry.get_root().add_child(structure_info)
        print('StructureParser -----> [DONE]')
