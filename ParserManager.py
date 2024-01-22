from Parser import MethodParser, StructureParser, AttributeParser
import Registery
import os
import tkinter as tk
from tkinter import filedialog

class ParserManager():
    def __init__(self):
        self.registery = Registery()
        self.current_class = None
        self.parsers = [
            StructureParser(self.registery),
            AttributeParser(self.registery),
            MethodParser(self.registery)
        ]

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

    