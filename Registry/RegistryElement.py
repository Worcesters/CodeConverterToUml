from TreeModule.TreeElement import TreeElement
from abc import ABC, abstractmethod


class RegistryElement(TreeElement):
    def __init__(self):
        pass
    
    @abstractmethod
    def buildUml(self):
        pass

class ProgramRegistry(RegistryElement):
    def __init__(self):
        pass
    
    def buildUml(self):
        uml_str = ''
        for element in self.get_children():
           uml_str += element.buildUml()
            
        return """
                @startuml

                skinparam classAttributeIconSize 0
                
                {uml_str}

                @enduml
        """.format(uml_str=uml_str)