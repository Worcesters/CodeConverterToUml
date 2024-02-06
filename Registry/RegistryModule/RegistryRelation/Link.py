from abc import ABC, abstractmethod
from Registry.RegistryElement import RegistryElement

class Link(ABC, RegistryElement):

    @abstractmethod
    def get_source(self):
        pass
    
    @abstractmethod
    def get_Destination(self):
        pass