from ParserModule.Parser import Parser
from Registry.Registry import Registry
from Registry.RegistryElement import (
    AttributeRegistry,
    VisibilityRegistry,
    TypeRegistry
)
import re

class AttributeParser(Parser):
    def __init__(self):
        print('Initialisation AttributeParser')
        print('└────────────────────────────│')
        
    def parse(self, line: str, registry: Registry):
        print('AttributeParser -----> [START]')
        attribute_pattern = re.compile(r"""(?P<visibility>public|protected|private)?\s*\$(?P<attribute_name>\w+)""", re.MULTILINE | re.DOTALL)

        for match in re.finditer(attribute_pattern, line):
            
            attribute_element = AttributeRegistry()
            attribute_element.set_name(match.group('attribute_name'))
            
            visibility_element = VisibilityRegistry()
            visibility_element.set_visibility(match.group('visibility'))
            
            type_element = TypeRegistry()
            type_element.set_type(match.group('attribute_type'))
            
            registry.get_active_element().add_child(attribute_element)
            registry.set_active_element()
        print('AttributeParser -----> [DONE]')
