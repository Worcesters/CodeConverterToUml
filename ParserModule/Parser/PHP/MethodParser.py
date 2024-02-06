from ParserModule.Parser import Parser
from Registry.Registry import Registry
from Registry.RegistryElement import (
    MethodRegistry,
    VisibilityRegistry,
    TypeRegistry,
    ParamsRegistry
)
import re

class MethodParser(Parser):
    def __init__(self):
        print('Initialisation MethodParser')
        print('└─────────────────────────│')
        

    def parse(self, line: str, registry: Registry):
        print('MethodParser -----> [START]')
        # Récupérer le motif regex pour les méthodes
        method_pattern = re.compile(r"""(?P<visibility>public|protected|private)?\s*(?P<abstract>abstract\s+)?function\s+(?P<method_name>\w+)\s*\((?P<method_params>.*?)\)(?:\s*:\s*(?P<return_type>\w+))?""", re.MULTILINE | re.DOTALL)

        for match in re.finditer(method_pattern, line):
            params_str = match.group('method_params')

            # Récupérer le motif regex pour les paramètres
            param_pattern = re.compile(r"""(?P<param_type>\w+)?\s*\$(?P<param_name>\w+)""")

            param_list = self.parse_parameters(params_str, param_pattern)
       
            method_element = MethodRegistry()
            method_element.set_name(match.group('method_name'))
            method_element.set_return_type(match.group('return_type'))
            method_element.set_abstract(bool(match.group('abstract')))
            
            params_element = ParamsRegistry()
            params_element.set_params(param_list)
            
            type_element = TypeRegistry()
            type_element.set_type(match.group('param_type'))

            visibility_element = VisibilityRegistry()
            visibility_element.set_visibility(match.group('visibility'))
            

            registry.get_active_element().add_child(method_element)
            registry.set_active_element()
            
        print('MehtodParser -----> [DONE]')

    def parse_parameters(self, params_str, param_pattern):
        return [match.groupdict() for match in re.finditer(param_pattern, params_str)]
