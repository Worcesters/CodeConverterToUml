from ParserModule.Parser import Parser
from Registry.RegistryModule import Registry
from Registry.RegistryElement import (
    StructureRegistry,
    TypeRegistry,
    HeritageRegistry
)
import re

class StructureParser(Parser):
    def __init__(self):
        print('Initialisation StructureParser')
        print('└────────────────────────────│')

         
    def parse(self, line: str, registry: Registry):
        print('StructureParser -----> [START]')
        
        structure_pattern = re.compile(r"""(?P<type>class|interface|enum)\s+(?P<name>\w+)\s*(?:extends\s+(?P<extends>\w+)\s*)?(?:implements\s+(?P<implements>[\w\s,]+))?""", re.MULTILINE | re.DOTALL)

        for match in re.finditer(structure_pattern, line):
            
            # Configuration du type de structure en fonction de l'entité déterminée
            structure_element = match.group('type').capitalize() + "Registry" # Transforme 'class' en 'ClassRegistry', etc.
            structure_element.set_name(match.group('name'))
            
            # Configuration de l'héritage et des implémentations
            if match.group('extends') or match.group('implements'):
                heritage_element = HeritageRegistry()
                if match.group('extends'):
                    heritage_element.set_extends(match.group('extends'))
                if match.group('implements'):
                    heritage_element.set_implements(match.group('implements'))
            
            registry.get_active_element().add_child(structure_element)
            registry.set_active_element()
            
        print('StructureParser -----> [DONE]')
