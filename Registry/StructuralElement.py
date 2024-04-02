"""Module providing a abstract class for python."""
from abc import ABC, abstractmethod
from TreeModule.Tree import Tree
from Registry.IUmlBuilder import IUmlBuilder

class StructuralElement( Tree, IUmlBuilder, ABC ):
    """
    Base class for all structural elements that can be represented in UML
    """

    @abstractmethod
    def buildUml( self ) -> str:
        """
        Builds UML representation of the structural element

        :return: UML representation of the structural element
        """

class RegistryProgram( StructuralElement ):
    """
    Represents a registry program, which is the top level element of the registry

    The registry program is the root of the tree and contains all the other
    structural elements of the code.
    """

    def buildUml( self ):
        uml_str = ''
        root = self.get_root()
        print(root)
        if root:
            for element in root.get_children():
                print(element)
                uml_str += element.buildUml()
                print( f'str {uml_str}')

        return f"""
                @startuml

                skinparam classAttributeIconSize 0

                {uml_str}

                @enduml
        """.format( uml_str=uml_str )
