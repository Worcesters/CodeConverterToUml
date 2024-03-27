import re
from ParserModule.Parser.PHP.Parser import Parser
from Registry.Registry import Registry
from Registry.RegistryModule.StructuralRegistry.Structure import RegistryAttribute
from TreeModule.TreeElement import TreeElement


class AttributeParser( Parser ):
    """
    Parser for PHP attributes.

    This parser is responsible for parsing PHP lines and adding attributes to the registry.
    """

    def __init__( self ):
        super().__init__()
        print('Initialisation AttributeParser')
        print('└────────────────────────────│')

    def parse(self, line: str, registry: Registry):
        """
        Parse a PHP line and add attributes to the registry.

        Args:
            line (str): The PHP line to parse.
            registry (Registry): The registry to add attributes to.
        """

        # Print that parsing has started
        print('AttributeParser -----> [START]')

        # Define the pattern to find PHP attributes
        attribute_pattern = re.compile(r"""(?P<visibility>public|protected|private)?\s*\$(?P<attribute_name>\w+)""", re.MULTILINE | re.DOTALL)

        # Find all matches in the line
        for match in re.finditer(attribute_pattern, line):

            # Create a new attribute element
            attribute_element = RegistryAttribute()

            # Set the attribute name and visibility
            attribute_element.set_name(match.group('attribute_name'))
            attribute_element.set_visibility(self.get_visibility(match.group('visibility')))

            # Add the attribute to the registry
            if attribute_element is not None:
                # print(f"attribute_element is an instance of RegistryAttribute: {isinstance(attribute_element, RegistryAttribute)}")
                # active_element = registry.get_active_element()
                #print(f"Type of active_element: {type(active_element)}")

                registry.get_active_element().add_child( TreeElement(attribute_element) )
                registry.set_active_element(attribute_element)


        print('AttributeParser -----> [DONE]')
