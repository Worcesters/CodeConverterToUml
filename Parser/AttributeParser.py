from interface import ParseInterface
import re

class AttributeParser(ParseInterface):
    def __init__(self, registery):
        self.registery = registery

    def parse(self, code: str, current_class):
        if current_class:
            attribute_pattern = r'(?P<visibility>public|protected|private)?\s+\$(?P<attribute_name>\w+)\s*(?P<attribute_type>\w*)\s*;'

            for match in re.finditer(attribute_pattern, code, re.MULTILINE | re.DOTALL):
                visibility = match.group('visibility')
                attribute_name = match.group('attribute_name')
                attribute_type = match.group('attribute_type')

                attribute_info = {
                    "name": attribute_name,
                    "visibility": visibility,
                    "type": attribute_type
                }

                # Ajouter l'attribut au registre avec le couple (parent, enfant)
                self.registery.add_children(current_class, attribute_info)

