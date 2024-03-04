from abc import ABC, abstractmethod
from Registry.RelationalElement import RelationalElement

class Link( ABC, RelationalElement ):

    def __init__( self ):
       pass

    @abstractmethod
    def get_source( self ):
        pass

    @abstractmethod
    def get_Destination( self ):
        pass

class Composition( Link ):
    def __init__( self ):
       pass

    def buildUml( self ):
        return self.get_source() + ' *-- ' + self.get_Destination()

class Heritage( Link ):
    def __init__( self ):
        pass

    def buildUml( self ):
        return self.get_source() + ' --|> ' + self.get_Destination()


class Association( Link ):
    def __init__( self ):
        pass

    def buildUml( self ):
        return self.get_source() + ' --> ' + self.get_Destination()

class Aggregation( Link ):
    def __init__( self ):
        pass

    def buildUml( self ):
        return self.get_source() + ' o--> ' + self.get_Destination()

class Implementation( Link ):
    def __init__( self ):
        pass

    def buildUml( self ):
        return self.get_source() + ' ..|> ' + self.get_Destination()

class Dependance( Link ):
    def __init__( self ):
        pass

    def buildUml( self ):
        return self.get_source() + ' ..> ' + self.get_Destination()