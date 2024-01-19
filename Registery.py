class Registery:
    def __init__(self):
        self.registry = {}

    def add_parent(self, element):
        if element not in self.registry:
            self.registry[element] = {"children": []}

    def add_child(self, parent, child):
        if parent in self.registry:
            self.registry[parent]["children"].append(child)

    def get_children(self, parent):
        return self.registry.get(parent, {}).get("children", [])

    def get_class_info(self, class_name):
        return self.registry.get(class_name, None)

    def get_all_classes(self):
        return self.registry
