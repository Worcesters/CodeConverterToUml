import CodeConverterRegistry
import os
import tkinter as tk
from tkinter import filedialog

class ParserManager():
    def __init__(self):
        self.code_converter_registry = CodeConverterRegistry()
        self.parsers = [
            #StructureParser(self.code_converter_registry),
            #AttributeParser(self.code_converter_registry),
            #MethodParser(self.code_converter_registry)
        ]
    
    def set_parser(self, parsers: list):
        for parser in parsers:
            self.parsers.append(parser)
    
    def reset_parsers(self):
        self.parsers.clear()

    def parse_file(self, file_path):
        if os.path.exists(file_path):
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

    