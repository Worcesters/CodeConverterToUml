from RegistryFactory import Registry
import os

class ParserManager():
    def __init__(self):
        self.registry = Registry()
        self.parsers = []
    
    def set_parser(self, parsers: list):
        for parser in parsers:
            self.parsers.append(parser)
    
    def reset_parsers(self):
        self.parsers.clear()

    def parse_file(self, file_paths):
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                code = file.read()

            for line in code.split('\n'):
                for parser in self.parsers:
                    parser.parse(line)

    def parse_files(self, file_paths):
        for file_path in file_paths:
            self.parse_file(file_path)

    def parse_folders(self, folder_path):
        file_paths = self.parse_files(folder_path)
        self.parse_files(file_paths)

    