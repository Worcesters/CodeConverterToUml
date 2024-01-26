from ParserModule.Interface import ParseInterface
import re
from abc import ABC, abstractmethod


class AttributeParser(ParseInterface, ABC):
    name: str
    visibility: str
    type: str
    
    def __init__(self, name: str, visibility: str, type: str):
        self.name = name
        self.visibility = visibility
        self.type = type

    @abstractmethod
    def parse(self, line: str):
        pass