import re
from ParserModule.Parser.PHP.Parser import Parser
from Registry.Registry import Registry
from Registry.RegistryModule.RelationalRegistry.Link import (Heritage, Implementation, Pole)
from Registry.RegistryModule.StructuralRegistry.Structure import (RegistryClass, RegistryEnum, RegistryInterface)

from TreeModule.TreeElement import TreeElement

class StructureParser( Parser ):
    """
    Structure parser for PHP code.

    This class is responsible for parsing PHP code and extracting structure information
    such as class, interface, and enum definitions. The extracted information is then
    added to the registry.
    """

    def __init__( self ):
        super().__init__()
        # print('Initialisation StructureParser')
        # print('└────────────────────────────│')


    def parse(self, line: str, registry: Registry):
        # print('StructureParser -----> [START]')

        structure_pattern = re.compile(
            r"""(?P<type>class|interface|enum)\s+(?P<name>\w+)\s*"""
            r"""(?:extends\s+(?P<extends>\w+)\s*)?"""
            r"""(?:implements\s+(?P<implements>[\w\s,]+))?""",
            re.MULTILINE | re.DOTALL
        )

        for match in re.finditer(structure_pattern, line):

            type_to_class = {
                'class': RegistryClass,
                'interface': RegistryInterface,
                'enum': RegistryEnum
            }

            structure_element_type = match.group('type')
            structure_element = type_to_class.get(structure_element_type, lambda: None)()
            structure_element.set_name(match.group('name'))

            if match.group('extends') or match.group('implements'):
                if match.group('extends'):
                    heritage_element = Heritage()

                    # Create Pole object for source
                    source_pole_extends = Pole()
                    source_pole_extends.name = match.group('name')
                    heritage_element.set_source(source_pole_extends)

                    # Create Pole object for destination
                    destination_pole_extends = Pole()
                    destination_pole_extends.name = match.group('extends')
                    heritage_element.set_destination(destination_pole_extends)

                if match.group('implements'):
                    implementation_element = Implementation()

                    # Create Pole object for source
                    source_pole_implements = Pole()
                    source_pole_implements.name = match.group('name')
                    implementation_element.set_source(source_pole_implements)

                    # Create Pole object for destination
                    destination_pole_implements = Pole()
                    destination_pole_implements.name = match.group('implements')
                    implementation_element.set_destination(destination_pole_implements)

            if structure_element is not None:
                active_element = registry.get_active_element()
                TreeElement(active_element).add_child(structure_element)
                registry.set_active_element(structure_element)

        # print('StructureParser -----> [DONE]')
