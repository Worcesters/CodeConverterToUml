from TreeModule.TreeElement import TreeElement

class Tree:
    root = None

    def set_root(self, element):
        if isinstance(element, TreeElement):
            Tree.root = element
        else:
            Tree.root = TreeElement(element)
        print('TREE set_root() -----> [DONE]')
        print('├──├──├──├──├──├──├──│├──├──├──├──├──├──├──│')
        print('└───────────────────────────────────────────')

    def get_root(self):
        if Tree.root is None:
            print("WARNING: Root element is not set.")
        print('TREE get_root() -----> [DONE]')
        print('├──├──├──├──├──├──├──│├──├──├──├──├──├──├──│')
        print('└───────────────────────────────────────────')
        return Tree.root