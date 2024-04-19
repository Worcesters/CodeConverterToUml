from typing import List, Optional


class TreeElement:
    def __init__(self, element: Optional[object] = None):
        self.element = element
        self.children: List['TreeElement'] = []
        self.parent: Optional['TreeElement'] = None

    # def __str__(self):
    #     # print(f"TREE __str__ - element: {self.element} - children: {self.children} - parent: {self.parent}")
    #     return f"Element: {self.element}, Children: {self.children}, Parent: {self.parent}"

    def set_parent(self, parent: 'TreeElement') -> None:
        # print(f"TREE set_parent - parent: {parent}")
        self.parent = parent

    def add_child(self, child: 'TreeElement') -> None:
        # print(f"TREE add_child - child: {child}")
        # Vérifier si l'objet passé en paramètre a une méthode set_parent
        if hasattr(child, 'set_parent'):
            # print(f"TREE add_child - calling child.set_parent(self) - child: {child} - self: {self}")
            child.set_parent(self)
            self.children.append(child)
            # print(f"TREE add_child - added child: {child} to parent: {self}")
        else:
            # print(f"TREE add_child - Cannot add child. Invalid type. child: {child}")
            pass

    def add_children(self, children: List['TreeElement']) -> None:
        # print(f"TREE add_children - children: {children}")
        for child in children:
            self.add_child(child)

    def get_child(self, element) -> Optional['TreeElement']:
        # print(f"TREE get_child - element: {element}")
        for child in self.children:
            if child.element == element:
                return child
        return None

    def get_children(self) -> List['TreeElement']:
        return self.children

    def get_parent(self) -> Optional["TreeElement"]:
        """Return the parent element or None."""
        # print(f"TREE get_parent")
        return self.parent

