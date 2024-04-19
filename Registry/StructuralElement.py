"""Module providing a abstract class for python."""
from abc import ABC, abstractmethod
from Registry.IUmlBuilder import IUmlBuilder
from TreeModule.TreeElement import TreeElement

class StructuralElement( IUmlBuilder, ABC ):
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

    def __init__(self, config, tree_element: TreeElement) -> None:
        self.config = config
        self.tree_element = tree_element

    def buildUml( self ) -> str:

        # print(f'Building UML for {self.__class__.__name__}')
        # print(self.tree_element)
        # print(f'Children count: {len(self.tree_element.get_children())}')

        uml_str = ''
        for element in self.tree_element.get_children():
            # print(f'Adding UML for {element.__class__.__name__}')
            # print(f'element.buildUml(): {element.buildUml()}')
            uml_str += element.buildUml()

        return f"""
                @startuml

                skinparam classAttributeIconSize 0

                {uml_str}

                @enduml
        """.format( uml_str=uml_str )
