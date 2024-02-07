from ParserModule.Parser.PHP import Parser
import re

class StructureParser(Parser):
    def __init__(self, registry):
        print('Initialisation StructureParser')
        print('└────────────────────────────│')
        self.registry = registry

    def parse(self, code: str):
        print('StructureParser -----> [START]')
        
        structure_pattern = re.compile(r"""(?P<type>class|interface|enum)\s+(?P<name>\w+)\s*(?:extends\s+(?P<extends>\w+)\s*)?(?:implements\s+(?P<implements>[\w\s,]+))?""", re.MULTILINE | re.DOTALL)
        
        print(structure_pattern)
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
