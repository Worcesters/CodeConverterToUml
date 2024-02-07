from abc import ABC, abstractmethod
from Registry.RelationalElement import RelationalElement

class Link(ABC, RelationalElement):

    def __init__(self):
       pass
    
    def get_source(self):
        pass
    
    def get_Destination(self):
        pass

class Association(Link):
    def __init__(self):
       pass
    
    
    
    def buildUml(self):
        pass
    
   