from ParserModule.Interface import ParseInterface
import re
from abc import ABC, abstractmethod

class MethodParser(ParseInterface, ABC):
    visibility: str
    name: str
    abstract: bool
    params: list
    return_type: str
    
    def __init__(self, visibility: str, name: str, abstract: bool, params: list, return_type: str):
        self.visibility = visibility
        self.name = name
        self.abstract = abstract
        self.params = params
        self.return_type = return_type
    
    @abstractmethod
    def parse(self, line: str):
        pass