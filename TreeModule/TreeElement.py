from typing import List, Optional


class TreeElement:
    """
    Represents a tree element, which is an element of a tree structure.

    A tree element has a parent element and zero or more child elements.
    """

    def __init__(self, element: Optional[object] = None):
        """
        Initializes the tree element.

        The tree element is empty after initialization.
        """
        self.element = element
        self.children: List['TreeElement'] = []
        self.parents: List['TreeElement'] = []
        self.parent: Optional['TreeElement'] = None
        self.heritages: List['TreeElement'] = []


    def add_herits(self, heritage: 'TreeElement') -> None:
        """
        Adds a child element to the tree element.

        Args:
            child: The child element to add.
        """
        #child.set_parent(self)
        self.heritages.append(heritage)

    def set_parent(self, parent: 'TreeElement') -> None:
        """
        Sets the parent element of the tree element.

        Args:
            parent: The parent element to set.
        """
        self.parent = parent

    def add_parent(self, parent: 'TreeElement') -> None:
        self.parents.append(parent)

    def add_child(self, child: 'TreeElement') -> None:
        """
        Adds a child element to the tree element.

        Args:
            child: The child element to add.
        """
        #child.set_parent(self)
        self.children.append(child)

    def add_children(self, children: List['TreeElement']) -> None:
        """
        Adds multiple child elements to the tree element.

        Args:
            children: The child elements to add.
        """
        for child in children:
            self.add_child(child)

    def get_child(self, element) -> Optional['TreeElement']:
        """
        Returns a child element with the given element or None.

        Args:
            element: The element to search for.

        Returns:
            The child element with the given element or None.
        """
        for child in self.children:
            if child.element == element:
                return child
        return None

    def get_children(self) -> List['TreeElement']:
        """
        Returns a list of all child elements.

        Returns:
            A list of all child elements.
        """
        return self.children

    def get_parent(self) -> Optional["TreeElement"]:
        return self.parent

    def get_parents(self) -> List['TreeElement']:
        return self.parents

    # def get_herit(self) -> Optional["TreeElement"]:
    #     return self.heritage

    def get_herits(self) -> List['TreeElement']:
        return self.heritages
