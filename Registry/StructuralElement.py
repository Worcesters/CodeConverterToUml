from TreeModule.TreeElement import TreeElement
from abc import ABC, abstractmethod
from Registry.IUmlBuilder import IUmlBuilder

class StructuralElement( TreeElement, IUmlBuilder ):
    def __init__( self ):
        pass

class RegistryProgram( StructuralElement ):
    def __init__( self ):
        pass

    def buildUml( self ):
        uml_str = ''
        for element in self.get_children():
            uml_str += element.buildUml()

        return f"""
                @startuml

                skinparam classAttributeIconSize 0

                {uml_str}

                @enduml
        """.format( uml_str=uml_str )