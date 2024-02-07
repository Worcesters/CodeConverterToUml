from ParserModule.Parser.PHP import Parser
from Registry.Registry import Registry
from Registry.RegistryModule.StructuralRegistry.Structure import RegistryAttribute
import re

class AttributeParser(Parser):
    def __init__(self):
        print('Initialisation AttributeParser')
        print('└────────────────────────────│')
        
    def parse(self, line: str, registry: Registry):
        print('AttributeParser -----> [START]')
        attribute_pattern = re.compile(r"""(?P<visibility>public|protected|private)?\s*\$(?P<attribute_name>\w+)""", re.MULTILINE | re.DOTALL)

        for match in re.finditer(attribute_pattern, line):
            
            attribute_element = RegistryAttribute()
            attribute_element.set_name(match.group('attribute_name'))
            attribute_element.set_visibility(self.get_visibility(match.group('visibility')))
            attribute_element.set_type(self.get_type(match.group('attribute_type')))
            
            registry.get_active_element().add_child(attribute_element)
            registry.set_active_element()
        print('AttributeParser -----> [DONE]')
