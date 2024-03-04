from ParserModule.Parser.PHP import Parser
from Registry.Registry import Registry
from Registry.RegistryModule.RelationalRegistry.Link import (Heritage, Implementation)
import re

class StructureParser( Parser ):
    def __init__( self ):
        print('Initialisation StructureParser')
        print('└────────────────────────────│')


    def parse( self, line: str, registry: Registry ):
        print('StructureParser -----> [START]')

        structure_pattern = re.compile(r"""(?P<type>class|interface|enum)\s+(?P<name>\w+)\s*(?:extends\s+(?P<extends>\w+)\s*)?(?:implements\s+(?P<implements>[\w\s,]+))?""", re.MULTILINE | re.DOTALL)

        for match in re.finditer(structure_pattern, line):

            # Configuration du type de structure en fonction de l'entité déterminée
            structure_element = "Registry" + match.group('type').capitalize() # Transforme 'class' en 'RegistryClass', etc.
            structure_element.set_name(match.group('name'))


            # TODO : Configuration de l'héritage et des implémentations
            if match.group('extends') or match.group('implements'):
                if match.group('extends'):
                    heritage_element = Heritage()
                    heritage_element.set_source(match.group('name'))
                    heritage_element.set_destination(match.group('extends'))
                if match.group('implements'):
                    Implementation_element = Implementation()
                    Implementation_element.set_source(match.group('name'))
                    Implementation_element.set_destination(match.group('implements'))

            registry.get_active_element().add_child(structure_element)
            registry.set_active_element()

        print('StructureParser -----> [DONE]')
