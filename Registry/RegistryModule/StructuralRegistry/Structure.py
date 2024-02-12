from enum import Enum
from Registry.StructuralElement import StructuralElement
from typing import Optional, List
from abc import ABC, abstractmethod

class RegistryVisibility( Enum ):
    PUBLIC = "+"
    PROTECTED = "#"
    PRIVATE = "-"
    
class RegistryType( Enum ):
    STRING = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    ARRAY = "array"
    OBJECT = "object"
    NULL = "null"
    VOID = "void"
    RESOURCE = "resource"
    MIXED = "mixed"
    CLASS = "class"
    TRAIT = "trait"
    FUNCTION = "function"
    CONSTANT = "constant"
    INTERFACE = "interface"
    ENUM = "enum"
    NAMESPACE = "namespace"
    TUPLE = "tuple"
    UNION = "union"
    KEYWORD = "keyword"
    UNKNOWN = "unknown"


class RegistryCommonElement( StructuralElement ):
    def __init__( self, name: str = '', visibility: 'RegistryVisibility' = RegistryVisibility.PUBLIC, type: 'RegistryType' = RegistryType.UNKNOWN ):
        self.mutability = True
        self.name = name
        self.visibility = visibility
        self.type = type

    def set_mutability( self, mutability: bool ):
        self.mutability = mutability

    def set_name( self, name: str ):
        if name:
            self.name = name
    
    def set_visibility( self, visibility: 'RegistryVisibility' ):
        if visibility:
            self.visibility = visibility
    
    def set_type( self, type: 'RegistryType' ):
        if type:
            self.type = type
    
class Structure( RegistryCommonElement ):
    def __init__( self ):
        super().__init__()
        self.attributes: 'List[RegistryAttribute]' = []  # Liste vide par défaut
        self.methods: 'List[RegistryMethod]' = []  # Liste vide par défaut
    
    def add_attribute( self, attribute: 'RegistryAttribute' ):
        if isinstance( attribute, RegistryAttribute ):  # Correction pour vérifier le type correct
            self.attributes.append(attribute)
            attribute.set_owner( self )
        
    def add_method( self, method: 'RegistryMethod' ):
        if isinstance( method, RegistryMethod ):
            self.methods.append(method)
            method.set_owner( self )

class RegistryClass( Structure ):
    def __init__( self ):
        super().__init__()
    
    def buildUml(self):
        attributes_uml = '\n    '.join([attr.buildUml() for attr in self.attributes])
        methods_uml = '\n    '.join([meth.buildUml() for meth in self.methods])
        return f"class {self.name} {{\n    {attributes_uml}\n    {methods_uml}\n}}\n"


class RegistryInterface( Structure ):
    def __init__( self ):
        super().__init__()
        
    def buildUml(self):
        methods_uml = '\n    '.join([meth.buildUml() for meth in self.methods])
        return f"interface {self.name} {{\n    {methods_uml}\n}}\n"

class RegistryEnum( Structure ):
    def __init__( self ):
        super().__init__()
        
    def buildUml( self ):
        return 'enum ' + self.name

class RegistryAttribute( RegistryCommonElement ):
    def __init__( self ):
        super().__init__()
    
    def buildUml( self ):
        #TODO : voir pour la condition de la mutabilité
        return f"{self.visibility.value} {self.name} : {self.type.value}"
        
class RegistryMethod( RegistryCommonElement ):
    def __init__( self ):
        super().__init__()
        self.parameters: 'List[RegistryParameter]' = []
        self.abstract: bool = False
            
    def set_abstract( self, abstract: bool ):
        self.abstract = abstract
    
    def buildUml(self):
        parameters_uml = ', '.join([param.buildUml() for param in self.parameters])
        return f"{self.visibility.value} {self.name}({parameters_uml}) : {self.type.value}"

class RegistryParameter( RegistryCommonElement ):
    def __init__( self ):
        super().__init__()
        
    def buildUml( self ):
        return f"{self.name} : {self.type.value}"