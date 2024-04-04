from typing import List, Optional


class TreeElement:
    def __init__(self, element):
        self.element = element
        self.children: List['TreeElement'] = []
        self.parent: Optional['TreeElement'] = None

    def __str__(self):
        return f"Element: {self.element}, Children: {self.children}, Parent: {self.parent}"

    def set_parent(self, parent: 'TreeElement') -> None:
        print(f"Setting parent to: {parent}")
        self.parent = parent

    def add_child(self, child) -> None:
        # Vérifier si l'objet passé en paramètre a une méthode set_parent
        if hasattr(child, 'set_parent'):
            child.set_parent(self)
            self.children.append(child)
            print(f"Added child: {child} to parent: {self}")
        else:
            print(f"Cannot add child. Invalid type.")

    def add_children(self, children: List['TreeElement']) -> None:
        for child in children:
            self.add_child(child)

    def get_child(self, element) -> Optional['TreeElement']:
        for child in self.children:
            if child.element == element:
                return child
        return None

    def get_children(self) -> List['TreeElement']:
        return self.children

    def get_parent(self) -> Optional["TreeElement"]:
        """Return the parent element or None."""
        return self.parent
