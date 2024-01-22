from interface import ParseInterface
import re

class MethodParser(ParseInterface):
    def __init__(self, registery, current_class):
        self.registery = registery
        self.current_class = current_class

    def parse(self, line: str):
        if self.current_class:
            
            method_pattern = re.compile(r'(?P<visibility>public|protected|private)?\s+(?P<abstract>abstract)?\s*function\s+(?P<method_name>\w+)\s*\((?P<method_params>[^)]*)\)\s*(?::\s*(?P<return_type>\w+))?\s*[{;]?')
            
            for match in re.finditer(method_pattern, line, re.MULTILINE | re.DOTALL):
                visibility = match.group('visibility')
                abstract = match.group('abstract')
                method_name = match.group('method_name')
                params = match.group('method_params')
                return_type = match.group('return_type')
                param_list = self.parse_parameters(params)
                
                method_info = {
                    "name": method_name,
                    "visibility": visibility,
                    "abstract": bool(abstract),
                    "params": param_list,
                    "return_type": return_type
                }
                self.registery.add_children(self.current_class, method_info)
    
    def parse_parameters(self, params):
        param_pattern = r'\$?(?P<param_name>\w+)(?::\s*(?P<param_type>\w+))?'
        return [match.groupdict() for match in re.finditer(param_pattern, params)]