from typing import List, Optional


class TreeElement:
    def __init__( self, element ):
        self.element = element
        self.children = []
        self.parent = None

    def set_parent( self, parent: 'TreeElement' ) -> None:
        self.parent = parent

    def add_child( self, child: 'TreeElement' ) -> None:
        child.set_parent( self )
        self.children.append(child)

    def add_children( self, children: List['TreeElement'] ) -> None:
        for child in children:
            self.add_child(child)

    def get_child( self, element ) -> Optional['TreeElement']:
        for child in self.children:
            if child.element == element:
                return child
        return None

    def get_children( self ) -> List['TreeElement']:
        return self.children

    def get_parent( self ) -> 'TreeElement':
        return self.parent
