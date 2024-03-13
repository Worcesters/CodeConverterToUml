from abc import ABC, abstractmethod
from Registry.RelationalElement import RelationalElement

class Link( RelationalElement, ABC ):
    """
    This class represents a link in the system.
    It provides methods for getting the source and destination of the link.
    """

    @abstractmethod
    def get_source( self ):
        pass

    @abstractmethod
    def get_Destination( self ):
        pass

class Composition( Link ):
    """
    This class represents a composition link in the system.

    A composition link is a link that has an ownership semantics, which means that
    the source owns the destination.

    This class provides methods for getting the source and destination of the link.
    """

    def buildUml( self ):
        return self.get_source() + ' *-- ' + self.get_Destination()

class Heritage( Link ):
    """
    This class represents a heritage link in the system.

    A heritage link is a link that has an inheritance semantics,
    which means that the destination is a subtype of the source.

    This class provides methods for getting the source and destination of the link.
    """

    def buildUml( self ):
        """
        Builds the UML representation of this heritage link.

        Returns:
            str: The UML representation of this heritage link.
        """
        return self.get_source() + ' --|> ' + self.get_Destination()


class Association(Link):
    """
    This class represents an association link in the system.

    An association link is a link that has a 'has-a' relationship,
    which means that the source has a relationship with the destination.

    This class provides methods for getting the source and destination of the link.
    """

    def buildUml(self):
        """
        Builds the UML representation of this association link.

        Returns:
            str: The UML representation of this association link.
        """
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