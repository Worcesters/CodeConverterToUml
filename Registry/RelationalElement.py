from abc import ABC, abstractmethod
from Registry.IUmlBuilder import IUmlBuider
from enum import Enum

class RelationalElement(IUmlBuider):
    def __init__(self):
        pass
    
    @abstractmethod
    def set_source(self, pole: 'Pole') -> 'Pole':
        pass
    
    @abstractmethod
    def set_Destination(self, pole: 'Pole') -> 'Pole':
        pass
    
    @abstractmethod
    def get_source(self) -> 'Pole':
        pass
    
    @abstractmethod
    def get_Destination(self) -> 'Pole':
        pass

class Pole():
    def __init__(self):
       self.name: str = ''
       self.cardinality: int = 1
       
class Cardinality(Enum):
    ZERO = 0
    ONE = 1
    MANY = 2