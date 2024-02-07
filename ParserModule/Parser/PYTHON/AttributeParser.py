from ParserModule.Parser.PHP import Parser
import re

class AttributeParser(Parser):
    def __init__(self, registry):
        print('Initialisation AttributeParser')
        print('└────────────────────────────│')
        self.registry = registry

    def parse(self, code: str):
        print('AttributeParser -----> [START]')
        attribute_pattern = re.compile(r"""(?P<visibility>public|protected|private)?\s*\$(?P<attribute_name>\w+)""", re.MULTILINE | re.DOTALL)

        for match in re.finditer(attribute_pattern, code):
            visibility = match.group('visibility') or 'public'  # 'public' par défaut si non spécifié
            attribute_name = match.group('attribute_name')
            attribute_type = match.group('attribute_type') or 'mixed'  # 'mixed' par défaut si non spécifié

            attribute_info = {
                "name": attribute_name,
                "visibility": visibility,
                "type": attribute_type
            }
            
            self.registry.get_root().add_child(attribute_info)
        print('AttributeParser -----> [DONE]')
