from ParserModule.Interface import ParseInterface
import re

class AttributeParser(ParseInterface):
    def __init__(self, registry, dispatcher):
        print('Initialisation AttributeParser')
        print('└────────────────────────────│')
        self.registry = registry
        self.dispatcher = dispatcher

    def parse(self, code: str):
        print('AttributeParser -----> [START]')
        # Récupérer le motif regex pour les attributs
        attribute_pattern_str = self.dispatcher.get_pattern('attribute_pattern')
        attribute_pattern = re.compile(attribute_pattern_str, re.MULTILINE | re.DOTALL)

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
