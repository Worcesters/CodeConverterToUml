from ParserModule.Interface import ParseInterface
import re
from abc import ABC, abstractmethod

class StructureParser(ParseInterface, ABC):
    name: str
    visibility: str
    
    def __init__(self, name: str, visibility: str):
        self.name = name
        self.visibility = visibility

    @abstractmethod
    def parse(self, line: str):
        pass