from ParserModule.Parser import Parser
from Registry.RegistryModule import Registry
import re

class MethodParser(Parser):
    def __init__(self ):
        super().set_level(2)
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
            # INSTANCIATION DES REGISTRY
            # set_MethodName
            # set_mon cul ...
            method_info = {
                "name": match.group('method_name'),
                "visibility": match.group('visibility'),
                "abstract": bool(match.group('abstract')),
                "params": param_list,
                "return_type": match.group('return_type')
            }

            registry.get_root().add_child(method_info)
            registry.get_active_element().add_child(method_info)
        print('MehtodParser -----> [DONE]')

    def parse_parameters(self, params_str, param_pattern):
        return [match.groupdict() for match in re.finditer(param_pattern, params_str)]
