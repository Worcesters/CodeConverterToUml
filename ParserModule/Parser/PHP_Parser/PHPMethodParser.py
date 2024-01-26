from ParserModule.MethodParser import MethodParser as ABS_MethodParser

class MethodParser(ABS_MethodParser):
    def __init__(self, registry):
        self.registry = registry

    def parse(self, line: str):
        print(line)
        method_pattern = re.compile(r'(?P<visibility>public|protected|private)?\s+(?P<abstract>abstract)?\s*function\s+(?P<method_name>\w+)\s*\((?P<method_params>[^)]*)\)\s*(?::\s*(?P<return_type>\w+))?\s*[{;]?')
        
        for match in re.finditer(method_pattern, line, re.MULTILINE | re.DOTALL):
            params = match.group('method_params')
            param_list = self.parse_parameters(params)
            
            method_info = {
                "name": match.group('method_name'),
                "visibility": match.group('visibility'),
                "abstract": bool(match.group('abstract')),
                "params": param_list,
                "return_type": match.group('return_type')
            }

            self.registry.get_root().add_child(method_info)

    def parse_parameters(self, params):
        param_pattern = r'\$?(?P<param_name>\w+)(?::\s*(?P<param_type>\w+))?'
        return [match.groupdict() for match in re.finditer(param_pattern, params)]