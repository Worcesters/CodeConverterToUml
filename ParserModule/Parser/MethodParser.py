from ParserModule.Interface import ParseInterface
import re

class MethodParser(ParseInterface):
    def __init__(self, registry, dispatcher):
        self.registry = registry
        self.dispatcher = dispatcher

    def parse(self, line: str):
        # Récupérer le motif regex pour les méthodes
        method_pattern_str = self.dispatcher.get_pattern('method_pattern')
        method_pattern = re.compile(method_pattern_str, re.MULTILINE | re.DOTALL)

        for match in re.finditer(method_pattern, line):
            params_str = match.group('method_params')

            # Récupérer le motif regex pour les paramètres
            params_pattern_str = self.dispatcher.get_pattern('param_pattern')
            param_pattern = re.compile(params_pattern_str)

            param_list = self.parse_parameters(params_str, param_pattern)

            method_info = {
                "name": match.group('method_name'),
                "visibility": match.group('visibility'),
                "abstract": bool(match.group('abstract')),
                "params": param_list,
                "return_type": match.group('return_type')
            }

            self.registry.get_root().add_child(method_info)

    def parse_parameters(self, params_str, param_pattern):
        return [match.groupdict() for match in re.finditer(param_pattern, params_str)]
