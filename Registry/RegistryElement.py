from TreeModule.TreeElement import TreeElement
from abc import ABC, abstractmethod
class RegistryElement(TreeElement):
    def __init__(self):
        pass
    
    @abstractmethod
    def buildUml(self):
        pass


class StructureRegistry(RegistryElement):
    def __init__(self):
        pass
    
    def set_name(self):
        pass
    
class AttributeRegistry(StructureRegistry):
    def __init__():
        pass

    def buildUml(self):
        pass
    
class MethodRegistry(StructureRegistry):
    def __init__():
        pass
    
    def set_visibility(self):
        pass
    
    def set_abstract(self):
        pass
    
    def set_return_type(self):
        pass
    
    def buildUml(self):
        pass

class ParamsRegistry(StructureRegistry):
    def __init__():
        pass
    
    def set_params(self):
        pass
    
    def buildUml(self):
        pass
    
class VisibilityRegistry(StructureRegistry):
    def __init__():
        pass
    
    def set_visibility(self):
        pass
    
    def buildUml(self):
        pass
    
class TypeRegistry(StructureRegistry):
    def __init__():
        pass
    
    def set_type(self): 
        pass
    
    def buildUml(self):
        pass
    
class HeritageRegistry(StructureRegistry):
    def __init__():
        pass
    
    def set_extends(self):
        pass
    
    def set_implements(self):
        pass

class ClassRegistry(StructureRegistry):
    def __init__():
        pass
    
    def buildUml(self):
        pass

class InterfaceRegistry(StructureRegistry):
    def __init__():
        pass
    
    def buildUml(self):
        pass
    
class EnumRegistry(StructureRegistry):
    def __init__():
        pass
    
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