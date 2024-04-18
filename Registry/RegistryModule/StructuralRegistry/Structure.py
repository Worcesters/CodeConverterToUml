from enum import Enum
from typing import List
from Registry.StructuralElement import StructuralElement

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

class RegistryCommonElement(StructuralElement):
    """
    Base class for common elements in the registry.
    """

    def __init__(self, name: str = '', visibility: 'RegistryVisibility' = RegistryVisibility.PUBLIC,
                 element_type: 'RegistryType' = RegistryType.UNKNOWN):
        """
        Initialize a new RegistryCommonElement.

        Args:
            name (str): The name of the element.
            visibility (RegistryVisibility): The visibility of the element.
            element_type (RegistryType): The type of the element.
        """

        self.mutability = True  # Whether the element is mutable
        self.name = name  # The name of the element
        self.visibility = visibility  # The visibility of the element
        self.element_type = element_type  # The type of the element

    def set_mutability(self, mutability: bool):
        """
        Set the mutability of the element.

        Args:
            mutability (bool): The new mutability value.
        """
        self.mutability = mutability

    def set_name(self, name: str):
        """
        Set the name of the element.

        Args:
            name (str): The new name.
        """
        if name:
            self.name = name

    def set_visibility( self, visibility: 'RegistryVisibility' ):
        """
        Set the visibility of the element.

        Args:
            visibility (RegistryVisibility): The new visibility.
        """
        if visibility:
            self.visibility = visibility

    def set_type( self, element_type: 'RegistryType' ):
        """
        Set the type of the element.

        Args:
            element_type (RegistryType): The new type.
        """
        if element_type:
            self.element_type = element_type

class Structure( RegistryCommonElement ):
    """
    Base class for structural elements.

    Attributes:
        attributes (List[RegistryAttribute]): The list of attributes of the structure.
        methods (List[RegistryMethod]): The list of methods of the structure.
    """
    def __init__( self ):
        super().__init__()
        self.attributes: List['RegistryAttribute'] = []  # List of attributes, empty by default
        self.methods: List['RegistryMethod'] = []  # List of methods, empty by default

    def add_attribute( self, attribute: 'RegistryAttribute' ):
        """
        Add an attribute to the structure.

        Args:
            attribute (RegistryAttribute): The attribute to add.
        """
        if isinstance(attribute, RegistryAttribute):  # Check the correct element_type
            self.attributes.append(attribute)
            attribute.set_parent(self)

    def add_method( self, method: 'RegistryMethod' ):
        """
        Add a method to the structure.

        Args:
            method (RegistryMethod): The method to add.
        """
        if isinstance(method, RegistryMethod):
            self.methods.append(method)
            method.set_parent(self)


class RegistryClass( Structure ):
    """
    Class structure.
    """
    def __init__( self ):
        """
        Initialize a new class structure.
        """
        super().__init__()

    def buildUml( self ):
        """
        Build the UML representation of the class.

        Returns:
            str: The UML representation of the class.
        """
        attributes_uml = '\n\t'.join([attr.buildUml() for attr in self.attributes])
        methods_uml = '\n\t'.join([meth.buildUml() for meth in self.methods])
        return f"class {self.name} {{\n\t{attributes_uml}\n\t{methods_uml}\n}}"


class RegistryInterface( Structure ):
    """
    Interface structure.
    """
    def __init__( self ):
        super().__init__()

    def buildUml( self ):
        """
        Build the UML representation of the interface.

        Returns:
            str: The UML representation of the interface.
        """
        methods_uml = '\n    '.join([meth.buildUml() for meth in self.methods])
        return f"interface {self.name} {{\n    {methods_uml}\n}}"


class RegistryEnum( Structure ):
    """
    Enum structure.
    """
    def __init__(self):
        super().__init__()

    def buildUml(self):
        """
        Build the UML representation of the enum.

        Returns:
            str: The UML representation of the enum.
        """
        return f"enum {self.name}"


class RegistryAttribute( RegistryCommonElement ):
    """
    Attribute structure.
    """
    def __init__(self):
        super().__init__()
        self.owner = None

    def set_parent(self, parent):
        self.owner = parent

    def buildUml(self):
        """
        Build the UML representation of the attribute.

        Returns:
            str: The UML representation of the attribute.
        """
        if self.mutability:
            return f"{self.visibility} {self.name}"
        else:
            return f"{self.visibility} const {self.name} : {self.element_type}"


class RegistryMethod( RegistryCommonElement ):
    """
    Method structure.
    """
    def __init__(self):
        super().__init__()
        self.parameters: List['RegistryParameter'] = []
        self.abstract: bool = False
        self.owner = None

    def set_abstract(self, abstract: bool):
        """
        Set the abstract status of the method.

        Args:
            abstract (bool): The new abstract status.
        """
        self.abstract = abstract

    def set_parent(self, parent):
        self.owner = parent

    def buildUml(self):
        parameters_uml = ', '.join([param.buildUml() for param in self.parameters])
        return f"{self.visibility.value} {self.name}({parameters_uml}) : {self.element_type.value}"

class RegistryParameter( RegistryCommonElement ):
    def __init__( self ):
        super().__init__()

    def buildUml(self):
        return self.name + ': ' + self.element_type
