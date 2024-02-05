from abc import ABC, abstractmethod, abstractclass
from Registry.RegistryModule import Registry
from ParserModule.Parser.Interface import IParser
from typing import Optional, Type


@abstractclass
class Parser(IParser):

    def __init__(self):
        self.level = 0

    def set_level(self, level: int):
        self.level = level
    
    def get_level(self):
        return self.level