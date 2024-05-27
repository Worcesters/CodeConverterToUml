import re
from ParserModule.Parser.PHP.Parser import Parser
from Registry.Registry import Registry
from Registry.RegistryModule.RelationalRegistry.Link import (Heritage, Implementation, Pole)
# from Registry.RelationalElement import Pole
from Registry.RegistryModule.StructuralRegistry.Structure import (RegistryClass, RegistryEnum, RegistryInterface)

from TreeModule.TreeElement import TreeElement

class StructureParser( Parser ):
    """
    Structure parser for PHP code.

    This class is responsible for parsing PHP code and extracting structure information
    such as class, interface, and enum definitions. The extracted information is then
    added to the registry.
    """

    def parse(self, line: str, registry: Registry, tree_element: TreeElement):
        structure_pattern = re.compile(
            r"""\b(?P<type>class|interface|enum)\s+(?P<name>[A-Z][\w]*)\b"""  # Match the type and name.
            r"""(?:\s+extends\s+(?P<extends>[\\\w]+))?"""  # Optionally match the 'extends' clause.
            r"""(?:\s+implements\s+(?P<implements>(?:[\\\w]+\s*,\s*)*[\\\w]+))?""",  # Optionally match the 'implements' clause.
            re.VERBOSE | re.MULTILINE | re.DOTALL
        )

        for match in re.finditer(structure_pattern, line):
            structure_element_type = match.group('type')

            if (structure_element_type == 'enum'):
                structure_element = RegistryEnum()
            elif (structure_element_type == 'interface'):
                structure_element = RegistryInterface()
            else:
                structure_element = RegistryClass()

            structure_element.set_name(match.group('name'))

            if match.group('extends') or match.group('implements'):
                if match.group('extends'):
                    print('heritage match extends')
                    heritage_element = Heritage()

                    # Create Pole object for source
                    source_pole_extends = Pole()
                    source_pole_extends.name = match.group('name')
                    heritage_element.set_source(source_pole_extends)

                    # Create Pole object for destination
                    destination_pole_extends = Pole()
                    destination_pole_extends.name = match.group('extends')
                    heritage_element.set_destination(destination_pole_extends)

                    tree_element.add_herits(heritage_element)
                    print(f'tree_element: {tree_element}')
                    print(f'heritage_element: {heritage_element}')

                if match.group('implements'):
                    print('heritage match implements')
                    implementation_element = Implementation()

                    # Create Pole object for source
                    source_pole_implements = Pole()
                    source_pole_implements.name = match.group('name')
                    implementation_element.set_source(source_pole_implements)

                    # Create Pole object for destination
                    destination_pole_implements = Pole()
                    destination_pole_implements.name = match.group('implements')
                    implementation_element.set_destination(destination_pole_implements)
                    tree_element.add_herits(implementation_element)
                    print(f'tree_element: {tree_element}')
                    print(f'implementation_element: {implementation_element}')

            if structure_element is not None:
                active_tree_element = registry.get_active_element()

                tree_element.add_parent(structure_element)
                registry.set_active_element(tree_element)

