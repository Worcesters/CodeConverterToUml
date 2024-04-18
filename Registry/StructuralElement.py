"""Module providing a abstract class for python."""
from abc import ABC, abstractmethod
from TreeModule.TreeElement import TreeElement
from Registry.IUmlBuilder import IUmlBuilder

class StructuralElement( TreeElement, IUmlBuilder, ABC ):
    """
    Base class for all structural elements that can be represented in UML
    """

    @abstractmethod
    def buildUml( self ) -> str:
        """
        Builds UML representation of the structural element

        :return: UML representation of the structural element
        """
        print(f'Building uml for {self.__class__.__name__}')

class RegistryProgram( StructuralElement ):
    """
    Represents a registry program, which is the top level element of the registry

    The registry program is the root of the tree and contains all the other
    structural elements of the code.
    """
    def buildUml( self ):

        print(f'Building UML for {self.__class__.__name__}')

        uml_str = ''
        for element in self.get_children():
            print(f'Adding UML for {element.__class__.__name__}')
            print(f'element.buildUml(): {element.buildUml()}')
            uml_str += element.buildUml()

        print(f'Finished building UML for {self.__class__.__name__}')

        return f"""
                @startuml

                skinparam classAttributeIconSize 0

                {uml_str}

                @enduml
        """.format( uml_str=uml_str )
