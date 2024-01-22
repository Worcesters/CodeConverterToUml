from typing import List

class ArbreElement:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.children = []
        self.parent = None

    def set_parent(self, parent: 'ArbreElement') -> None:
        self.parent = parent

    def add_child(self, child: 'ArbreElement') -> None:
        child.set_parent(self)
        if self.children is None:
            self.children = child
        else:
            current_child = self.children
            while current_child.next is not None:
                current_child = current_child.next
            current_child.next = child

    def add_children(self, children: List['ArbreElement']) -> None:
        for child in children:
            self.add_child(child)

    def get_child(self, element) -> 'ArbreElement':
        current_child = self.children
        while current_child is not None:
            if current_child.element == element:
                return current_child
            current_child = current_child.next
        return None

    def get_children(self) -> List['ArbreElement']:
        result = []
        current_child = self.children
        while current_child is not None:
            result.append(current_child)
            current_child = current_child.next
        return result

    def get_parent(self) -> 'ArbreElement':
        return self.parent
