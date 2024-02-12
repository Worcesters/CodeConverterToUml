from abc import ABC, abstractmethod
from Registry.Registry import Registry
from ParserModule.Parser.Interface import IParser
from typing import Optional, Type
from Registry.RegistryModule.StructuralRegistry.Structure import (RegistryVisibility, RegistryType)


class Parser( IParser ):

    def __init__( self ):
        self.visibility_mapping: dict = {
            'public': RegistryVisibility.PUBLIC,
            'protected': RegistryVisibility.PROTECTED,
            'private': RegistryVisibility.PRIVATE
        }
        
        self.type_mapping: dict = {
            'string': RegistryType.STRING,
            'int': RegistryType.INT,
            'float': RegistryType.FLOAT,
            'bool': RegistryType.BOOL,
            'array': RegistryType.ARRAY,
            'object': RegistryType.OBJECT,
            'null': RegistryType.NULL,
            'void': RegistryType.VOID,
            'resource': RegistryType.RESOURCE,
            'mixed': RegistryType.MIXED,
            'class': RegistryType.CLASS,
            'trait': RegistryType.TRAIT,
            'function': RegistryType.FUNCTION,
            'constant': RegistryType.CONSTANT,
            'interface': RegistryType.INTERFACE,
            'enum': RegistryType.ENUM,
            'namespace': RegistryType.NAMESPACE,
            'tuple': RegistryType.TUPLE,
            'union': RegistryType.UNION,
            'keyword': RegistryType.KEYWORD,
            'unknown': RegistryType.UNKNOWN
        }
        
    def get_visibility( self, visibility: str ) -> RegistryVisibility:
        return self.visibility_mapping[visibility] if self.visibility_mapping[visibility] is not None else RegistryVisibility.PUBLIC  
    
    def get_type( self, type: str ) -> RegistryType:
        return self.type_mapping[type] if self.type_mapping[type] is not None else RegistryType.UNKNOWN  