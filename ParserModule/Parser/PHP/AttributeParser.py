from ParserModule.Parser import Parser
from Registry.RegistryModule import Registry
import re

class AttributeParser(Parser):
    def __init__(self):
        super().set_level(2)
        print('Initialisation AttributeParser')
        print('└────────────────────────────│')
        
    def parse(self, line: str, registry: Registry):
        print('AttributeParser -----> [START]')
        attribute_pattern = re.compile(r"""(?P<visibility>public|protected|private)?\s*\$(?P<attribute_name>\w+)""", re.MULTILINE | re.DOTALL)

        for match in re.finditer(attribute_pattern, line):
            visibility = match.group('visibility') or 'public'  # 'public' par défaut si non spécifié
            attribute_name = match.group('attribute_name')
            attribute_type = match.group('attribute_type') or 'mixed'  # 'mixed' par défaut si non spécifié

            attribute_info = {
                "name": attribute_name,
                "visibility": visibility,
                "type": attribute_type
            }
            
            registry.get_root().add_child(attribute_info)
        print('AttributeParser -----> [DONE]')
