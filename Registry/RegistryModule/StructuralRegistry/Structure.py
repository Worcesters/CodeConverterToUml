from typing import List
from Registry.StructuralElement import StructuralElement



class Structure( StructuralElement ):
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
    # def __init__( self ):
    #     """
    #     Initialize a new class structure.
    #     """
    #     super().__init__()


    def buildUml( self ):
        """
        Build the UML representation of the class.

        Returns:
            str: The UML representation of the class.
        """


        # attributes_uml = ''.join([attr.buildUml() for attr in self.attributes])
        # methods_uml = ''.join([meth.buildUml() for meth in self.methods])
        class_uml = "class "+ self.name + " {\n"
        return class_uml


class RegistryInterface( Structure ):
    """
    Interface structure.
    """
    # def __init__( self ):
    #     super().__init__()

    def buildUml( self ):
        """
        Build the UML representation of the interface.

        Returns:
            str: The UML representation of the interface.
        """
        print('interface builder')
        methods_uml = '\n    '.join([meth.buildUml() for meth in self.methods])
        return f"interface {self.name} {{\n {methods_uml}\n}}\n"


class RegistryEnum( Structure ):
    """
    Enum structure.
    """
    # def __init__(self):
    #     super().__init__()

    def buildUml(self):
        """
        Build the UML representation of the enum.

        Returns:
            str: The UML representation of the enum.
        """
        print ('enum builder')
        return f"enum {self.name}\n\n"


class RegistryAttribute( StructuralElement ):
    """
    Attribute structure.
    """
    def __init__(self):
        super().__init__()
        self.owner = None

    def set_parent(self, parent):
        self.owner = parent

    def get_parent(self):
        return self.owner

    def buildUml(self):
        """
        Build the UML representation of the attribute.

        Returns:
            str: The UML representation of the attribute.
        """
        if self.mutability:
            return f"{self.visibility} {self.name}\n\n"
        else:
            return f"{self.visibility} const {self.name} : {self.element_type}\n\n"


class RegistryMethod( StructuralElement ):
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
        """
        Set the parent of the method.

        Args:
            parent (RegistryMethod | RegistryFunction): The new parent of the method.
        """
        self.owner = parent

    def buildUml(self):
        self.parameters = [param.buildUml() if isinstance(param, RegistryParameter) else param for param in self.parameters]
        return f"{self.visibility} {self.name}({', '.join(self.parameters)}) : {self.element_type}\n\n"

class RegistryParameter( StructuralElement ):
    """
    Parameter structure.
    """
    def __init__(self):
        """
        Initialize a new RegistryParameter.

        """
        super().__init__()
        self.owner = None  # The owner of the parameter, can be a method or a function

    def set_parent(self, parent):
        """
        Set the parent of the parameter.

        Args:
            parent (RegistryMethod | RegistryFunction): The new parent of the parameter.
        """
        self.owner = parent  # Set the owner of the parameter to the given parent

    def buildUml(self):
        return  f"{self.name}: {self.element_type}"
