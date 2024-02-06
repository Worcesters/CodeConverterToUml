from enum import Enum
from Registry.RegistryElement import RegistryElement

class Structure(RegistryElement):
    def __init__(self, name: str, attributes=None, methods=None):
        super().__init__()
        self.name = name
        self.attributes = attributes if attributes is not None else []  # Liste vide par défaut
        self.methods = methods if methods is not None else []  # Liste vide par défaut
        self.mutability = True  # Déplacé comme attribut d'instance

    def set_mutability(self, mutability: bool):
        self.mutability = mutability

    def set_name(self, name: str):
        if name:  # Vérifie que name n'est pas vide
            self.name = name

    def add_attribute(self, attribute: 'RegistryAttribute'):
        if isinstance(attribute, RegistryAttribute):  # Correction pour vérifier le type correct
            self.attributes.append(attribute)
            attribute.set_owner(self)
        
    def add_method(self, method: 'RegistryMethod'):
        if isinstance(method, RegistryMethod):
            self.methods.append(method)
            method.set_owner(self)

class RegistryVisibility(Enum):
    PUBLIC = "public"
    PROTECTED = "protected"
    PRIVATE = "private"
    
class RegistryType(Enum):
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

class RegistryClass(Structure):
    def __init__(self, name: str, attributes=None, methods=None):
        super().__init__(name, attributes, methods)

class RegistryInterface(Structure):
    def __init__(self, name: str, attributes=None, methods=None):
        super().__init__(name, attributes, methods)

class RegistryEnum(Structure):
    def __init__(self, name: str, attributes=None, methods=None):
        super().__init__(name, attributes, methods)

class RegistryAttribute(RegistryElement):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.owner = None  # Référence à RegistryClass, RegistryInterface, ou RegistryEnum

    def set_owner(self, owner):
        if isinstance(owner, (RegistryClass, RegistryInterface, RegistryEnum)):
            self.owner = owner

class RegistryMethod(RegistryElement):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.owner = None  # Référence à RegistryClass, RegistryInterface, ou RegistryEnum

    def set_owner(self, owner):
        if isinstance(owner, (RegistryClass, RegistryInterface, RegistryEnum)):
            self.owner = owner
