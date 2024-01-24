from typing import List

class ArbreElement:
    def __init__(self, element):
        self.element = element
        self.children = []
        self.parent = None

    def set_parent(self, parent: 'ArbreElement') -> None:
        self.parent = parent

    def add_child(self, child: 'ArbreElement') -> None:
        child.set_parent(self)
        self.children.append(child)

    def add_children(self, children: List['ArbreElement']) -> None:
        for child in children:
            self.add_child(child)

    def get_child(self, element) -> 'ArbreElement':
        for child in self.children:
            if child.element == element:
                return child
        return None

    def get_children(self) -> List['ArbreElement']:
        return self.children

    def get_parent(self) -> 'ArbreElement':
        return self.parent
