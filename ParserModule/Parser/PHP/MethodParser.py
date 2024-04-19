"""
This module imports necessary dependencies and defines the MethodParser class.
"""

import re

# Import the Parser class from the PHP.Parser module
from ParserModule.Parser.PHP.Parser import Parser

# Import the Registry class from the Registry module
from Registry.Registry import Registry

# Import the necessary classes from the StructuralRegistry.Structure module
from Registry.RegistryModule.StructuralRegistry.Structure import RegistryMethod, RegistryParameter

from TreeModule.TreeElement import TreeElement


class MethodParser( Parser ):
    """
    This class parses methods.
    """
    def __init__( self ):
        super().__init__()
        # print('Initialisation MethodParser')
        # print('└─────────────────────────│')


    def parse( self, line: str, registry: Registry, tree_element: TreeElement ):
        # print('MethodParser -----> [START]')
        # Récupérer le motif regex pour les méthodes
        method_pattern = re.compile(r"""(?P<visibility>public|protected|private)?\s*(?P<abstract>abstract\s+)?function\s+(?P<method_name>\w+)\s*\((?P<method_params>.*?)\)(?:\s*:\s*(?P<return_type>\w+))?""", re.MULTILINE | re.DOTALL)

        for match in re.finditer( method_pattern, line ):
            params_str = match.group( 'method_params' )
            self.parse_parameters( params_str )

            method_element = RegistryMethod()
            method_element.set_name( match.group( 'method_name' ) )
            method_element.set_abstract( bool(match.group( 'abstract' )) )
            method_element.set_visibility( self.get_visibility(match.group( 'visibility' )) )
            method_element.set_type( self.get_type(match.group( 'return_type' )) )

            if method_element is not None:
                active_tree_element = registry.get_active_element()
                tree_element.add_child(method_element)
                registry.set_active_element(tree_element)

        # print('MethodParser -----> [DONE]')


    def parse_parameters( self, params_str ):
        """
        This function parses the parameters of a method.

        Args:
            params_str (str): The string containing the parameters.

        Returns:
            list: A list of RegistryParameter objects.
        """
        # print('parse_parameters -----> [START]')
        param_pattern = re.compile(r"""(?P<param_type>\w+)?\s*\$(?P<param_name>\w+)""")
        param_elements = []
        for match in re.finditer( param_pattern, params_str ):
            param_element = RegistryParameter()
            param_element.set_name( match.group('param_name') )
            param_element.set_type( self.get_type(match.group( 'param_type' )) )
            param_elements.append( param_element )
        # print('parse_parameters -----> [DONE]')
        return param_elements
